"""Unit tests for fnv1a module"""
from __future__ import annotations
import unittest
from fnv1a import FNV1a


class TestModule(unittest.TestCase):
    """Test all functionality for fnv1a module"""
    _text: str = ("FNV1a(seed=14695981039346656037,\n"
                  "      prime=1099511628211,\n"
                  "      mask=18446744073709551615,\n"
                  "      text=None,\n"
                  "      hash_out=None,\n"
                  "      hash_list=[])")
    _test_string: str = "This is a test.com bro."

    def test_hash(self) -> None:
        """Test hashing function."""
        hasher: FNV1a = FNV1a()
        test: str | None = hasher.hash(self._test_string)
        self.assertEqual(test, 'ade2f4095d74bf44')

    def test_repr(self) -> None:
        """Test __repr__ function."""
        hasher: FNV1a = FNV1a()
        self.assertEqual(str(hasher), self._text)

    def test_dehash(self) -> None:
        """Test dehash function."""
        hasher: FNV1a = FNV1a()
        hasher.hash(self._test_string)
        new_hasher: FNV1a = FNV1a()
        self.assertEqual(FNV1a().dehash([]), "")
        test: str | None = new_hasher.dehash(hasher.hash_list)
        self.assertEqual(test, self._test_string)
        self.assertEqual(new_hasher.dehash([]), self._test_string)

        # Test exception throwing for improper arguments
        self.assertRaises(TypeError, new_hasher.dehash, 1234)
        self.assertRaises(TypeError, new_hasher.dehash, ["test"])
        self.assertRaises(ValueError, new_hasher.dehash, [123412341, 34123412])


if __name__ == '__main__':
    unittest.main()
