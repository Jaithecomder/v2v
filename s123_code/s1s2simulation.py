import sys
import random
import argparse
import statistics

sys.path.append('/home/abhi/Documents/v2v/data_cleaning')
from algorithm.testing import *
from s123_gennet import *
from s123_genroute import *

def main(strategy, setting, veh_density_prob, num_runs, lane_length, fix_same_random_seed):
    ev_travel_time_list = []
    avg_ev_travel_time = None

    for i in range(num_runs):
        seed_value = random.randint(1, 1000)  # Generate a random seed value
        if fix_same_random_seed:
            j=i*i
            random.seed(j)  # Set the seed for each iteration
            print(f"\nIter no. {i} & seed is {j}")
        else:
            random.seed(seed_value)  # Set the seed for each iteration
            print(f"\nIter no. {i} & seed is {seed_value}")
        
        lane_speeds = []
        net_rou_save_dir_path = rf'/home/abhi/Documents/v2v/data_cleaning/setting{setting}'
        network_save_name = rf's{setting}net.net.xml'
        route_save_name = rf"s{setting}rou.rou.xml"

        if setting == 3:
            lane_speeds = generate_random_speeds(4)
            lane_speeds.sort(reverse=True)
        else:
            lane_speeds = [16.667, 16.667, 16.667, 16.667]

        veh_speeds = create_network_file(lane_length, lane_speeds, setting, net_rou_save_dir_path, network_save_name)

        if strategy == "ERB":
            route_path = rf'/home/abhi/Documents/v2v/data_cleaning/setting{setting}/s{setting}erbrou.rou.xml'
            config_path = rf'/home/abhi/Documents/v2v/data_cleaning/setting{setting}/s{setting}erbconfig.sumocfg'
            
        else:
            create_route(net_rou_save_dir_path, route_save_name, veh_density_prob, setting, veh_speeds)
            route_path = rf'/home/abhi/Documents/v2v/data_cleaning/setting{setting}/s{setting}rou.rou.xml'
            config_path = rf'/home/abhi/Documents/v2v/data_cleaning/setting{setting}/s{setting}config.sumocfg'
        network_path = rf'/home/abhi/Documents/v2v/data_cleaning/setting{setting}/s{setting}net.net.xml'

        ev_departure, ev_arrival = run_sumo(NET_FILE=network_path, ROUTE_FILE=route_path, CONFIG_FILE=config_path, strategy=strategy, setting=setting)
        ev_travel_time = ev_arrival - ev_departure
        ev_travel_time_list.append(ev_travel_time)
        print("\t", ev_travel_time)
            
    avg_ev_travel_time = statistics.mean(ev_travel_time_list)
    
    print(f"\n\tThe travel times of EV in the {i+1} runs are - {ev_travel_time_list} \n\t \
        The strategy is {strategy}\n\t\
        The average EV run time is - {avg_ev_travel_time}\
        ")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pass arguments through command line.')
    parser.add_argument('-s', '--strategy', type=str, help='Strategy: FLS, SUMO, BLS, ERB', default='ERB')
    parser.add_argument('-st', '--setting', type=int, help='Setting value', default=3)
    parser.add_argument('-vdp', '--veh_density_prob', type=str, help='Vehicle density probability', default='0.60')
    parser.add_argument('-runs', '--num_runs', type=int, help='Num of runs U have to average for', default=10)
    parser.add_argument('-len', '--lane_length', type=float, help='Give stretch of the road in metres', default=2000.00)
    parser.add_argument('-same_seed', '--fix_same_random_seed', type=bool,
                        help='if to fix the same seed for different strategies', default=True)
    args = parser.parse_args()

    main(args.strategy, args.setting, args.veh_density_prob, args.num_runs, args.lane_length, args.fix_same_random_seed)

