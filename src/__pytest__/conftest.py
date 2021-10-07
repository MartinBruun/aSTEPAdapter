import pytest

"""
    A file of all the fixtures for each table which should be accepted by the Adapter.
    Each fixture follows the format:
    fake_database_table_number()
    where 
    "fake" indicates it is mock data, 
    "database" is the database it is from, 
    "table" is the table mocked.
    "number" is the fixture grouping, such as to create different example datasets and expected models
    
    Each Fixture Grouping should have an "fake_expected_model_number" to show the expected model if all the fixtures are combined to TNM standard.
"""

"""
    FIXTURE GROUPING 1: a graph of 4 nodes, connected in a straight line
"""

@pytest.fixture
def fake_mapdata_node_1():
    """

    """
    return [
        {
            "node_id": 0,
            "lon": 41,
            "lat": 51
        },
        {
            "node_id": 1,
            "lon": 42,
            "lat": 52
        },
        {
            "node_id": 2,
            "lon": 43,
            "lat": 53
        },
        {
            "node_id": 3,
            "lon": 44,
            "lat": 54
        },
    ]

@pytest.fixture
def fake_mapdata_edge_1():
    """
        Edges making a straight line from node 1 to node 4 in fake_mapdata_node, with distance increasing by 100 each time
    """
    return [
        {
            "edge_id": 0,
            "edge_basenode": 0,
            "distance": 10,
            "edge_name": "Eksempel Gade",
            "highway": "highway",
            "maxspeed": 130,
            "edge_adj": 1,
        },
        {
            "edge_id": 1,
            "edge_basenode": 1,
            "distance": 100,
            "edge_name": "Eksempel Gade",
            "highway": "highway",
            "maxspeed": 130,
            "edge_adj": 2,
        },
        {
            "edge_id": 2,
            "edge_basenode": 1,
            "distance": 200,
            "edge_name": "Eksempel Gade",
            "highway": "residential",
            "maxspeed": 80,
            "edge_adj": 3,
        },
        {
            "edge_id": 3,
            "edge_basenode": 2,
            "distance": 300,
            "edge_name": "Eksempel Gade",
            "highway": "residential",
            "maxspeed": 80,
            "edge_adj": 4,
        },
        {
            "edge_id": 4,
            "edge_basenode": 2,
            "distance": 400,
            "edge_name": "Eksempel Gade",
            "highway": "city",
            "maxspeed": 50,
            "edge_adj": 5,
        },
        {
            "edge_id": 5,
            "edge_basenode": 3,
            "distance": 500,
            "edge_name": "Eksempel Gade",
            "highway": "city",
            "maxspeed": 50,
            "edge_adj": 6,
        },
        {
            "edge_id": 6,
            "edge_basenode": 1,
            "distance": 600,
            "edge_name": "Eksempel Gade2",
            "highway": "highway",
            "maxspeed": 135,
            "edge_adj": 0,
    #edge.from_node_id = row["edge_basenode"]#TODO: RFC navneændring
        }
    ]


@pytest.fixture
def fake_expected_model_1():
    return {
        "error_list": [],
        "meta_data": {
            "last_service": "Creator",
            "priority": 0,
        },
        "vehicle":{
            "id":0,
            "data":{}
        },
        "nodes": [
            {
                "node_id": 0,
                "node_weight": 0,
                "data":{
                    "longitude": 41,
                    "latitude": 51,
                },
                "edges": [
                    {
                        "edge_id": 0,
                        "to_node_id": 1,
                        "edge_weight": 0,
                        "data":{
                            "road_name": "Eksempel Gade",
                            "distance": 10,
                            "max_speed": 130,
                            "road_type": "highway"
                        },
                    },
                ],
            },
            {
                "node_id": 1,
                "node_weight": 0,
                "data":{
                    "longitude": 42,
                    "latitude": 52,
                },
                "edges": [
                    {
                        "edge_id": 1,
                        "to_node_id": 2,
                        "edge_weight": 0,
                        "data":{
                            "road_name": "Eksempel Gade",
                            "distance": 100,
                            "max_speed": 130,
                            "road_type": "highway"

                        },
                    },
                    {
                        "edge_id": 2,
                        "to_node_id": 3,
                        "edge_weight": 0,
                        "data":{
                            "road_name": "Eksempel Gade",
                            "distance": 200,
                            "max_speed": 80,
                            "road_type": "residential"
                        },
                    },
                    {
                        "edge_id": 6,
                        "to_node_id": 0,
                        "edge_weight": 0,
                        "data":{
                            "road_name": "Eksempel Gade2",
                            "distance": 600,
                            "max_speed": 135,
                            "road_type": "highway"
                        },
                    },
                ],
            },
            {
                "node_id": 2,
                "node_weight": 0,
                "data":{
                    "longitude": 43,
                    "latitude": 53,
                },
                "edges": [
                    {
                        "edge_id": 3,
                        "to_node_id": 4,
                        "edge_weight": 0,
                        "data":{
                            "road_name": "Eksempel Gade",
                            "distance": 300,
                            "max_speed": 80,
                            "road_type": "residential"
                        },
                    },
                    {
                        "edge_id": 4,
                        "to_node_id": 5,
                        "edge_weight": 0,
                        "data":{
                            "road_name": "Eksempel Gade",
                            "distance": 400,
                            "max_speed": 50,
                            "road_type": "city"
                        },
                    },
                ],
            },
            {
                "node_id": 3,
                "node_weight": 0,
                "data":{
                    "longitude": 44,
                    "latitude": 54,
                },
                "edges": [
                    {
                        "edge_id": 5,
                        "to_node_id": 6,
                        "edge_weight": 0,
                        "data":{
                            "road_name": "Eksempel Gade",
                            "distance": 500,
                            "max_speed": 50,
                            "road_type": "city"
                        },
                    },
                ],
            },
  ]
  }

"""
    FIXTURE GROUPING 2: Not Defined Yet
"""