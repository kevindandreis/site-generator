import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.XYZ)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_invalid_type(self):
        # Attempt to create a TextNode with an invalid TextType and assert it fails
        with self.assertRaises(ValueError):
            TextNode("This should fail", TextType.XYZ)


if __name__ == "__main__":
    unittest.main()
