import xml.etree.ElementTree as ET


class UMLClass:
    def __init__(self, name, documentation, is_root):
        self.name = name
        self.documentation = documentation
        self.is_root = is_root
        self.attributes = []
        self.children = []
        self.multiplicity = None  # min, max


class ModelBuilder:
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.classes = {}
        self.order = []

    def build_model(self):
        tree = ET.parse(self.xml_path)
        root = tree.getroot()

        for elem in root:
            if elem.tag == 'Class':
                name = elem.attrib['name']
                self.order.append(name)
                uml_class = UMLClass(
                    name=name,
                    documentation=elem.attrib.get('documentation', ''),
                    is_root=(elem.attrib.get('isRoot', 'false') == 'true')
                )
                for attr in elem.findall('Attribute'):
                    uml_class.attributes.append((attr.attrib['name'], attr.attrib['type']))
                self.classes[name] = uml_class

        for elem in root:
            if elem.tag == 'Aggregation':
                src = elem.attrib['source']
                tgt = elem.attrib['target']
                mult = elem.attrib['sourceMultiplicity']
                self.classes[tgt].children.append(src)
                self.classes[src].multiplicity = mult

        return self.classes
