#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'Integer_Math' function below.
#
# The function accepts following parameters:




#  1. INTEGER Side
#  2. INTEGER Radius
#

def Integer_Math(Side, Radius):
    # Write your code here
    a = Side * Side
    b = Side * Side * Side
    c = 3.14 * Radius * Radius
    x = round(c,2)
    d = (4/3)*3.14*Radius*Radius*Radius
    y = round(d,2) 
    print("Area of Square is "+ str(a))
    print("Volume of Cube is "+ str(b))
    print("Area of Circle is "+ str(x))
    print("Volume of Sphere is "+ str(y))
    
if __name__ == '__main__':
    Side = int(input().strip())

    Radius = int(input().strip())

    Integer_Math(Side, Radius)