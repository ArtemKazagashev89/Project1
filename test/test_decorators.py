import os

import pytest

from src.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


def test_log_file():
    my_function(1, 2)
    with open("mylog.txt", "r") as file:
        assert "my_function ok\n" in file.read()


def test_log_console(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok\n" in captured.out


def test_log_error_file():
    @log(filename="mylog.txt")
    def error_function():
        raise ValueError("test error")

    error_function()
    with open("mylog.txt", "r") as file:
        assert "error_function error: ValueError. Inputs: (), {}\n" in file.read()


def test_log_error_console(capsys):
    @log()
    def error_function(x):
        return 1 / x

    error_function(0)
    captured = capsys.readouterr()
    assert "error_function error: ZeroDivisionError. Inputs: (0,), {}\n" in captured.out
