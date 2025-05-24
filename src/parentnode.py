from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] = None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Missing tag.")
        if self.children == None:
            raise ValueError("Missing children.")
        
        result = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
