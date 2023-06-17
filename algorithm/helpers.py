import traci

# Define log function to print traci output
def log(msg):
    print("[LOG] " + str(msg))

# Get minimum and average speeds of vehicles within communication distance CD
def get_speeds_within_cd(vehicle,lane,CD):
    """
    Get the minimum and average speeds of all vehicles within a certain communication range of the current vehicle.
    """
    # Get the position of the current vehicle
    vehicle_pos = traci.vehicle.getPosition(vehicle)

    # Get a list of nearby vehicles within the communication range
    nearby_vehicles = get_vehicles_ahead(vehicle,lane,CD)
    
    # Calculate the speeds of nearby vehicles
    speeds = [v['speed'] for v in nearby_vehicles if v['distance'] <= CD and v['position'][0] > vehicle_pos[0] and v['speed'] >= 0]

    # Calculate the minimum and average speeds
    if len(speeds) > 0:
        min_speed = min(speeds)
        avg_speed = sum(speeds) / len(speeds)
    else:
        min_speed = 0
        avg_speed = 0

    return min_speed, avg_speed

def get_vehicles_ahead(vehicle_id, lane_id, CD):
    """
    Get a list of vehicles ahead of the given vehicle ID within the specified distance on the given lane.
    Returns a list of dictionaries with keys "id", "distance", "lane_id", "position", and "speed".
    """
    # Get the position of the given vehicle
    vehicle_pos = traci.vehicle.getPosition(vehicle_id)
    
    # Get a list of all vehicles on the same lane
    lane_vehicles = traci.lane.getLastStepVehicleIDs(lane_id)
    
    # Get the details for each nearby vehicle on the given lane
    nearby_vehicles = []
    for v in lane_vehicles:
        # Get the lane and position of the nearby vehicle
        v_lane_id = traci.vehicle.getLaneID(v)
        v_pos = traci.vehicle.getPosition(v)
        
        # Calculate the distance between the vehicles
        distance_to_v = traci.simulation.getDistance2D(vehicle_pos[0], vehicle_pos[1], v_pos[0], v_pos[1])
        #distance_to_v = traci.simulation.getDistance2D(0, vehicle_pos[1], 0, v_pos[1])
        
        # If the vehicle is within the specified distance and on the same lane, add it to the list
        if distance_to_v <= CD and v_lane_id == lane_id:
            v_speed = traci.vehicle.getSpeed(v)
            v_details = {
                "ref_vehicle": vehicle_id,
                "id": v,
                "distance": distance_to_v,
                "lane_id": v_lane_id,
                "position": v_pos,
                "speed": v_speed
            }
            nearby_vehicles.append(v_details)
    return nearby_vehicles
