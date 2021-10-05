import pytest
import json

from src.adapter import Adapter

@pytest.mark.parametrize("test_dict", [
    (None),
    ({}),
])
def test_adapter_from_json_deserializes(test_dict):
    expected_options_dict = test_dict
    serialized_test_json = json.dumps(expected_options_dict)
    adapter = Adapter()

    deserialized_options = adapter.from_json(serialized_test_json)

    assert deserialized_options == expected_options_dict