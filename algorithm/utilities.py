import time
import traci
import random
from .helpers import *
from .hyperparameters import *


# Define function to calculate lane utility
def calculate_utility(lane, vehicle):
    start_time = time.time()  # Start measuring time
    # Get lane statistics
    min_speed, avg_speed = get_speeds_within_cd(vehicle, lane, CD)
    # Calculate maximum speed limit for lane
    max_speed = traci.lane.getMaxSpeed(lane)
    
    # Calculate the number of vehicles within communication distance ahead of the given vehicle
    mv = traci.vehicle.getMinGap(vehicle)
    lv = traci.vehicle.getLength(vehicle)
    max_num_vehicles = int(CD / (mv + lv))
    #print(max_num_vehicles)
    pos = traci.vehicle.getPosition(vehicle)
    num_vehicles = 0

    for veh_id in traci.lane.getLastStepVehicleIDs(lane):
        veh_pos = traci.vehicle.getPosition(veh_id)
        veh_dist = veh_pos[0] - pos[0] - lv
        #print(veh_dist)
        if veh_dist > 0 and veh_dist <= CD:
                num_vehicles += 1
    # Calculate lane utility
    utility = WA * (min_speed / max_speed) + WB * (avg_speed / max_speed) + WC * ((max_num_vehicles - num_vehicles) / max_num_vehicles)

    end_time = time.time()  # Stop measuring time
    total_time = end_time - start_time
    #print(f"calculate_utility time taken: {total_time:.6f} seconds")
    
    return utility

def request_front_vehicles_to_change_lane(ev, CD, best_lane_id):
    ev_lane_id = traci.vehicle.getLaneID(ev)       
    lv = traci.vehicle.getLength(ev)  
    pos = traci.vehicle.getPosition(ev)
    
    for veh_id in traci.lane.getLastStepVehicleIDs(best_lane_id):
        veh_pos = traci.vehicle.getPosition(veh_id)
        veh_dist = veh_pos[0] - pos[0] - lv
        veh_dist = (lambda x: x if x > 0 else CD * 2)(veh_pos[0] - pos[0] - lv)
        if veh_dist <= CD:
            traci.vehicle.changeLaneRelative(veh_id, 1, duration=DURATION) # 1 - right ==> GOES UP, -1 left ==> GOES DOWN
        else:
            continue


def stopping_vehicles(strategy, same_lane=IF_SAME_LANE, how_many_vehicles_to_stop=HOW_MANY_VEHICLES_TO_STOP):
    vehicle_ids = traci.vehicle.getIDList()

    if strategy != 'FLS':
        if "v_1" in vehicle_ids:
            vehicle_ids = list(vehicle_ids)
            vehicle_ids.remove("v_1")
            vehicle_ids = tuple(vehicle_ids)
        # Select a random subset of vehicles to stop
        vehicles_to_stop = random.choices(vehicle_ids, k=min(how_many_vehicles_to_stop, len(vehicle_ids)))
    else:
        # Get the vehicle IDs in the specified lane
        fastest_lane_id = FASTEST_LANE_ID
        fastest_lane_veh_ids = traci.lane.getLastStepVehicleIDs(fastest_lane_id)
        if same_lane:
            if "v_1" in vehicle_ids:
                fastest_lane_veh_ids = list(fastest_lane_veh_ids)
                fastest_lane_veh_ids.remove("v_1")
                fastest_lane_veh_ids = tuple(fastest_lane_veh_ids)
            vehicles_to_stop = random.choices(fastest_lane_veh_ids, k=min(how_many_vehicles_to_stop, len(fastest_lane_veh_ids)))
        else:
            oth_veh_ids = list(vehicle_ids)
            oth_veh_ids = list(filter(lambda x: x not in fastest_lane_veh_ids, oth_veh_ids))
            oth_veh_ids = tuple(oth_veh_ids)
            vehicles_to_stop = random.choices(oth_veh_ids, k=min(how_many_vehicles_to_stop, len(oth_veh_ids)))

    # Set the speed of selected vehicles to zero
    for vehicle_id in vehicles_to_stop:
        if vehicle_id in vehicle_ids:
            traci.vehicle.setSpeed(vehicle_id, 2.8)
        else:
            print(f"Invalid vehicle ID: {vehicle_id}")

                
def lane_probability(lane, vehicle):
    # Get lane statistics
    min_speed, avg_speed = get_speeds_within_cd(vehicle, lane, CD)
    # Calculate maximum speed limit for lane
    max_speed = traci.lane.getMaxSpeed(lane)
    
    # Calculate the number of vehicles within communication distance ahead of the given vehicle
    mv = traci.vehicle.getMinGap(vehicle)
    lv = traci.vehicle.getLength(vehicle)
    max_num_vehicles = int(CD / (mv + lv))

    pos = traci.vehicle.getPosition(vehicle)
    num_vehicles = 0

    for veh_id in traci.lane.getLastStepVehicleIDs(lane):
        veh_pos = traci.vehicle.getPosition(veh_id)
        veh_dist = veh_pos[0] - pos[0] - lv
        #print(veh_dist)
        if veh_dist > 0 and veh_dist <= CD:
                num_vehicles += 1

    # Calculate lane utility
    utility = WA * (min_speed / max_speed) + WB * (avg_speed / max_speed) + WC * ((max_num_vehicles - num_vehicles) / max_num_vehicles)
