import tempfile


def temp_file():
    with tempfile.NamedTemporaryFile(mode="w+t") as f:
        f.write("bla bla")
        print(f.name)
        # /var/folders/qp/bqd8cy5945xb1y4jn23z_hbh0000gn/T/tmp5xmavu1_


if __name__ == "__main__":
    temp_file()
