import json


def load_data(file_path):
    with open(file_path, 'r') as file:
        # Check if the file is empty
        content = file.read()
        # Check if the content is empty
        if not content:
            return []
        data = json.loads(content)
    return data


def store_data(bot_list, file_path):
    with open(file_path, 'w') as f:
        json.dump(bot_list, f)