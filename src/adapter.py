import json

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
        nodes = table_kwargs["nodes"]
        for row in table_kwargs["nodes"]:
            node_id = row["node_id"]
            longitude = row["lon"]
            latitude = row["lat"]
            node_weight = row["node_weight"]

            edges=table_kwargs["edges"]
            for row in table_kwargs["edges"]:
                to_node_id = row["to_node_id"] #TODO: RFC navneændring
                from_node=row["edge_basenode"]
                distance=row["distance"]
                road_name=row["edge_name"]
                highway=row["highway"]#UNDEFINED
                max_speed=row["maxspeed"]#UNDEFINED
                to_node=row["edge_adj"]

        example_model = {
        "error_list": [],
        "meta_data": {
            "last_service": "Creator",
            "priority": None,
        },
        "vehicle":{
            
        },
        "nodes": [
            {
                "id": node_id,
                "weight": node_weight,
                "data":{
                
                },
                "edges": [
                    {
                        "to_node_id": 1,
                        "weight": 1,
                        "data":{

                        },
                    },
                ],
            },
            {
                "id": 1,
                "weight": 1,
                "data":{
                
                },
                "edges": [
                    {
                        "id": 1,
                        "weight": 1,
                        "data":{

                        },
                    },
                ],
            },
            {
                "id": 1,
                "weight": 1,
                "data":{
                
                },
                "edges": [
                    {
                        "id": 1,
                        "weight": 1,
                        "data":{

                        },
                    },
                ],
            },
            {
                "id": 1,
                "weight": 1,
                "data":{
                
                },
                "edges": [
                    {
                        "id": 1,
                        "weight": 1,
                        "data":{
                            
                        },
                    },
                ],
            },
        ]
        }
        serialized_data = json.dumps(example_model)
        return serialized_data