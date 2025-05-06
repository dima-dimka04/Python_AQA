import xml.etree.ElementTree as ET
import xml.dom.minidom as md


def build_xml_node(cls_name, classes):
    cls = classes[cls_name]
    elem = ET.Element(cls.name)
    for name, typ in cls.attributes:
        child = ET.SubElement(elem, name)
        child.text = typ
    for child_cls in cls.children:
        elem.append(build_xml_node(child_cls, classes))
    return elem


def generate_config_xml(classes, filepath):
    root_name = next(cls.name for cls in classes.values() if cls.is_root)
    root_elem = build_xml_node(root_name, classes)
    xml_str = ET.tostring(root_elem, encoding='utf-8')
    pretty = md.parseString(xml_str).toprettyxml(indent="    ")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(pretty)
