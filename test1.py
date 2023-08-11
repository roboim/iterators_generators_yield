class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.curlist = []
        self.i = 0
        self.index = -1
        return self

    def __next__(self):

        if self.i >= len(self.list_of_list):
            raise StopIteration
        self.index += 1
        self.curlist = self.list_of_list[self.i]
        item = self.curlist[self.index]
        if self.index >= len(self.curlist) - 1:
            self.index = -1
            self.i += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
