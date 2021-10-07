import pytest
import json

from src.adapter import Adapter

# Should be changed to get a json string as input, when options gets a clear usecase
def test_adapter_from_json_deserializes_empty_options_for_creator():
    serialized_test_json = json.dumps({})
    adapter = Adapter()

    deserialized_options = adapter.from_json(serialized_test_json)

    assert {} == deserialized_options

def test_adapter_to_json_serializes_grouping_1_to_traffic_model_schema(fake_mapdata_node_1, fake_mapdata_edge_1, fake_expected_model_1):
    adapter = Adapter()

    serialized_model = adapter.to_json(
        nodes=fake_mapdata_node_1, 
        edges=fake_mapdata_edge_1
    )

    assert fake_expected_model_1 == json.loads(serialized_model)