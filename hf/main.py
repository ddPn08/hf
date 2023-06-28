from fire import Fire

from .commands import COMMANDS


def main():
    Fire({k: v.run for k, v in COMMANDS.items()})


if __name__ == "__main__":
    main()
