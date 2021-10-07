import json
from .data_model import  DataModel
#from .edge import Edge



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
        dataModel = DataModel
        nodesJSON = table_kwargs["nodes"]
        dataModel.errorList = table_kwargs["errors"]
        dataModel.metadata = table_kwargs["metadata"]
        dataModel.vehicle = table_kwargs["vehicle"]

        #Add nodes to dataModel
        for row in table_kwargs["nodes"]:
            node=makeNode(row)
            dataModel.nodes.insert(node.node_id, node)#add node at its node_id
        
        #Add edges to nodes in dataModel
        for row in table_kwargs["edges"]:
            edge = makeEdge(row)
            from_node_id = row["edge_basenode"]
            dataModel.nodes[from_node_id].edges.insert(edge.edge_id,edge)#the from_node_id is used to position an edge at its origining node, and the edge, using this alternative can remove edge.from_node_id from makeEdge
           
        serialized_data = json.dumps(dataModel)
        return serialized_data
                  
        

def makeNode(row):
    node ={} 
    node.node_id = row["node_id"]
    node.node_weight = row["node_weight"]
    node.edges = [] 
    node.data = {
        "longitude" : row["lon"],
        "latitude" : row["lat"]
    }
    return node

def makeEdge(row):
    edge = {}
    edge.edge_id= row["edge_id"]
    edge.to_node_id = row["edge_adj"] #TODO: RFC navneændring
    #edge.from_node_id = row["edge_basenode"]#TODO: RFC navneændring
    edge.Data={
        "distance" : row["distance"],
        "road_name" : row["edge_name"],
        "road_type" : row["highway"],#UNDEFINED 
        "max_speed" : row["maxspeed"],#UNDEFINED
    }
    return edge

    