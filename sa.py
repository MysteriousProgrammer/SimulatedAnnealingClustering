import dataclasses
import graph
import random
from typing import List

# Taken from this answer: https://stackoverflow.com/a/2135920
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

@dataclasses.dataclass
class SA:
    nodes: List[graph.Node]
    num_clusters: int
    initial_temp: int
    final_temp: int
    temp_rate_update: float
    iters_per_temp: int
    current_temp: int = 0

    def initialize_clusters(self):
        self.clusters = {}
        divided_nodes = list(split(self.nodes, self.num_clusters))
        for i in range(self.num_clusters):
            self.clusters[i] = set(list(divided_nodes[i]))
        print("Initialized {} clusters:".format(self.num_clusters))
        print(self.clusters)
        
    def initialize_cut(self):
        cut_size = 0
        node_name_to_cluster_id = dict()
        for cluster_id, nodes in self.clusters.items():
            for node in nodes:
                node_name_to_cluster_id[node.name] = cluster_id

        for cluster in self.clusters.values():
            for node in cluster:
                for neighbor in node.neighbors:
                    if node_name_to_cluster_id[node.name] != node_name_to_cluster_id[neighbor.name]:
                        cut_size = cut_size + 1
        cut_size = int(cut_size/2)
        print("Initial cut size: {}".format(cut_size))
        
    def try_to_accept(self):
        return 
    
    def update_temp(self):
        self.current_temp = self.current_temp * (1 - self.temp_rate_update)
        print("Updated temperature to {}/{}".format(self.current_temp, self.final_temp))

    def random_move(self):
        cluster1, cluster2 = random.sample(range(0, len(self.clusters)), 2)
        print("Selected these ids: {} and {}".format(cluster1, cluster2))

        # TO-DO: Select one node from each cluster
        node_from_cluster1 = '???'
        node_from_cluster2 = '???'
        print("Selected these nodes: {} and {}".format(node_from_cluster1, node_from_cluster2))
        return
    
    def cal_cost_delt(self):
        return 0

    def update_cut(self):
        return
    
    def run(self):
        self.current_temp = self.initial_temp
        self.initialize_clusters()
        self.initialize_cut() 
        while self.current_temp > self.final_temp:
            self.random_move()
            self.cal_cost_delt()
            if self.cal_cost_delt() > 0:
                print("Movement is accepted")
            else:
                self.try_to_accept()
            self.update_cut()
            self.update_temp()
        
            
   
        
        