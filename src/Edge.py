class Edge:
    def __init__(self,edgeFromDatabase):
        self.edge_id= ["edge_id"]
        self.to_node_id = edgeFromDatabase["edge_adj"] #TODO: RFC navneændring
        self.from_node = edgeFromDatabase["edge_basenode"]
        self.Data={
        "distance" : edgeFromDatabase["distance"],
        "road_name" : edgeFromDatabase["edge_name"],
        "road_type" : edgeFromDatabase["residential"],#UNDEFINED 
        "max_speed" : edgeFromDatabase["maxspeed"],#UNDEFINED
        }
