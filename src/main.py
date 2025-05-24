from htmlnode import HTMLNode
from textnode import TextNode, TextType

def main():
    text_node = TextNode("Hello World", TextType.BOLD, "https://www.boot.dev")
    print(text_node)
    html_node = HTMLNode("a", "Click Me", props = {"class": "primary", "href": "https://boot.dev"})
    print(html_node)
    print(html_node.props_to_html())
  
if __name__ == "__main__":
    main()
