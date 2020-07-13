import os
from xml.etree import ElementTree


input_file = 'cf79.xml'
fullfile = os.path.abspath(os.path.join('data', input_file))

output_file = open("autores.xml", "w")

dom = ElementTree.parse(fullfile)
records = dom.findall('RECORD')

for record in records:
  authors = record.find('AUTHORS')
  if authors is not None:
    for author in authors:
      output_file.write(f'{ElementTree.tostring(author, encoding="unicode")} \n')