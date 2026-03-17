# This test file contains unit tests for the core processing logic of the agnostic lambda core package.
from agnostic_lambda_core.core import process_data

def test_process_data_returns_expected_result():
    payload = {"user": "Ervin"}
    result = process_data(payload)

    assert result["status"] == "works"
    assert result["subsystem"] == "agnostic-core-v3"
    assert "Ervin" in result["message"]