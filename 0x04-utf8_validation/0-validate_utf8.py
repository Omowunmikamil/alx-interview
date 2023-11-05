#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    numberBytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:

        maskByte = 1 << 7

        if numberBytes == 0:

            while maskByte & byte:
                numberBytes += 1
                maskByte = maskByte >> 1

            if numberBytes == 0:
                continue

            if numberBytes == 1 or numberBytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        numberBytes -= 1

    if numberBytes == 0:
        return True

    return False
