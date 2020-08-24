"""
This module implements a shared set. 

It makes it possible to have a master set and subsets that reference 
parts of the master set. It has the following properties:

- Removing items from the master set will recursively remove them from all
  subsets

- Inserting items into the master set will allow them to be inserted into
  any of the subsets

- Subsets cannot contain elements which are not present in the master set

- Removing items from subsets will not remove them from the master set

- Insertion and removal have O(1) time complexity
"""


class Sharedset:
    """
    Wrapper around Python's set class that allows subsets.

    Args:
        iterable (iterable): Initial values for the set
        master (Sharedset): Master set

    Attributes:
        master (Sharedset): Master set
        subsets (set[Sharedset]): Set of subsets
    """

    def __init__(self, iterable=[], master=None):
        self._py_set = set(iterable)

        self.master = master
        self.subsets = set()

        if master is not None:
            if not self._py_set.issubset(master._py_set):
                raise ValueError(
                    "Set can't have elements not present in master.")

            master.subsets.add(self)

    def __str__(self):
        return self._py_set.__str__()

    def __iter__(self):
        return iter(self._py_set)

    def __contains__(self, element):
        return self._py_set.__contains__(element)

    def __len__(self):
        return self._py_set.__len__()

    def add(self, element, subsets=()):
        """
        Add an element to the sharedset

        Args:
            element (hashable): Element to be added
            subsets (iterable): Iterable containing subsets the element should
                                be added to in addition to the master set.
        """

        if self.master:
            if not element in self.master:
                raise ValueError(
                    "Can't add element not present in master to subset")

        self._py_set.add(element)

        for subset in subsets:
            if not subset in self.subsets:
                raise ValueError("Can't specify set not flagged as subset.")

            subset.add(element)

    def add_subset(self, other):
        """
        Adds a new subset to the current set.

        Args:
            other (Sharedset): Set to be added as a subset
        """

        if other.master:
            raise ValueError("Subset can't have more than one master")

        other.master = self
        self.subsets.add(other)

    def remove(self, element):
        """
        Removes an element from the set and all subsets.

        Args:
            element (hashable): Element to be removed
        """

        self._py_set.remove(element)

        for subset in self.subsets:
            if element in subset:
                subset.remove(element)

    def remove_subset(self, subset):
        """
        Removes a subset from the current set.

        Args:
            subset (Sharedset): Subset to be removed
        """

        self.subsets.remove(subset)

        subset.master = None

    def clear(self):
        """
        Clears the set and all subsets.
        """

        self._py_set.clear()

        for subset in self.subsets:
            subset.clear()
