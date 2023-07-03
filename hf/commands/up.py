import os
from typing import *

from hf.api import api
from hf.fs import fs
from hf.utils import get_repo_info, join_current_dir


def run(local_file: str, filepath: str = None, ignore_patterns: List[str] = []):
    if local_file.endswith("/"):
        local_file = local_file[:-1]
    if filepath is None:
        filepath = os.path.split(local_file)[-1]
    filepath = join_current_dir(filepath)

    repo_type, repo_id, repo_path = get_repo_info(filepath)

    if os.path.isdir(local_file):
        api.upload_folder(
            folder_path=local_file,
            repo_id=repo_id,
            repo_type=repo_type,
            path_in_repo=repo_path,
            ignore_patterns=ignore_patterns,
        )
    else:
        if fs.exists(filepath) and fs.isdir(filepath):
            filepath = os.path.join(filepath, os.path.basename(local_file))
        api.upload_file(
            path_or_fileobj=local_file,
            repo_id=repo_id,
            repo_type=repo_type,
            path_in_repo=repo_path,
        )
