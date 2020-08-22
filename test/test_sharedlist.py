from src import sharedlist


def test_sharedlist():
    lst = sharedlist.SharedList()

    lst.push_back("a")
    lst.push_back("b")
    lst.push_back("c")

    assert len(lst) == 3


    

