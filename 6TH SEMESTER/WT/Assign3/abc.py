from lxml import etree

xml_file = "employees.xml"
xsd_file = "employees.xsd"

xml_doc = etree.parse(xml_file)
xsd_doc = etree.parse(xsd_file)
xml_schema = etree.XMLSchema(xsd_doc)

if xml_schema.validate(xml_doc):
    print("XML is valid against XSD!")
else:
    print("XML validation failed:", xml_schema.error_log)
