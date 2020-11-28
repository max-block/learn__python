def check_auth(f):
    def wrapper(*args):
        print("0", args[0])
        print("1", args[1])
        return f(*args)

    return wrapper


class TelegramBot:
    @check_auth
    def cmd1_handler(self, login: str, password: str):
        pass

    @check_auth
    def cmd2_handler(self, login: str, password: str):
        pass


def main():
    tb = TelegramBot()
    tb.cmd1_handler("u1", "p1")


if __name__ == "__main__":
    main()
