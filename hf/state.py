import json
import os
from pathlib import Path

HF_STATE_FILE_PATH = Path.home().joinpath(".hf", "hf-state.json")


def load_state():
    os.makedirs(os.path.dirname(HF_STATE_FILE_PATH), exist_ok=True)
    if not os.path.exists(HF_STATE_FILE_PATH):
        with open(HF_STATE_FILE_PATH, "w") as f:
            json.dump({"current_directory": ""}, f)
    with open(HF_STATE_FILE_PATH, "r") as f:
        return json.load(f)


def save_state(state):
    with open(HF_STATE_FILE_PATH, "w") as f:
        json.dump(state, f)


def set_current_director(filepath: str):
    state = load_state()
    state["current_directory"] = filepath
    save_state(state)


def get_current_directory():
    state = load_state()
    return Path(state["current_directory"])
