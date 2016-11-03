#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function,division

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,100,1)
y=x**2
y2=x**3

plt.plot(x,y,'.')
plt.plot(x,y2,'--')

plt.xlabel('Age')
plt.ylabel('Hatred')
plt.show()
