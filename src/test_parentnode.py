import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNodeToHtml(unittest.TestCase):
    def test_with_children(self):
        child_node = LeafNode("span", "child")
        test_obj = ParentNode("div", [child_node])
        self.assertEqual(test_obj.to_html(), "<div><span>child</span></div>")

    def test_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        test_obj = ParentNode("div", [child_node])
        self.assertEqual(
            test_obj.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_children_none(self):
        test_obj = ParentNode("Tag", None)
        with self.assertRaises(ValueError) as cm:
            test_obj.to_html()
        exception = cm.exception
        self.assertEqual(exception.args[0], "Missing children.")

    def test_tag_none(self):
        test_obj = ParentNode(None, [])
        with self.assertRaises(ValueError) as cm:
            test_obj.to_html()
        exception = cm.exception
        self.assertEqual(exception.args[0], "Missing tag.")

    def test_tag_empty(self):
        test_obj = ParentNode("", [])
        with self.assertRaises(ValueError) as cm:
            test_obj.to_html()
        exception = cm.exception
        self.assertEqual(exception.args[0], "Missing tag.")

    def test_children_empty(self):
        test_obj = ParentNode(
            "Tag", [], props={"prop1": "prop-one", "prop2": "prop-two"}
        )
        self.assertEqual(
            test_obj.to_html(), '<Tag prop1="prop-one" prop2="prop-two"></Tag>'
        )

    def test_multiple_and_value_only_children(self):
        span_child = LeafNode("span", "child", {"span-prop": "spanPropValue"})
        value_child = LeafNode(None, "value")
        parent_child = ParentNode(
            "ul",
            [
                LeafNode("li", "list item 1"),
                LeafNode("li", "list item 2"),
                LeafNode("li", "list item 3", {"isLast": "true"}),
            ],
        )
        test_obj = ParentNode("div", [span_child, value_child, parent_child])

        self.assertEqual(
            test_obj.to_html(),
            '<div><span span-prop="spanPropValue">child</span>value<ul><li>list item 1</li><li>list item 2</li><li isLast="true">list item 3</li></ul></div>',
        )


if __name__ == "__main__":
    unittest.main()
