import xml.sax

class RecipeHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.name = ""
        self.ingredients = ""
        self.steps = ""
        self.servingSize = ""  

    def startElement(self, name, attrs):
        self.current = name
        if name == "recipe":
            print(f'--Recipe ID: {attrs.get("id", "N/A")}--')

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "ingredients":
            self.ingredients = content
        elif self.current == "steps":
            self.steps = content
        elif self.current == "servingSize":  
            self.servingSize = content

    def endElement(self, name):
        if self.current == "name":
            print(f'Name: {self.name}')
        elif self.current == "ingredients":
            print(f'Ingredients: {self.ingredients}')
        elif self.current == "steps":
            print(f'Steps: {self.steps}')
        elif self.current == "servingSize":  
            print(f'Serving Size: {self.servingSize}')
        
        self.current = ""

parser = xml.sax.make_parser()
handler = RecipeHandler()
parser.setContentHandler(handler)

parser.parse('recipe.xml')
