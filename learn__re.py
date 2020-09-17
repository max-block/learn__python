import re


def t1():
    # find 0x19184ab45c40c2920b0e0e31413b9434abd243ed
    data = "/token/0x514910771af9ca656af840dff83e8264ecf986ca?a=0x19184ab45c40c2920b0e0e31413b9434abd243ed"
    m = re.search(r"\?a=(.*)$", data)
    if m:
        print(m.group(1))  # 0x19184ab45c40c2920b0e0e31413b9434abd243ed


if __name__ == "__main__":
    t1()
