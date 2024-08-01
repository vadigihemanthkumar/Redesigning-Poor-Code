import json

class Storage:
    @staticmethod
    def save_to_file(data, filename):
        # Save data to a JSON file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename):
        try:
            # Try to load data from a JSON file
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []





