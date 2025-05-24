import unittest
from leafnode import LeafNode


class TestLeafNodeToHtml(unittest.TestCase):
    def test_value_error(self):
        test_obj = LeafNode(
            None, None, props={"prop1": "prop-one", "prop2": "prop-two"}
        )
        with self.assertRaises(ValueError):
            test_obj.to_html()

    def test_tag_none(self):
        test_obj = LeafNode(
            None, "TagValue", props={"prop1": "prop-one", "prop2": "prop-two"}
        )
        self.assertEqual(test_obj.to_html(), "TagValue")

    def test_tag_empty(self):
        test_obj = LeafNode(
            None, "TagValue", props={"prop1": "prop-one", "prop2": "prop-two"}
        )
        self.assertEqual(test_obj.to_html(), "TagValue")

    def test_tag_present(self):
        test_obj = LeafNode(
            "Tag", "TagValue", props={"prop1": "prop-one", "prop2": "prop-two"}
        )
        self.assertEqual(
            test_obj.to_html(), '<Tag prop1="prop-one" prop2="prop-two">TagValue</Tag>'
        )

    def test_no_props(self):
        test_obj = LeafNode("Tag", "TagValue")
        
        self.assertEqual(test_obj.to_html(), "<Tag>TagValue</Tag>")

if __name__ == "__main__":
    unittest.main()
