import unittest
import regular_expressions as passcheck

class TestPassword(unittest.TestCase):
    def test_valid_password(self):
        password = 'asdf1234'
        test = passcheck.check_password(password)
        self.assertTrue(test)

    def test_invalid_passwords(self):
        passwords = ['1234', 'asdf:1234', ':14%#@fE4v']
        for word in passwords:
            test = passcheck.check_password(word)
            self.assertFalse(test)


if __name__ == '__main__':
    unittest.main()
