import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import json
import codecs
import unittest

from addresscleaner import parse_address

class TestAddressParsing(unittest.TestCase):
    def test_cases(self):
        filename = os.path.join(os.path.dirname(__file__), "test_cases")
        with codecs.open(filename, 'r', 'utf-8') as fh:
            raw = fh.read()
        parts = raw.split("====")
        for part in parts:
            if not part.strip():
                continue
            txt, jsontxt = part.split("----")
            expected = json.loads(jsontxt)
            actual = parse_address(txt)
            self.assertEquals(actual, expected)

if __name__ == "__main__":
    unittest.main()
