import random

# Function to convert a string of comma-separated floats to a list of floats
def string_to_float_list(s):
    return [float(x) for x in s.split(',')]

def convert_to_lane_speeds(speeds_df, seed):
    # Set the random seed
    random.seed(seed)

    # Copy the speeds dataframe to avoid modifying the original
    lane_speeds_df = speeds_df.copy()

    # Iterate through each row of the dataframe
    for i, row in lane_speeds_df.iterrows():
        # Get the average speed for the road
        avg_speed = row['Bavgs']

        # Generate a random max speed for each lane
        lane_speeds = []
        for j in range(row['MAX_LANES']):
            limits = 0.4 * avg_speed
            max_speed = round(random.uniform(max(avg_speed - limits, 0), avg_speed + limits), 2)
            lane_speeds.append(max_speed)

        lane_speeds.sort()
        # Update the lane speeds for the row
        lane_speeds_df.at[i, 'LANE_SPEEDS'] = ','.join(map(str, lane_speeds))
        # string to float
    
    lane_speeds_df['LANE_SPEEDS'] = lane_speeds_df['LANE_SPEEDS'].apply(string_to_float_list)

    return lane_speeds_df