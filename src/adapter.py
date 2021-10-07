import json
from DataModel import  DataModel
from Edge import Edge
from Node import Node



class Adapter:
    """
        The Adapter is responsible for serialization and deserialization of the Transport Network Model (TNM) defined in RFC0020.
        It follows the following interface:
            from_json(JSON model)
            to_json(**table_kwargs)
        All Microservices following TNM must have an Adapter implementing this interface.
    """

    def __init__(self):
        """
            The Adapter constructor. Currently not in use.
        """
        pass

    def from_json(self, options):
        """
            Converts the TNM to some internal representation.
            In this Creator service, it converts some options (defined in RFC0020) from JSON to a python dictionary.
        """
        if options == None:
            options = {}
        return json.loads(options)

    def to_json(self, **table_kwargs):
        """ 
            Converts the internal representation from the service to the TNM.
            In this Creator service, it converts data from the Database to the initial JSON schema following the TNM.
        """
        nodesJSON = table_kwargs["nodes"]
        nodes = []
        # for row in table_kwargs["nodes"]:
        #     nodes.append(makeNode(row))
        

        edges=table_kwargs["edges"]
        for row in table_kwargs["edges"]:
            edges.append(makeEdge(row))
            
            
        for node in table_kwargs["nodes"]:
            nodes.append(makeNode(row))
            for edge in edges:
                if node.id == edge.from_node_id:
                    node.edges.append(edge)
                    edges.remove(edge)
            DataModel.nodes.append(node)
            

        serialized_data = json.dumps(DataModel)
        return serialized_data
                  
        # example_model = {
        # "error_list": [],
        # "meta_data": {
        #     "last_service": "Creator",
        #     "priority": None,
        # },
        # "vehicle":{
            
        # },
        # "nodes": [
        #     {
        #         "id": node_id,
        #         "weight": node_weight,
        #         "data":{
                
        #         },
        #         "edges": [
        #             {
        #                 "to_node_id": 1,
        #                 "weight": 1,
        #                 "data":{

        #                 },
        #             },
        #         ],
        #     },
        #     {
        #         "id": 1,
        #         "weight": 1,
        #         "data":{
                
        #         },
        #         "edges": [
        #             {
        #                 "id": 1,
        #                 "weight": 1,
        #                 "data":{

        #                 },
        #             },
        #         ],
        #     },
        #     {
        #         "id": 1,
        #         "weight": 1,
        #         "data":{
                
        #         },
        #         "edges": [
        #             {
        #                 "id": 1,
        #                 "weight": 1,
        #                 "data":{

        #                 },
        #             },
        #         ],
        #     },
        #     {
        #         "id": 1,
        #         "weight": 1,
        #         "data":{
                
        #         },
        #         "edges": [
        #             {
        #                 "id": 1,
        #                 "weight": 1,
        #                 "data":{
                            
        #                 },
        #             },
        #         ],
        #     },
        # ]
        # }

def makeNode(row):
    node_id : row["node_id"]
    longitude : row["lon"]
    latitude : row["lat"]
    node_weight :  row["node_weight"]
    edges = []
    node = {node_id,longitude,latitude,node_weight,edges}
    
    return node

def makeEdge(row):
    # edge_id= ["edge_id"]
    # to_node_id = row["edge_adj"] #TODO: RFC navneændring
    # from_node = row["edge_basenode"]
    # distance = row["distance"]
    # road_name = row["edge_name"]
    # road_type = row["residential"]#UNDEFINED 
    # max_speed = row["maxspeed"]#UNDEFINED
    # to_node = row["edge_adj"]
    edge = Edge(row)
    {edge_id,from_node,distance,road_name,road_type,max_speed,to_node}
    
    
    return 

    