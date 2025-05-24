from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from parentnode import ParentNode

def main():
    text_node = TextNode("Hello World", TextType.BOLD, "https://www.boot.dev")
    print(text_node)

    html_node = HTMLNode(
        "a", "Click Me", props={"class": "primary", "href": "https://boot.dev"}
    )
    print(html_node)
    print(html_node.props_to_html())

    leaf_node = LeafNode(
        "a", "Click Me", props={"class": "primary", "href": "https://boot.dev"}
    )
    print(leaf_node)
    print(leaf_node.to_html())

    parent_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(parent_node)
    print(parent_node.to_html())

if __name__ == "__main__":
    main()
