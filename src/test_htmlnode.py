import unittest
from htmlnode import HTMLNode


class TestHTMLNodePropsToHtml(unittest.TestCase):
    def test_props_present(self):
        test_obj = HTMLNode(props={"prop1": "prop-one", "prop2": "prop-two"})
        expected_props_str = ' prop1="prop-one" prop2=\"prop-two\"'
        self.assertEqual(test_obj.props_to_html(), expected_props_str)
    
    def test_props_none(self):
        test_obj = HTMLNode()
        expected_props_str = ''
        self.assertEqual(test_obj.props_to_html(), expected_props_str)
    
    def test_props_empty(self):
        test_obj = HTMLNode(props = {}) 
        expected_props_str = ''
        self.assertEqual(test_obj.props_to_html(), expected_props_str)
        

if __name__ == "__main__":
    unittest.main()
