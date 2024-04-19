import sys
from src import main


def test_hello(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
