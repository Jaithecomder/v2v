# Define simulation parameters
SIM_STEP = 1                    # Time step of the simulation in seconds
last_considered_vehicle = 250   # Duration at which last vehicle generated 

# Define V2V communication parameters
CD = 100        # communication distance in meters
WA = 0.4        # weight for lowest speed
WB = 0.4        # weight for average speed
WC = 0.2        # weight for number of vehicles
DELTA = 0.1  # minimum utility difference for lane change
DURATION = 5    # OTHER VEHICLES LANE CHANGE DURATION
EV_DURATION = 5 # EV LANE CHANGE DURATION
RI = 10         # recomputation interval
INTRODUCE_STOP =  False
HOW_MANY_VEHICLES_TO_STOP =  5  #[1, 3, 5]
STOP_VEHICLE_TIME         =  10   # [5, 10, 20, 40, 60, 80, 100, 120]

IF_SAME_LANE = True    # For FLS SLOWING VEHICLES -- True for the fastest lane
FASTEST_LANE_ID = "E0_0"     # For FLS SLOWING VEHICLES
