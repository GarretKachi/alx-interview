#!/usr/bin/python3
""" valid UTF-8 encoding determination """


def validUTF8(data):
    """ doc """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
