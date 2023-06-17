import pandas as pd
import numpy as np
from generate_lanespeeds import *
from generate_network import *
from generate_route import *
from generate_sumoconfig import *
from testing import *


def bucket_simulation(singlerow, save_directory_path, num_iterations, strategy, veh_density_prob):
    group = singlerow['Group'].iloc[0]
    bucket = singlerow['Bucket'].iloc[0]

    each_bucket_lane_speeds = []
    bucket_average = 0
    
    for i in range(num_iterations):
        lane_speeds_df = convert_to_lane_speeds(singlerow, seed=i)
        network_path = create_network_file(lane_speeds_df, save_directory_path)
        route_path = create_route(save_dir_path=save_directory_path, group=group, veh_density_prob=veh_density_prob)
        config_path = generate_config(save_config_dir=save_directory_path,
                                    save_name=rf"{group}_{bucket}config.sumocfg",
                                    net_path=network_path, route_path=route_path)
        print(f"\nITER No. - {i}\n\
              GROUP - {group}\tBUCKET - {bucket}\t\
              LANE_SPEEDS - {lane_speeds_df['LANE_SPEEDS'].iloc[0]}")
        
        ev_departure, ev_arrival = run_sumo(NET_FILE=network_path, ROUTE_FILE=route_path, CONFIG_FILE=config_path,strategy=strategy)
        ev_travel_time = ev_arrival - ev_departure
        print(f"\n\tThe travel time of EV is - {ev_travel_time}")
        each_bucket_lane_speeds.append(ev_travel_time)
    bucket_average = np.mean(each_bucket_lane_speeds)
    print(f"For {group} and {bucket} & applying {strategy} startegy, the bucket average is -- {bucket_average}")
    return bucket_average

def group_simulation(group_data, each_group, save_directory_path, num_iterations, strategy, veh_density_prob):
    grj = 0
    bw_sum = 0
    for i, row in group_data.iterrows():
        row = row.to_frame().T 
        bucket_average = bucket_simulation(row, save_directory_path, num_iterations, strategy, veh_density_prob)
        grj += bucket_average * row['BucketWeights'].iloc[0]
        bw_sum += row['BucketWeights'].iloc[0]
    ev_group_avg = grj/bw_sum
    print(f"For {row['Group'].iloc[0]},with {strategy} the group average is -- {ev_group_avg}")
    return ev_group_avg, grj, bw_sum

def simulation(df, save_directory_path, num_iterations, strategy, veh_density_prob):
    group_names = ['g2', 'g3', 'g4', 'g5']
    ev_group_wise = []
    grj_list = []
    bw_sum_list = []
    for each_group in group_names:
        grouped_data = df.loc[df['Group'] == each_group]
        ev_group_avg , grj, bw_sum = group_simulation(grouped_data, each_group,
                                                       save_directory_path, num_iterations, strategy, veh_density_prob)
        ev_group_wise.append(ev_group_avg)
        grj_list.append(grj)
        bw_sum_list.append(bw_sum)
        
    ev_time = sum(grj_list)/sum(bw_sum_list)
    return ev_time

if __name__  == '__main__':
    df = pd.read_csv("/home/abhi/Documents/v2v/data_cleaning/required_dataframe.csv")
    save_directory_path = rf"/home/abhi/Documents/v2v/data_cleaning/save_dir"
    num_iterations = 1
    strategy = 'SUMO'
    veh_density_prob = 0.75
    ev_time = simulation(df, save_directory_path, num_iterations, strategy, veh_density_prob)
    print(f"Overall, the ev run time is -- {ev_time}  and strategy is {strategy}")