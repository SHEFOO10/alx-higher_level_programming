#!/usr/bin/python3
import hidden_4

[print(name) for name in dir(hidden_4) if not name.startswith('__')]
