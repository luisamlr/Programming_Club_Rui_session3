#8
# Linear Search is a simple algorithm that you can use to search for an item in a list
# or (list of) string. It can be expressed in pseudo-code as:


@pytest.mark.parametrize('alist, positions, new', [
    ([1, 2, 3, 4], [1], [1, 3, 3, 4]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 3, 5, 6], [1, 1, 2, 4, 4, 6, 7, 7, 8]),
    ([10, 20, 30, 40, 50], [0, 2, 4], [11, 20, 31, 40, 51]),
    ([], [], [])
])
def test_modify_list(alist, positions, new):
    assert exercise7.modify_list_by_reference(alist, positions, new) == new
