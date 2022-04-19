import dataclasses
import graph
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
    temp_update: float
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
        return
    
    def try_to_accept(self):
        return 
    
    def update_temp(self):
        return   
    
    def random_move(self):
        return
    
    def cal_cost_delt(self):
        return
    
    def run(self):
        self.initialize_clusters()
        self.initialize_cut() 
        while self.current_temp> self.final_temp:
            self.random_move()
            self.cal_cost_delt()
            if self.cal_cost_delt>0:
                print("Movement is accepted")
            else:
                self.try_to_accept()
            self.update_temp()
        
            
   
        
        