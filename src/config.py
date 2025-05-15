import json
import yaml

def load_config(file_path):
    """
    Load configuration from a JSON or YAML file.
    """
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file format. Use JSON or YAML.")
