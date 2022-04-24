from cmath import exp
import dataclasses
import graph
import random
from typing import List
import matplotlib.pyplot as plt

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
        self.current_cut_size = 0
        for cluster in self.clusters.values():
            for node in cluster:
                for neighbor in node.neighbors:
                    if self.node_name_to_cluster_id[node.name] != self.node_name_to_cluster_id[neighbor.name]:
                        self.current_cut_size = self.current_cut_size + 1
        self.current_cut_size = int(self.current_cut_size/2)
        
    def update_temp(self):
        self.current_temp = self.current_temp * (1 - self.temp_rate_update)
        self.temperature_history.append(self.current_temp)
        print("Updated temperature to {} out of final {}".format(self.current_temp, self.final_temp))

    def select_two_nodes(self):
        cluster1, cluster2 = random.sample(range(0, len(self.clusters)), 2)
        node_from_cluster1 = random.sample(self.clusters[cluster1], 1)[0]
        node_from_cluster2 = random.sample(self.clusters[cluster2], 1)[0]
        return (cluster1, node_from_cluster1), (cluster2, node_from_cluster2)

    def swap(self, node1, node2):
        self.clusters[node1[0]].remove(node1[1])
        self.clusters[node2[0]].remove(node2[1])
        self.clusters[node1[0]].append(node2[1])
        self.clusters[node2[0]].append(node1[1])

        self.node_name_to_cluster_id[node1[1].name] = node2[0]
        self.node_name_to_cluster_id[node2[1].name] = node1[0]

    def try_to_accept(self, delta):
        probability_of_accepting = abs(exp((-delta/(self.current_temp/100))))
        random_number = random.uniform(0.0, 1.0)
        if random_number < probability_of_accepting:
            return True
        else:
            return False

    def update_best_solution(self):
        self.best_cut = self.current_cut_size
        self.best_solution = self.clusters.copy()
        #print("New best solution of cut {} found: {}".format(self.best_cut, self.best_solution))

    def run(self):
        self.temperature_history = [self.initial_temp]
        self.current_temp = self.initial_temp
        self.initialize_clusters()
        self.initialize_node_name_to_cluster_id_dict()
        self.initialize_cut()
        self.best_cut = self.current_cut_size
        self.best_solution = self.clusters.copy()
        self.cut_history = [self.best_cut]
        while self.current_temp > self.final_temp:
            for _ in range(self.iters_per_temp):
                node1, node2 = self.select_two_nodes()
                self.swap(node1, node2)
                old_cut = self.current_cut_size
                self.initialize_cut()
                if self.current_cut_size < self.best_cut:
                    self.update_best_solution()             
                new_cut = self.current_cut_size
                delta = new_cut - old_cut
                if delta > 0:
                    if not self.try_to_accept(delta):                    
                        new_node1 = (node2[0], node1[1])
                        new_node2 = (node1[0], node2[1])
                        self.swap(new_node1, new_node2)
                        self.initialize_cut()
            self.cut_history.append(self.current_cut_size)
            self.update_temp()

        self.plot_graph()
        print("Best cut: {}\nBest solution: {}".format(self.best_cut, self.best_solution))

    def plot_graph(self):
        t = list(range(0, len(self.temperature_history)))
        data1 = self.temperature_history
        data2 = self.cut_history
        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Temperature', color=color)
        ax1.plot(t, data1, color=color)

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        color = 'tab:blue'
        ax2.set_ylabel('Cut', color=color)  # we already handled the x-label with ax1
        ax2.plot(t, data2, color=color)

        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        plt.show()


        
            
   
        
        