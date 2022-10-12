#!/bin/python3

"""Script for commenting out missing files from tripwire policy text file"""

from genericpath import isfile
import re
from sys import argv
from os import path


GETFILE = r"^\s*(?P<filename>[^#(){}\s]+)\s*->.*$"

lines = []

if __name__ == '__main__':
    if len(argv) < 2:
        print('Usage: twpol-fix.py <twpol.txt>')
    with open(argv[1], 'r') as f:
        for line in f:
            m = re.match(GETFILE, line, re.M)
            if m is not None:
                filename = m.group('filename')
                if path.exists(filename):
                    lines.append(line)
                else:
                    lines.append('# not found #' + line)
            else:
                lines.append(line)
    
    with open(argv[1]+'.new', 'w') as f:
        for line in lines:
            f.write(line)