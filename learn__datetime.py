from datetime import datetime


def replace():
    d1 = datetime.now()
    print(d1)  # 2020-02-13 08:41:25.956719
    d2 = d1.replace(year=2222)
    print(d1)  # 2020-02-13 08:41:25.956719
    print(d2)  # 2222-02-13 08:41:49.605996


def current_timestamp():
    value = datetime.utcnow().timestamp()
    print(value)  # 1590372867.085675
    print(int(value))  # 1590372867


if __name__ == "__main__":
    current_timestamp()
