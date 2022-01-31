"""
This is a quick app to pick a student at random. Will add more bells and whistles when the time comes.
The plan for V1 is a simple commandline program that will return a random student.
"""

__author__ = 'Katie Kruzan'
__version__ = '1.0'

import random


def run(file):
    #
    with open(file, 'r') as f:
        students = [x.strip() for x in f.readlines()]
    # print(students)
    return random.choice(students)


if __name__ == '__main__':
    # We will expect the students will be in a txt document with one student per line.
    # This file will be in the /input folder
    filename = 'input/students.txt'
    print(run(filename))
