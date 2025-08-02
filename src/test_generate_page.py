import unittest

from generate_page import extract_title


class GeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        html = extract_title(md)
        self.assertEqual(
            html,
            "this is an h1",
        )