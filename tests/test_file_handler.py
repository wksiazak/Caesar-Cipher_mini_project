import json
from unittest.mock import MagicMock, patch

import pytest

from file_handler import FileManager


@pytest.fixture
def mock_db_handler():
    return MagicMock()


@pytest.fixture
def file_manager(mock_db_handler):
    return FileManager(mock_db_handler)


@pytest.fixture
def sample_data():
    return {"key1": "abc", "key2": "def", "key3": "xyz"}


def test_encrypt_json_file(file_manager, mock_db_handler, sample_data):
    with patch("builtins.open", return_value=MagicMock()) as mock_open:
        mock_open.return_value.__enter__().read.return_value = json.dumps(sample_data)

        file_manager.encrypt_json_file("test_file.json", 3)

        expected_calls = [(("key1", "def"),), (("key2", "ghi"),), (("key3", "abc"),)]
        assert mock_db_handler.add_to_ciphers.call_args_list == expected_calls


def test_decrypt_json_file(file_manager, mock_db_handler, sample_data):
    with patch("builtins.open", return_value=MagicMock()) as mock_open:
        mock_open.return_value.__enter__().read.return_value = json.dumps(sample_data)

        file_manager.decrypt_json_file("test_file.json", 3)

        expected_calls = [(("key1", "xyz"),), (("key2", "abc"),), (("key3", "uvw"),)]
        assert mock_db_handler.add_to_ciphers.call_args_list == expected_calls


def test_encrypt_json_file_file_not_found(file_manager, mock_db_handler):
    with patch("builtins.open", side_effect=FileNotFoundError()):
        file_manager.encrypt_json_file("non_existing_file.json", 3)
        assert mock_db_handler.add_to_ciphers.call_count == 0
