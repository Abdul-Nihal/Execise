from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
with open('xml1.xml', 'r') as f:
	data = f.read()
Bs_data = BeautifulSoup(data, "xml")
b_unique = Bs_data.find_all('book')
#print(b_unique)
b_name = Bs_data.find('book', {'id':'bk103'})
#print(b_name)
value = b_name.text
#print(value)
tree = ET.parse('xml1.xml')
root = tree.getroot()
#print(root)
#print(root[1].attrib)
#print(root[3][0].text)
