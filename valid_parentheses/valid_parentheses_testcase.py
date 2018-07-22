import unittest
from valid_parentheses import isValid


class tests(unittest.TestCase):
    def test(self):
        self.assertEqual(isValid("([)"), False)
        self.assertEqual(isValid("([][)"), False)
        self.assertEqual(isValid("([]))"), False)
        self.assertEqual(isValid("([]){)}[]"), False)
        self.assertEqual(isValid("([]){()}[]"), True)
        self.assertEqual(isValid("{}[]()"), True)
        self.assertEqual(isValid("{[]}()"), True)
        self.assertEqual(isValid("({[]})"), True)

unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
