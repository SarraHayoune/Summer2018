
# Assignement3: Create a file and save it

import pynbody
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import os
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)


# loading the snapshot
s =pynbody.load('/mnt/cptmarvel/files.list')

print s 
