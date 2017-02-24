import unittest
from lessonI import LessonI


class _100doors_main_test_case():
    def test_main_should_not_return_value(self):
        result = LessonI.naive(1)
        self.assertEqual(result, None)


def test_main():
    unittest.main()

if __name__ == '__main__':
    test_main()