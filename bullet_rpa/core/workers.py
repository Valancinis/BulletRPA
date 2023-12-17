import json

def load_data():
    file_path = 'data/robots.json'
    with open(file_path, 'r') as file:
        # Check if the file is empty
        if file.tell() == 0:
            return None
        data = json.load(file)
    return data

def store_data(list):
    file_path = 'data/robots.json'
    with open(file_path, 'w') as f:
        json.dump(list, f)

