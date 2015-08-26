import numpy as np
import os
import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def parse_section(open_file):
    """
    Parse a section in an ms output file.
    A section should start with '//'
    """
    res = []

    line = open_file.readline()

    # EOF
    if line == '':
        return (True,0,np.array([]))

    while line != '//\n':
        line = open_file.readline()

    line = open_file.readline()
    marker_segsites = "segsites:"
    if not line.startswith(marker_segsites):
        logging.error("No segsites in the section")
        return # do nothing, consider sys.exit()

    nbsegsites = int(line[len(marker_segsites)+1:])

    line = open_file.readline()
    marker_position = "positions:"
    if not line.startswith(marker_position):
        logging.error("No positions in the section")
        # Because we dont use position, then we directly use this line
    else:
        line = open_file.readline()

    i = 0
    while line != '\n' and line != '':
        line = line[:-1]
        res.append([int(elem) for elem in line])
        line = open_file.readline()
        
    return (False,nbsegsites,np.array(res))

