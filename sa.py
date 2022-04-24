from cmath import exp
import dataclasses
from optparse import Values
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
            self.clusters[i] = list(divided_nodes[i])
        print("Initialized {} clusters:".format(self.num_clusters))
        print(self.clusters)
    
    def initialize_node_name_to_cluster_id_dict(self):
        self.node_name_to_cluster_id = dict()
        for cluster_id, nodes in self.clusters.items():
            for node in nodes:
                self.node_name_to_cluster_id[node.name] = cluster_id
        
    def initialize_cut(self):
        self.cut_size = 0
        for cluster in self.clusters.values():
            for node in cluster:
                for neighbor in node.neighbors:
                    if self.node_name_to_cluster_id[node.name] != self.node_name_to_cluster_id[neighbor.name]:
                        self.cut_size = self.cut_size + 1
        self.cut_size = int(self.cut_size/2)
        print("Initial cut size: {}".format(self.cut_size))
    
    def update_temp(self):
        self.current_temp = self.current_temp * (1 - self.temp_rate_update)
        print("Updated temperature to {}/{}".format(self.current_temp, self.final_temp))

    def select_two_nodes(self):
        print("the current configration is", self.clusters.items())
        cluster1, cluster2 = random.sample(range(0, len(self.clusters)), 2)
        print("Selected these ids: {} and {}".format(cluster1, cluster2))
        node_from_cluster1 = random.sample(self.clusters[cluster1], 1)[0]
        node_from_cluster2 = random.sample(self.clusters[cluster2], 1)[0]
        print("Selected these nodes: {} and {}".format(node_from_cluster1, node_from_cluster2))
        return (cluster1, node_from_cluster1), (cluster2, node_from_cluster2)

    def swap(self, node1, node2):
        print("Swapping nodes {} from cluster {} with {} from cluster {}".format(node1[1], node1[0], node2[1], node2[0]))
        self.clusters[node1[0]].remove(node1[1])
        self.clusters[node2[0]].remove(node2[1])
        self.clusters[node1[0]].append(node2[1])
        self.clusters[node2[0]].append(node1[1])

    def update_cut(self, node1, node2):
        self.current_cut_size = self.cut_size
        node1_object = self.clusters[node2[0]][-1]
        print("Selected node neighors", node1_object.neighbors)
        node2_object = self.clusters[node1[0]][-1]
        print("Selected node neighors", node2_object.neighbors)
        for neighbor in node1_object.neighbors:
            if self.node_name_to_cluster_id[neighbor.name] != self.node_name_to_cluster_id[node2_object.name]:
                self.current_cut_size += 1           
        for neighbor in node2_object.neighbors:
            if self.node_name_to_cluster_id[neighbor.name] == self.node_name_to_cluster_id[node1_object.name]:
                self.current_cut_size += 1 
        print("Current cut after moving {} to cluster {} and {} to cluster {} is {}".format(node1[1], node2[0], node2[1], node1[0], self.current_cut_size)) 
        
    def try_to_accept(self):
        self.rondom_num = random.uniform(0 , 1)
        self.delta_cut_size = self.cut_size - self.current_cut_size
        self.Boltzmann_probability = abs(exp(-self.delta_cut_size/ self.current_temp))
        if  self.delta_cut_size < 0 and self.Boltzmann_probability > self.rondom_num :
            print(" The movement is accepted and the curremt cut size is {} and the new configartion is {}".format(self.current_cut_size, self.clusters))
        else:
            self.current_cut_size = self.cut_size
    def run(self):
        self.current_temp = self.initial_temp
        self.initialize_clusters()
        self.initialize_node_name_to_cluster_id_dict()
        self.initialize_cut() 
        while self.current_temp > self.final_temp:
            node1, node2 = self.select_two_nodes()
            self.swap(node1, node2)
            old_cut = self.cut_size
            self.update_cut(node1, node2)
            new_cut = self.current_cut_size
            delta = old_cut - new_cut
            if delta > 0:
                print("Movement is accepted")
            else:
                self.try_to_accept()
            self.update_temp()
        
            
   
        
        