import xml.sax 

class XMLHandler(xml.sax.ContentHandler):
  def __init__(self, output_file):
    self.currentTag = ""
    self.buffer = ""
    self.title = ""
    self.output_file = output_file


  def startElement(self, tag, attributes):
    if tag == "TITLE":
      self.currentTag = tag

  def endElement(self, tag):
    if self.currentTag == "TITLE":
      output_file.write(f'<TITLE>{self.buffer}</TITLE>\n')
      

    self.currentTag = ""
    self.buffer = ""

  def characters(self, content):
    if self.currentTag == "TITLE":
      self.buffer += content


if (__name__ == "__main__"):
  output_file = open("titulos.xml", "w")
  parser = xml.sax.make_parser()

  handler = XMLHandler(output_file)
  parser.setContentHandler(handler)
  parser.parse('data/cf79.xml')
