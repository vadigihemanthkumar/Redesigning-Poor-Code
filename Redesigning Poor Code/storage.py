import json

class Storage:
    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                if not content.strip():  # Check for empty file
                    raise ValueError(f"{filename} is empty.")
                return json.loads(content)
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {filename}: {e}")
            return []
        except ValueError as e:
            print(e)
            return []

