import json
import os

class Storage:
    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename):
        if not os.path.isfile(filename):
            print(f"Error: File '{filename}' not found.")
            # Create default file content based on the filename
            default_data = [] if filename != 'checkouts.json' else [{}]
            Storage.save_to_file(default_data, filename)
            return default_data
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file '{filename}': {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []



