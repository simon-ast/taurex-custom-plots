import numpy as np
import h5py as h5

"""
GOAL:   Reproduce (somewhat) the plots provided by TauREx, but make them
        "nicer" (frame spacing etc.)

PARTS: 

PSEUDCODE

"""


FILE = "retrieval.out"
test = h5.File(FILE)
print(test.keys())
