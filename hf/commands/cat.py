import sys

from hf.fs import fs
from hf.utils import join_current_dir


def run(filepath: str):
    filepath = join_current_dir(filepath)
    sys.stdout.buffer.write(fs.cat(filepath))
