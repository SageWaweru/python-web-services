# parse an XML file using the xml.sax module
import xml.sax

class PersonHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.name = ""
        self.age = ""
        self.weight = ""
        self.height = ""

    def startElement(self, name, attrs):
        self.current = name
        if name == "person":
            print(f'--Person ID: {attrs["id"]}--')

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print(f'Name: {self.name}')
        elif self.current == "age":
            print(f'Age: {self.age}')
        elif self.current == "weight":
            print(f'Weight: {self.weight}')
        elif self.current == "height":
            print(f'Height: {self.height}')
        
        # Reset the current element after processing
        self.current = ""

# Create an XML parser and set the handler
parser = xml.sax.make_parser()
handler = PersonHandler()
parser.setContentHandler(handler)

# Parse the XML file
parser.parse('people.xml')
