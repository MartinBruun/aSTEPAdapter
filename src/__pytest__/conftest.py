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
            "node_id": 1,
            "lon": 41,
            "lat": 51
        },
        {
            "node_id": 2,
            "lon": 42,
            "lat": 52
        },
        {
            "node_id": 3,
            "lon": 43,
            "lat": 53
        },
        {
            "node_id": 4,
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
            "edge_id": 1,
            "edge_basenode": 1,
            "distance": 100,
            "edge_name": "Eksempel Gade",
            "highway": True,
            "maxspeed": 130,
            "edge_adj": 2,
        },
        {
            "edge_id": 2,
            "edge_basenode": 2,
            "distance": 200,
            "edge_name": "Eksempel Gade",
            "highway": False,
            "maxspeed": 80,
            "edge_adj": 3,
        },
        {
            "edge_id": 3,
            "edge_basenode": 3,
            "distance": 300,
            "edge_name": "Eksempel Gade",
            "highway": False,
            "maxspeed": 50,
            "edge_adj": 4,
        },
    ]

def fake_expected_model_1():
    return {
        "error_list": [],
        "meta_data": {
            "last_service": "Creator",
            "priority": None,
        },
        "vehicle":{
            
        },
        "nodes": [
            {
                "id": 1,
                "weight": 1,
                "data":{
                
                },
                "edges": [
                    {
                        "id": 2,
                        "weight": 1,
                        "data":{
                            "name": "Eksempel Gade",
                            "highway": True,
                            "distance": 100,
                            "max_speed": 130
                        },
                    },
                ],
            },
            {
                "id": 2,
                "weight": 1,
                "data":{
                
                },
                "edges": [
                    {
                        "id": 1,
                        "weight": 1,
                        "data":{
                            "name": "Eksempel Gade",
                            "highway": True,
                            "distance": 300,
                            "max_speed": 130
                        },
                    },
                    {
                        "id": 3,
                        "weight": 1,
                        "data":{
                            "name": "Eksempel Gade",
                            "highway": False,
                            "distance": 200,
                            "max_speed": 80
                        },
                    },
                ],
            },
            {
                "id": 3,
                "weight": 1,
                "data":{
                
                },
                "edges": [
                    {
                        "id": 2,
                        "weight": 1,
                        "data":{
                            "name": "Eksempel Gade",
                            "highway": False,
                            "distance": 200,
                            "max_speed": 80
                        },
                    },
                    {
                        "id": 4,
                        "weight": 1,
                        "data":{
                            "name": "Eksempel Gade",
                            "highway": False,
                            "distance": 300,
                            "max_speed": 50
                        },
                    },
                ],
            },
            {
                "id": 4,
                "weight": 1,
                "data":{
                
                },
                "edges": [
                    {
                        "id": 3,
                        "weight": 1,
                        "data":{
                            "name": "Eksempel Gade",
                            "highway": False,
                            "distance": 300,
                            "max_speed": 50
                        },
                    },
                ],
            },
        ]
    }

"""
    FIXTURE GROUPING 2: Not Defined Yet
"""