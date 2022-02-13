def hello_world(arg=0):
    if arg == 0:
        print("hello world")
    else:
        print("arg not 0")


if __name__ == "__main__":  # pragma: no cover
    hello_world()
