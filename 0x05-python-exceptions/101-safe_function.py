#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        answer = fct(*args)
        return answer
    except Exception as error:
        sys.stderr.write(f"Exception: {error}\n")
        return None
