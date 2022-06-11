import unittest
from jsondelta import compare

class DiffTests(unittest.TestCase):
    def test_equal(self): self.assertEqual(compare({'a': [1]}, {'a': [1]}), [])
    def test_nested(self):
        changes = compare({'a': [1,2], 'drop': 5}, {'a': [1,3,4], 'add': True})
        self.assertEqual([c[1] for c in changes], ['changed','added','added','removed'])
    def test_types(self):
        self.assertEqual(compare(True,1)[0][1],'type')
        self.assertEqual(compare(None,[])[0][1],'type')

if __name__ == '__main__': unittest.main()
