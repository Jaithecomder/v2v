import random

def create_route(save_dir_path, save_name, veh_density_prob, setting, veh_speeds):
    
    # Create the root element for the XML tree
    route_file = f'''<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">\n'''
    
    # Add the "route" element to the tree
    route_file += f'''\t<route id="r_0" edges="E0" />\n'''
    prob = veh_density_prob
    # Add the "flow" and "vehicle" elements to the tree/home/abhi/Documents/v2v/data_cleaning
    numbers = [0, 1, 2, 3]
    counts = [0] * len(numbers)
    high_counts = [0, 0]
    low_counts = [0, 0]
    for i in range(250): 
        if i != 200:
            vehicle_name = rf"taxi_v{i}"

            # Calculate the weight for each number based on the counts
            weights = [1 / (count + 1) for count in counts]     
                                                
            # Randomly select a number based on the weights
            random_number = random.choices(numbers, weights)[0]            
            # Increment the count for the selected number
            counts[random_number] += 1
            if setting == 1:
                route_file += f'''\t<flow id="{vehicle_name}" type="{vehicle_name}" begin="{i}.00" end="{i+1}.00" departSpeed="avg" departLane="{random_number}" color="cyan" route="r_0" probability="{prob}"/>\n'''
            else:
                veh_speed = veh_speeds[i]
                if float(veh_speed) > 12.11:
                    hnumbers = [0, 1]
                    # Calculate the weight for each number based on the counts
                    hweights = [1 / (count + 1) for count in high_counts]
                    # Randomly select a number based on the weights
                    random_number = random.choices(hnumbers, hweights)[0]            
                    # Increment the count for the selected number
                    high_counts[random_number] += 1

                    route_file += f'''\t<flow id="{vehicle_name}" type="{vehicle_name}" begin="{i}.00" end="{i+1}.00" departSpeed="avg" departLane="{random_number}" color="cyan" route="r_0" probability="{prob}"/>\n'''
                else:
                    lnumbers = [2, 3]
                    random_number = random.choice(lnumbers)
                    route_file += f'''\t<flow id="{vehicle_name}" type="{vehicle_name}" begin="{i}.00" end="{i+1}.00" departSpeed="avg" departLane="{random_number}" color="cyan" route="r_0" probability="{prob}"/>\n'''
        else:
            route_file += f'''\t<vehicle id="v_1" type="emv" depart="200.00" departSpeed="max" departLane="0" color="red" route="r_0"/>\n'''
    route_file += f'''</routes>'''
  
    # Write the net file to disk
    with open(f'{save_dir_path}/{save_name}', 'w') as f:
        f.write(route_file)
