#!/bin/python3
import argparse
import sa
import test

def main():
    parser = argparse.ArgumentParser(description='Simulated Annealing for Node Clustering.')
    parser.add_argument('-number_of_clusters', 
                        type=int,
                        default=3,
                        help='the number of clusters that should be generated')
    parser.add_argument('-initial_temperature', 
                        type=int,
                        default=10000,
                        help='the initial temperature for simulated annealing')
    parser.add_argument('-final_temperature', 
                        type=int, 
                        default=10,
                        help='the temperature that, when reached, finishes the algorithm')
    parser.add_argument('-temperature_change', 
                        type=float,
                        default=0.05,
                        help='update rate for the temperature')
    parser.add_argument('-iterations_per_temperature', 
                        type=int, 
                        default=1,
                        help='the number of random movements between two temperature changes')

    args = parser.parse_args()
    check_arguments(args)
    print_args(args)
    runner = sa.SA(test.get_test_graph(),
                    args.number_of_clusters,
                    args.initial_temperature,
                    args.final_temperature,
                    args.temperature_change,
                    args.iterations_per_temperature)
    runner.run()
    
def check_arguments(args):
    if args.initial_temperature <= 0:
        print("Error: initial temperature must be positive.")
        exit()
    if args.initial_temperature < args.final_temperature:
        print("Error: initial temperature is less than final temperature.")
        exit()
    if args.temperature_change >= 1.0 or args.temperature_change <= 0:
        print("Error: temperature change must be between 0 and 1.0 exclusive.")
        exit()
    if args.iterations_per_temperature <= 0:
        print("Error: iterations per temperature must be positive")
        exit()
    if args.number_of_clusters <= 1:
        print("Error: number of clusters must be more than 1")
        exit()

def print_args(args):
    print("Running SA-Clustering.\nNumber of clusters: {}\nInitial temp: {}\nFinal temp: {}\nTemp update factor: {}\nIterations per update: {}\n"
            .format(args.number_of_clusters, 
            args.initial_temperature, 
            args.final_temperature, 
            args.temperature_change, 
            args.iterations_per_temperature))


if __name__ == "__main__":
    main()
