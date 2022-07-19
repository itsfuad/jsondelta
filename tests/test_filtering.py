import unittest
from filtering import without_paths

class FilterTests(unittest.TestCase):
    def test_nested_ignore(self):
        changes = [("$['meta']['timestamp']",'changed',1,2), ("$['value']",'changed',1,2)]
        self.assertEqual(without_paths(changes,["$['meta']"]),[changes[1]])
    def test_prefix_boundary(self):
        changes = [("$['name2']",'added',None,1)]
        self.assertEqual(without_paths(changes,["$['name']"]),changes)

if __name__ == '__main__': unittest.main()
