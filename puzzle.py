import json

def load_puzzle(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["row_hints"], data["col_hints"], data["solution"], data["rows"], data["cols"]