from hf.fs import fs
from hf.state import get_current_directory, set_current_director
from hf.utils import join_current_dir


def run(filepath: str = ""):
    if filepath.startswith("/models"):
        filepath = filepath[8:]
    elif filepath.startswith("/datasets"):
        filepath = filepath[1:]
    else:
        filepath = join_current_dir(filepath)
    if not fs.exists(filepath):
        print(f"hf: cd: {filepath}: No such file or directory")
        return
    if fs.info(filepath)["type"] != "directory":
        print(f"hf: cd: {filepath}: Not a directory")
        return
    set_current_director(filepath)
    print(get_current_directory())
