import xml.sax
pole_katalog=[]

class XMLContextHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.element = None
        self.title = None
        self.artist = None
        self.country = None
        self.company = None
        self.price = None
        self.year = None

    def startElement(self, name, attrs):
        self.element = name

    def endElement(self, name):
        self.element = None
        if name =='CD':
            self.pole_array=[self.title,self.artist,self.country,self.company,self.price,self.year]
            pole_katalog.append(self.pole_array)

    def characters(self, content):
        if self.element == 'TITLE':
            self.title = content
        if self.element == 'ARTIST':
            self.artist = content
        if self.element == 'COUNTRY':
            self.country = content
        if self.element == 'COMPANY':
            self.company = content
        if self.element == 'PRICE':
            self.price = content
        if self.element == 'YEAR':
            self.year = content




f = open("vstup.xml", "r")
xml.sax.parse(f, XMLContextHandler())
f.close()
print pole_katalog
vystup = open("vystup.xml", "w")
x =  xml.sax.saxutils.XMLGenerator(vystup)
attr0 = xml.sax.xmlreader.AttributesImpl({})
x.startDocument()
x.startElement("CATALOG", attr0)

for i in range(len(pole_katalog)):
    x.startElement("CD", attr0)
    for j in range(0,6):
        if(j==0):
            x.startElement("TITLE",attr0)
            x.characters(pole_katalog[i][j])
            x.endElement("TITLE")
        if(j==1):
            x.startElement("ARTIST",attr0)
            x.characters(pole_katalog[i][j])
            x.endElement("ARTIST")
        if(j==2):
            x.startElement("COUNTRY",attr0)
            x.characters(pole_katalog[i][j])
            x.endElement("COUNTRY")
        if(j==3):
            x.startElement("COMPANY",attr0)
            x.characters(pole_katalog[i][j])
            x.endElement("COMPANY")
        if(j==4):
            x.startElement("PRICE",attr0)
            x.characters(pole_katalog[i][j])
            x.endElement("PRICE")
        if(j==5):
            x.startElement("YEAR",attr0)
            x.characters(pole_katalog[i][j])
            x.endElement("YEAR")
    x.endElement("CD")
x.startElement("CD", attr0)
x.startElement("TITLE",attr0)
x.characters("Moje pisnicka")
x.endElement("TITLE")
x.startElement("ARTIST",attr0)
x.characters("Ja")
x.endElement("ARTIST")
x.startElement("COUNTRY",attr0)
x.characters("Ceska republika")
x.endElement("COUNTRY")
x.startElement("COMPANY",attr0)
x.characters("Zator record a.s.")
x.endElement("COMPANY")
x.startElement("PRICE",attr0)
x.characters("1 000 000 Kc")
x.endElement("PRICE")
x.startElement("YEAR",attr0)
x.characters("2063")
x.endElement("YEAR")
x.endElement("CD")

x.endElement("CATALOG")
x.endDocument()