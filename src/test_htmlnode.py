import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("a", "abcdefg", None, {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertNotEqual(node.tag, "p")

    def test_value(self):
        node = HTMLNode("p", "abcdefg", None, {"href": "https://www.google.com"})
        self.assertEqual(node.value, "abcdefg")
        self.assertNotEqual(node.value, "pasdasd")

    def test_children(self):
        child1 = HTMLNode("span", "Child 1", None, {"class": "child"})
        child2 = HTMLNode("a", "Child 2", None, {"href": "https://example.com"})
        child3 = HTMLNode("div", "Child 3", None, {"id": "child3"})
        child4 = HTMLNode("span", "Child 4", None, {"style": "color:red;"})

        node = HTMLNode("p", "abcdefg", [child1, child2], {"href": "https://www.google.com"})

        self.assertEqual(node.children, [child1, child2])
        self.assertNotEqual(node.children, [child3, child4])

    def test_props(self):
        node = HTMLNode("p", "abcdefg", None, {"href": "https://www.boot.dev"})
        self.assertIn("href", node.props)
        self.assertEqual(node.props["href"], "https://www.boot.dev")
        self.assertNotIn("target", node.props)

    def test_props_to_html(self):
        node = HTMLNode("p", None, None, {"class": "header", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="header" id="main"')
        
        node_no_props = HTMLNode("p", "Hello, World!", None, None)
        self.assertEqual(node_no_props.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("div", "Test", None, {"class": "container"})
        repr_output = repr(node)   
        self.assertEqual(repr_output, "HTMLNode(div, Test, None, {'class': 'container'})")

if __name__ == "__main__":
    unittest.main()