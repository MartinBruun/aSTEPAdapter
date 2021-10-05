import pytest
import json

from src.adapter import Adapter

@pytest.mark.parametrize("test_dict", [
    (None),
    ({}),
])
def test_adapter_from_json_deserializes_options_for_creator(test_dict):
    expected_options_dict = test_dict
    serialized_test_json = json.dumps(expected_options_dict)
    adapter = Adapter()

    deserialized_options = adapter.from_json(serialized_test_json)

    assert deserialized_options == expected_options_dict

def test_adapter_to_json_serializes_to_traffic_model_schema(fake_mapdata_node, fake_mapdata_edge):
    adapter = Adapter()

    serialized_model = adapter.to_json(
        nodes=fake_mapdata_node, 
        edges=fake_mapdata_edge
    )

    expected_model = {
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
    assert expected_model == json.loads(serialized_model)