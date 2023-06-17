import random
import numpy as np

# Define a function to create the network file for each row
def create_network_file(lane_length, lane_speeds, setting, save_dir_path, save_name):
    # Iterate over each row
    max_lanes = 4
    lane_speeds = lane_speeds
    veh_speeds = []
    
    # Create the net file string
    net_file = f'''<net xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.16" junctionCornerDetail="5" limitTurnSpeed="5.50" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">
    <location netOffset="0.00,0.00" convBoundary="0.00,0.00,{lane_length},0.00" origBoundary="-10000000000.00,-10000000000.00,10000000000.00,10000000000.00" projParameter="!"/>
    <edge id="E0" from="J0" to="J1" priority="-1">
    '''
    
    # Add the lanes to the net file string
    for i in range(max_lanes):
        # Update the y-coordinate of the lane shape to increase with the lane index
        y = (i-1) * 3.2
        net_file += f'<lane id="E0_{i}" index="{i}" speed="{lane_speeds[i]}" length="{lane_length}" shape="0.00,{y} {lane_length},{y}"/>\n'
    
    # Add the junctions to the net file string
    net_file += f'<junction id="J0" type="dead_end" x="0.00" y="0.00" incLanes="" intLanes="" shape="0.00,0.00 0.00,{max_lanes*3.2}"/>\n'
    net_file += f'<junction id="J1" type="dead_end" x="{lane_length}" y="0.00" incLanes="{" ".join([f"E0_{i}" for i in range(max_lanes)])}" intLanes="" shape="{lane_length},{max_lanes*3.2} {lane_length},0.00"/>\n'
    
    net_file += f'<vehicleTypes>\n'
    if setting == 3:
            net_file += f'<vType id="taxi" accel="0.8" decel="4.5" speedDev="0.2" sigma="0.5" length="3.0" maxSpeed="25.0" guiShape="passenger"/>\n'
            net_file += f'<vType id="emv" vClass="emergency"/>\n'

    elif setting == 2:
            net_file += f'<vType id="taxi" accel="0.8" decel="4.5" sigma="0.5" length="3.0" maxSpeed="25.0" guiShape="passenger"/>\n'
            net_file += f'<vType id="emv" vClass="emergency"/>\n'

    elif setting == 1:
            net_file += f'<vType id="taxi" accel="0.8" decel="4.5" length="3.0" maxSpeed="25.0" guiShape="passenger"/>\n'
            net_file += f'<vType id="emv" vClass="emergency"/>\n'
    elif setting == 5:
            net_file += f'<vType id="taxi" accel="0.8" decel="4.5" sigma="0.5" length="3.0" maxSpeed="25.0" guiShape="passenger"/>\n'
            net_file += f'<vType id="emv" vClass="emergency"/>\n'

    for i in range(250):
        vehicle_name = rf"taxi_v{i}"
        if setting == 3:
            maxSpeed=rf"{random.uniform(5.5556, 16.667)}"
            veh_speeds.append(maxSpeed)
            net_file += f'<vType id="{vehicle_name}" accel="0.8" decel="4.5" speedDev="0.2" sigma="0.5" length="3.0" maxSpeed="{maxSpeed}" guiShape="passenger"/>\n'
        elif setting == 2:
            maxSpeed=rf"{random.uniform(5.5556, 16.667)}"
            veh_speeds.append(maxSpeed)
            net_file += f'<vType id="{vehicle_name}" accel="0.8" decel="4.5" length="3.0" maxSpeed="{maxSpeed}" guiShape="passenger"/>\n'
        elif setting == 1:
            maxSpeed = "16.67"
            net_file += f'<vType id="{vehicle_name}" accel="0.8" decel="4.5" length="3.0" maxSpeed="{maxSpeed}" guiShape="passenger"/>\n'
        elif setting == 5:
            maxSpeed=rf"{random.uniform(5.5556, 16.667)}"
            veh_speeds.append(maxSpeed)
            net_file += f'<vType id="{vehicle_name}" accel="0.8" decel="4.5" length="3.0" maxSpeed="{maxSpeed}" guiShape="passenger"/>\n'

    net_file += f'</vehicleTypes>\n'
    
    # Close the net file string
    net_file += '</edge>\n</net>'
    
    # Write the net file to disk
    with open(f'{save_dir_path}/{save_name}', 'w') as f:
        f.write(net_file)

    return veh_speeds

def generate_random_speeds(num_values):
    speeds = []
    while len(speeds) < num_values:
        mean_speed = 16.67  # m/s
        std_speed = 8.33  # m/s
        lane_speed = random.normalvariate(mean_speed, std_speed)
        if lane_speed >= 8:
            speeds.append(lane_speed)

    return speeds
