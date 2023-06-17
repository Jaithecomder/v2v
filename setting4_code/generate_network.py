# Define a function to create the network file for each row
def create_network_file(data, save_dir_path):
    # Iterate over each row
    for index, row in data.iterrows():
        # Extract the relevant values from the row
        group = row['Group']
        bucket = row['Bucket']
        max_lanes = row['MAX_LANES']
        lane_speeds = row['LANE_SPEEDS']
        AvgRoadSpeed = row['AvgRoadSpeed']
        
        # Create the net file string
        net_file = f'''<net xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.16" junctionCornerDetail="5" limitTurnSpeed="5.50" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">
        <location netOffset="0.00,0.00" convBoundary="0.00,0.00,2000.00,0.00" origBoundary="-10000000000.00,-10000000000.00,10000000000.00,10000000000.00" projParameter="!"/>
        <edge id="E0" from="J0" to="J1" priority="-1">
        '''
        
        # Add the lanes to the net file string
        for i in range(max_lanes):
            # Update the y-coordinate of the lane shape to increase with the lane index
            y = (i-1) * 3.2
            net_file += f'<lane id="E0_{i}" index="{i}" speed="{lane_speeds[i]}" length="2000.00" shape="0.00,{y} 2000.00,{y}"/>\n'
        
        # Add the junctions to the net file string
        net_file += f'<junction id="J0" type="dead_end" x="0.00" y="0.00" incLanes="" intLanes="" shape="0.00,0.00 0.00,{max_lanes*3.2}"/>\n'
        net_file += f'<junction id="J1" type="dead_end" x="2000.00" y="0.00" incLanes="{" ".join([f"E0_{i}" for i in range(max_lanes)])}" intLanes="" shape="2000.00,{max_lanes*3.2} 2000.00,0.00"/>\n'
        
        net_file += f'<vehicleTypes>'
        net_file += f'<vType id="taxi" accel="0.8" decel="4.5" speedDev="0.2" sigma="0.5" length="3.0" maxSpeed="25.0" guiShape="bicycle"/>'
        net_file += f'<vType id="emv" accel="0.8" decel="4.5" speedDev="0.2" sigma="0.5" length="3.0" maxSpeed="25.0" guiShape="passenger"/>'
        net_file += f'</vehicleTypes>'
        
        # Close the net file string
        net_file += '</edge>\n</net>'
        
        # Write the net file to disk
        with open(f'{save_dir_path}/{group}_{bucket}.net.xml', 'w') as f:
            f.write(net_file)

    return f'{save_dir_path}/{group}_{bucket}.net.xml'