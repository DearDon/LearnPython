from lxml import etree as ElementTree

parser = ElementTree.XMLParser(remove_blank_text=True)
xmlf='session.xml'
#xmlr = ElementTree.parse(xmlf,parser).getroot() #the same as following
xmlr = ElementTree.parse(xmlf,parser)

#reticle=xmlr.find('reticle'.)

#description=xmlr.find('description').text.strip()
descriptions=xmlr.findall('description')
for d in descriptions:
    print d.text
#print description[0]
