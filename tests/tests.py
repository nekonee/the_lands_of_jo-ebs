import nose
import unittest

from nose.tools import assert_equals

def status(fun):
    def test_new( *args, **kwargs):
        class_name = str(fun).split('.')[0].split(' ')[1]
        print("\nRunning test: {} {}".format(class_name, fun.__name__), end =' ')
        fun(*args, **kwargs)
        print("\033[92m✓\x1b[0m")
    return test_new


@status
def sanity_test():
    assert True



class ClassTemplateTests(unittest.TestCase):
    def setUp(self):
        from classes import Rectangle, Character
        self.rect = Rectangle(2, 2, 2, 2)
        self.charr = Character(1, 1, 'A', 'black', False)

    @status
    def test_rect_positive(self):
        rect_center = self.rect.centering()
        a = rect_center[0]
        b = rect_center[1]
        assert (a + b) >= 0

    @status
    def test_charr_positive(self):
        check_charr_move = self.charr.move(2, 2)
        assert_equals ((self.charr.axis_X == 3), (self.charr.axis_Y == 3))
