import os
from pathlib import Path


def check_if_file_exists():
    print(os.path.exists("/path/to/file"))
    print(Path("/Users/ccc/.bash_profile").exists())


def directory_of_the_script():
    print(Path(__file__).parent.absolute())


if __name__ == "__main__":
    check_if_file_exists()
