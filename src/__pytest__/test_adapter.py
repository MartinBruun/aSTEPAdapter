import pytest
import json

from src.adapter import Adapter

def test_hello():
    assert 1 == 1

def test_adapter_from_json_deserializes():
    expected_options_data = {
        "SomeOption": "This Option",
    }
    actual_options_data = json.dumps(expected_options_data)
    adapter = Adapter()

    deserialized_options = adapter.from_json(actual_options_data)

    assert deserialized_options == expected_options_data