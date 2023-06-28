import os
from concurrent.futures import ThreadPoolExecutor

from hf.fs import fs
from hf.utils import join_current_dir


def download(filepath: str, local_file: str):
    os.makedirs(os.path.dirname(local_file), exist_ok=True)
    with open(local_file, "wb") as f:
        with fs.open(filepath, "rb") as remote_file:
            f.write(remote_file.read())


def run(filepath: str, local_file: str = None, max_workers: int = os.cpu_count() / 2):
    filepath = join_current_dir(filepath)

    if filepath.endswith("/"):
        filepath = filepath[:-1]

    if local_file is None:
        local_file = "."
    if os.path.isdir(local_file):
        local_file = os.path.join(local_file, os.path.basename(filepath))

    if fs.isdir(filepath):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for item in fs.ls(filepath):
                if fs.isdir(item["name"]):
                    continue
                executor.submit(
                    download,
                    item["name"],
                    os.path.join(local_file, os.path.split(item["name"])[-1]),
                )
    else:
        download(filepath, local_file)
