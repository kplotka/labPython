import json
import os

SAVE_FILE = "save.json"

def level_key_from_path(path):
    if path is None:
        return "unknown"
    return os.path.splitext(os.path.basename(path))[0]

def save_game(name, level_path, grid_data):
    level_key = level_key_from_path(level_path)
    data = {}
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
    if level_key not in data:
        data[level_key] = {}
    data[level_key][name] = {"grid": grid_data}
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_all_saves():
    if not os.path.exists(SAVE_FILE):
        return {}
    with open(SAVE_FILE, "r") as f:
        return json.load(f)

def load_save_by_name(level_path, name):
    key = level_key_from_path(level_path)
    saves = load_all_saves()
    return saves.get(key, {}).get(name, None)