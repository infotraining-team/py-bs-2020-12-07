from lxml import etree as et

## creation
root = et.Element("root")
root.append(et.Element("child"))
child2 = et.SubElement(root, "child2")
root[0].attrib['company'] = "Hitachi"
root[1].attrib['company'] = "ABB"
root[0].attrib['value'] = "123421342"
root[1].attrib['value'] = "234234342"
root[0].append(et.Element("subchild"))
root[1].text = "Leszek"
root[0][0].attrib['people'] = "Someone"

print(et.tostring(root, pretty_print=True).decode())

## browse it
for elem in root.iter():    
    print(elem.tag, " -> ", elem.attrib, " -> ", elem.text)
