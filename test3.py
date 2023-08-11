class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flatten(self.list_of_list)
        self.i = -1
        return self

    def __next__(self):
        if self.i >= len(self.flat)-1:
            raise StopIteration
        self.i += 1
        self.item = self.flat[self.i]
        return self.item

    def flatten(self, nested):
        self.flat = []
        self.nested = nested

        def helper(nested):
            for e in nested:
                if isinstance(e, list):
                    helper(e)
                else:
                    self.flat.append(e)

        helper(nested)
        return self.flat

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()