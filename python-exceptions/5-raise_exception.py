#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("A type error occurred")
    except TypeError:
        print("Exception has been raised")
