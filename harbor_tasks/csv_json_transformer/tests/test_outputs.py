import json
import os
import pytest

class PathConfig:
    OUTPUT_FILE = '/app/output.json'

class OutputReader:
    @staticmethod
    def read_json(filepath):
        assert os.path.exists(filepath), f"File not found: {filepath}"
        with open(filepath, 'r') as f:
            return json.load(f)

class ValidationLogic:
    @staticmethod
    def validate_active_status(users):
        for user in users:
            assert str(user.get('active')).lower() == 'true', \
                f"Found inactive user in output: {user}"
    
    @staticmethod
    def validate_user_count(users, expected_count):
        assert len(users) == expected_count, \
            f"Expected {expected_count} users, found {len(users)}"
            
    @staticmethod
    def validate_specific_users(users, expected_names):
        found_names = {user.get('name') for user in users}
        assert expected_names.issubset(found_names), \
            f"Missing expected users. Found: {found_names}, Expected subset: {expected_names}"

class TestOutputValidator:
    def test_output_file_exists_and_is_valid(self):
        data = OutputReader.read_json(PathConfig.OUTPUT_FILE)
        
        assert isinstance(data, list), "Output should be a JSON list"
        
        ValidationLogic.validate_active_status(data)
        ValidationLogic.validate_user_count(data, 3)
        ValidationLogic.validate_specific_users(data, {'Alice', 'Charlie', 'Eve'})
