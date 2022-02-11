from to_do_list.hello import hello_world


def test_hello_world_is_printing(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
    assert captured.err == ""


def test_hello_world_arg_not_zero(capsys):
    hello_world(arg=1)
    captured = capsys.readouterr()
    assert captured.out == "arg not 0\n"
    assert captured.err == ""
