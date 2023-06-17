# Import the ElementTree module
import xml.etree.ElementTree as ET

def generate_config(save_config_dir, save_name, net_path, route_path):
    # Create the root element for the XML tree
    configuration = ET.Element("configuration", {
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xsi:noNamespaceSchemaLocation": "http://sumo.dlr.de/xsd/sumoConfiguration.xsd"
    })

    # Add the "input" element to the tree
    input_element = ET.SubElement(configuration, "input")

    # Add the "net-file" and "route-files" elements to the "input" element
    net_file = ET.SubElement(input_element, "net-file", {"value": f"{net_path}"})
    route_files = ET.SubElement(input_element, "route-files", {"value": f"{route_path}"})

    # Write the XML tree to a file
    ET.ElementTree(configuration).write(rf"{save_config_dir}/{save_name}", encoding="UTF-8", xml_declaration=True)

    return rf"{save_config_dir}/{save_name}"
