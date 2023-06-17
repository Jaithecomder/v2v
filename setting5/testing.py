# imports
import os
import sys
import traci
from .utilities import *
from .helpers import *
from .hyperparameters import *

def traci_simulation(sumo_cmd, strategy=None, recomputation_interval=10):
    traci.start(sumo_cmd)

    # Get a list of all lanes
    lanes = traci.lane.getIDList()
    # Get a list of all vehicle IDs
    vehicles = traci.vehicle.getIDList()
    
    # Initialize variables to track the departure time of V_1
    v1_departure = None
    v1_arrival = None
    ev_entry_count = False

    # Run the simulation loop
    while traci.simulation.getMinExpectedNumber() > 0:
        # Advance the simulation by one step
        traci.simulationStep()

        # Get a list of all vehicle IDs
        vehicles = traci.vehicle.getIDList()

        # Calculate the utility of each lane and choose the best lane for each vehicle
        for vehicle in vehicles:
            if vehicle == "v_1":
                if v1_departure is None:
                    ev_entry_count = True
                    v1_departure = traci.vehicle.getDeparture(vehicle)
                    print(f"\n\tVehicle {vehicle} entered the simulation at time {v1_departure:.2f}")
                if strategy=="BLS":
                    if traci.simulation.getTime() % recomputation_interval == 0:
                        current_lane = traci.vehicle.getLaneID(vehicle)
                        current_utility = calculate_utility(current_lane, vehicle)
                        best_utility = current_utility
                        best_lane = current_lane
                        for lane in lanes:
                            if lane != current_lane:
                                utility = calculate_utility(lane, vehicle)
                                if utility - current_utility > DELTA and utility > best_utility:
                                    best_utility = utility
                                    best_lane = lane
                        # If the best lane for the vehicle is different from its current lane, change lanes
                        if best_lane != current_lane:
                            best_lane_id = best_lane[-1]  # get the lane ID for the best lane index
                            #request_front_vehicles_to_change_lane(vehicle, CD, best_lane)
                            traci.vehicle.changeLane(vehicle, best_lane_id, duration=0)  # change to the best lane by ID
                        else:
                            best_lane_id = best_lane[-1]
                            #request_front_vehicles_to_change_lane(vehicle, CD, best_lane)
                    
                elif strategy == "FLS":
                    traci.vehicle.setLaneChangeMode(vehicle, 0)
                    if traci.simulation.getTime() % recomputation_interval == 0:
                        current_lane = traci.vehicle.getLaneID(vehicle)
                        #request_front_vehicles_to_change_lane(vehicle, CD, current_lane)

                elif strategy == "SUMO":
                    pass
                
                elif strategy == "ERB":
                    pass

            # Get the lane and speed information for the vehicle
            current_lane = traci.vehicle.getLaneID(vehicle)
            current_speed = traci.vehicle.getSpeed(vehicle)

        # Check if V_1 has left the simulation and record the time
        if ev_entry_count == True:
            if "v_1" not in vehicles and v1_arrival is None:
                v1_arrival = traci.simulation.getTime()
                print(f"\n\tVehicle v_1 left the simulation at time {v1_arrival:.2f}")
                break

        
    # End the simulation and close the TraCI connection
    traci.close()
    sys.stdout.flush()

    return (v1_departure, v1_arrival)

def run_sumo(NET_FILE, ROUTE_FILE, CONFIG_FILE, strategy="BLS"):
    sumo_cmd = ["sumo", 
                "-c", CONFIG_FILE, 
                "-n", NET_FILE, 
                "-r", ROUTE_FILE, 
                "--step-length", str(SIM_STEP),
                "--log", "/home/abhi/Documents/v2v/data_cleaning/log_files/my_log_file.txt",
                "--netstate-dump", "/home/abhi/Documents/v2v/data_cleaning/log_files/nsd.txt",
                "--ignore-route-errors", 
               
            ]
    v1_departure, v1_arrival = traci_simulation(sumo_cmd, strategy=strategy,recomputation_interval=RI) 
    return v1_departure, v1_arrival
