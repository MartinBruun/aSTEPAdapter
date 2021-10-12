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

def test_adapter_to_json_serializes_grouping_1_to_traffic_model_schema(fake_mapdata_node_1, fake_mapdata_edge_1, fake_expected_model_1):
    adapter = Adapter()

    serialized_model = adapter.to_json(
        nodes=fake_mapdata_node_1, 
        edges=fake_mapdata_edge_1
    )

    assert fake_expected_model_1 == json.loads(serialized_model)

# def test_adapter_to_json_serializes_grouping_2_to_traffic_model_schema(fake_mapdata_node_2, fake_mapdata_edge_2, fake_expected_model_2):
#     adapter = Adapter()

#     serialized_model_2 = adapter.to_json(
#         nodes=fake_mapdata_node_2, 
#         edges=fake_mapdata_edge_2
#     )

#     assert fake_expected_model_2 == json.loads(serialized_model_2)