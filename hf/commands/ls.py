from colorama import Fore

from hf.fs import fs
from hf.utils import hr_size, join_current_dir


def run(filepath: str = "", a: bool = False, l: bool = False, h: bool = False):
    filepath = join_current_dir(filepath)
    result = fs.ls(filepath)
    files = []
    for item in result:
        item["name"] = item["name"][len(filepath) + 1 :].split("/")[0]
        if item["name"] == "" or any([x for x in files if x["name"] == item["name"]]):
            continue
        if item["name"].startswith("."):
            if not a:
                continue

        info = fs.info(filepath + "/" + item["name"])

        if info["type"] == "directory":
            item["name"] = Fore.BLUE + item["name"] + Fore.RESET + "/"

        if h:
            item["size"] = hr_size(item["size"])

        files.append(
            {
                "name": item["name"],
                "size": item["size"],
                "last_modified": info["last_modified"]
                if "last_modified" in info
                else None,
            }
        )
    if l:
        for item in files:
            print(
                f"{item['size']:>10} {item['last_modified'].strftime('%b %d %H:%M') if item['last_modified'] is not None else '':>12} {item['name']}"
            )
    else:
        print(" ".join([item["name"] for item in files]))
