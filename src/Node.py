class Node:

    def __init__(self,nodeFromDatebase)
        self.node_id = nodeFromDatebase["node_id"]
        self.data = {
        "longitude" : nodeFromDatebase["lon"],
        "latitude" : nodeFromDatebase["lat"]
        }
        self.node_weight = nodeFromDatebase["node_weight"]
        self.edges = [] 
    