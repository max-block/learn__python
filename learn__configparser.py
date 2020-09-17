import configparser
from pathlib import Path


def read_config_files():
    # section in .conf file is required
    conf_file = Path(__file__).parent.absolute().joinpath("data/t1.conf")
    print("conf_file", conf_file)
    print(conf_file.exists())

    with conf_file.open() as f:
        config = configparser.ConfigParser()
        config.read_file(f)
        var1 = config["main"]["var1"]
        var2 = config["main"]["var2"]
        print({"var1": var1, "var2": var2})
        # {'var1': '1', 'var2': 'bla bla'}


if __name__ == "__main__":
    read_config_files()
