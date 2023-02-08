from unittest import TestCase, main
from my_slice import MyList

my_lst = MyList([1, 4, 2, -44, 0, 5, -2, 11, 3])
lst = [1, 4, 2, -44, 0, 5, -2, 11, 3]


class MyListTest(TestCase):
    def test_normal_1_1(self):
        self.assertEqual(my_lst[3:9], lst[3:9])
        self.assertEqual(my_lst[3:-2], lst[3:-2])
        self.assertEqual(my_lst[0:-1], lst[0:-1])
        self.assertEqual(my_lst[0:-5], lst[0:-5])
        self.assertEqual(my_lst[4:4], lst[4:4])
        self.assertEqual(my_lst[1:-1], lst[1:-1])
        self.assertEqual(my_lst[-3:-6], lst[-3:-6])
        self.assertEqual(my_lst[6:3], lst[6:3])
        self.assertEqual(my_lst[0:3], lst[0:3])

    def test_normal_1_1_1(self):
        self.assertEqual(my_lst[3:9:2], lst[3:9:2])
        self.assertEqual(my_lst[3:4:2], lst[3:4:2])
        self.assertEqual(my_lst[0:-1:3], lst[0:-1:3])
        self.assertEqual(my_lst[-6:-1:1], lst[-6:-1:1])
        self.assertEqual(my_lst[-1:-6:1], lst[-1:-6:1])
        self.assertEqual(my_lst[-1:-6:-1], lst[-1:-6:-1])
        self.assertEqual(my_lst[3:9:-2], lst[3:9:-2])
        self.assertEqual(my_lst[3:-9:-2], lst[3:-9:-2])


if __name__ == '__main__':
    main()
