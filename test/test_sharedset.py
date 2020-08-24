import pytest
from src import sharedset


def test_sharedset():
    objects = sharedset.Sharedset()

    objects.add("Test")
    objects.add("String")

    assert "Test" in objects
    assert "Other Test" not in objects

    with pytest.raises(ValueError):
        sharedset.Sharedset(("Hello",), master=objects)

    sub_objects = sharedset.Sharedset(master=objects)
    sub_objects.add("Test")

    with pytest.raises(ValueError):
        sub_objects.add("Other Test")

    objects.remove("Test")

    assert len(sub_objects) == 0

    objects.add("Test", (sub_objects,))

    sub_sub_objects = sharedset.Sharedset(("Test", ), master=sub_objects)

    with pytest.raises(ValueError):
        sub_sub_objects.add("Something")

    objects.clear()

    assert len(objects) == len(sub_objects) == len(sub_sub_objects) == 0

    sub_objects.remove_subset(sub_sub_objects)

    assert sub_sub_objects.master is None

    objects.add(1)
    objects.add(2)
    objects.add(3)

    a = list(objects)
    assert 1 in a and 2 in a and 3 in a
    assert str(objects)

    with pytest.raises(ValueError):
        objects.add(4, (sharedset.Sharedset(),))

    new_subset = sharedset.Sharedset()
    objects.add_subset(new_subset)

    assert new_subset in objects.subsets
    assert new_subset.master == objects

    with pytest.raises(ValueError):
        sub_objects.add_subset(new_subset)
