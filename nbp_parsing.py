from lxml import etree as et
import urllib.request as request

url = "https://www.nbp.pl/kursy/xml/en/20a240en.xml"

root = et.parse(request.urlopen(url))
print(et.tostring(root, pretty_print=True).decode())

## print name of currency and current exchange rate
for elem in root.iter("mid-rate"):
    print("{:35} {:20}".format(elem.attrib["currency"], elem.text))
    