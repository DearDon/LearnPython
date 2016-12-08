#########################################################################
# File Name: test_xml.py
# Purpose:
#	This file is to learn play with xml
# History:
#	Created Time: 2016-12-08
# Author: Don E-mail: dpdeng@whu.edu.cn
#########################################################################
from lxml import etree

def test():
    nsmap=root.nsmap
    print(nsmap)

    reticle=xmltree.find('reticle/reticle_id')
    print(reticle.text)

    description=xmltree.find('description').text.strip()
    descriptions=xmltree.findall('description')
    for d in descriptions:
        print d.text
    print description[0]

def diffAllNode(node1,node2):#two file need same format and order
    if len(node1)!=0:
        for i in range(len(node1)):
            diffAllNode(node1[i],node2[i])
    else:
        if node1.text != node2.text:
            print("{} is not equal to {}".format(node1.text, node2.text))
            # print(node1.text, node2.text)

def getAllPath(node,ppath,allpath):
    if node.getparent() is not None:
        new_ppath="/".join([ppath, node.tag])
    else:
        new_ppath=""
    if len(node)!=0:
        for subnode in node:
            getAllPath(subnode,new_ppath,allpath)
    else:
        # print("{}/{}".format(ppath, node.tag))
        allpath.append(new_ppath)

def testRevise(xmltree):
    root=xmltree.getroot()
    etree.SubElement(root, "Don1")

    don=xmltree.find('Don1')
    don.text="testwt"
    if len(don):
        print don
    else:
        print "no element for don"
    fileHandler = open("./test.xml", "wb")
    xmltree.write(fileHandler, encoding="utf-8", xml_declaration=True, pretty_print=True)
    fileHandler.close()

if __name__ == '__main__':
    parser = etree.XMLParser(remove_blank_text=True)
    xmlf='session.xml'
    xmlf1='test.xml'
    xmltree = etree.parse(xmlf,parser)
    xmltree1 = etree.parse(xmlf1,parser)
    root=xmltree.getroot()
    root1=xmltree1.getroot()

    if 0:
        diffAllNode(root,root1)

    if 1:
        allpath=[]
        getAllPath(root,'',allpath)
        # print(allpath)
        for path in allpath:
            node=xmltree.find(path)
            print(path, node.text)

