# Import the ElementTree module
import xml.etree.ElementTree as ET

def create_route(save_dir_path, group, veh_density_prob):
    
    # Create the root element for the XML tree
    routes = ET.Element("routes", {
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xsi:noNamespaceSchemaLocation": "http://sumo.dlr.de/xsd/routes_file.xsd"
    })

    # Add the "route" element to the tree
    route = ET.SubElement(routes, "route", {"id": "r_0", "edges": "E0"})
    prob = veh_density_prob
    # Add the "flow" and "vehicle" elements to the tree
    for i in range(int(group[-1])-1):
        flow = ET.SubElement(routes, "flow", {
            "id": rf"f_{i}",
            "type": "taxi",
            "begin": "0.00",
            "departLane": rf"{i}",
            "route": "r_0",
            "probability": rf"{prob}"
        })
    vehicle1 = ET.SubElement(routes, "vehicle", {
        "id": "v_0",
        "type": "taxi",
        "depart": "0.00",
        "departLane": "0",
        "color": "cyan",
        "route": "r_0"
    })
    vehicle2 = ET.SubElement(routes, "vehicle", {
        "id": "v_1",
        "type": "emv",
        "depart": "200.00",
        "departLane": rf"{int(group[-1])-1}",
        "color": "red",
        "route": "r_0"
    })

    # Write the XML tree to a file
    ET.ElementTree(routes).write(f"{save_dir_path}/route.rou.xml", encoding="UTF-8", xml_declaration=True)

    return f"{save_dir_path}/route.rou.xml"
