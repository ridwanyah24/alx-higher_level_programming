#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        answer = fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}".format(error))
        return None
    return answer
