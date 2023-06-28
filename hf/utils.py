from .state import get_current_directory


def hr_size(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def join_current_dir(filepath: str = ""):
    cur = get_current_directory()
    for name in filepath.split("/"):
        if name == "..":
            cur = cur.parent
        elif name == ".":
            continue
        else:
            cur = cur.joinpath(name)
    return str(cur)


def get_repo_info(
    filepath: str = "",
):
    if filepath.startswith("datasets"):
        repo_type = "dataset"
        filepath = filepath[9:]
        repo_id = "/".join(filepath.split("/")[:2])
        filepath = filepath[len(repo_id) + 1 :]
    else:
        repo_type = "model"
        filepath = filepath[8:]
        repo_id = filepath.split("/")[0]
        filepath = filepath[len(repo_id) + 1 :]
    return repo_type, repo_id, filepath
