#!/usr/bin/python3
""" Console Module """
from console import HBNBCommand
import io
from unittest.mock import patch

with patch('sys.stdout', new=io.StringIO()) as f:
    HBNBCommand().onecmd('help')
    print(f.getvalue())
