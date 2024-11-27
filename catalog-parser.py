import xml.sax

class CatalogHandler(xml.sax.ContentHandler):
    def __init__(book):
        book.current = ""
        book.title = ""
        book.year = ""
        book.author = ""
        book.genre = ""

    def startElement(book, title, attrs):
        book.current = title
        if title == "person":
            print(f'--Person ID: {attrs["id"]}--')

    def characters(book, content):
        if book.current == "title":
            book.title = content
        elif book.current == "year":
            book.year = content
        elif book.current == "author":
            book.author = content
        elif book.current == "genre":
            book.genre = content

    def endElement(book, title):
        if book.current == "title":
            print(f'title: {book.title}')
        elif book.current == "year":
            print(f'year: {book.year}')
        elif book.current == "author":
            print(f'author: {book.author}')
        elif book.current == "genre":
            print(f'genre: {book.genre}')
        
        book.current = ""

parser = xml.sax.make_parser()
handler = CatalogHandler()
parser.setContentHandler(handler)

parser.parse('catalog.xml')