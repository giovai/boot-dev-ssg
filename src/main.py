from textnode import TextNode, TextType

def main():
    text_node = TextNode("Hello World", TextType.BOLD, "https://www.boot.dev")
    print(text_node)
    
main()