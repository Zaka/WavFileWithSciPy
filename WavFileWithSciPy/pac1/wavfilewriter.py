#===============================================================================
# from scipy.io import wavfile
# from numpy import *
# 
# import math
# 
# freq = 440.0
# data_size = 40000
# fname = "WaveTest.wav"
# frate = 6025.0  # framerate as a float
# amp = 6000.0     # multiplier for amplitude
# 
# sine_list_x = zeros((2,data_size))
# for x in range(data_size):
#    sine_list_x[0][x] = math.sin(x)
#    sine_list_x[1][x] = math.sin(x)
#    #==========================================================================
#    # sine_list_x[x] = math.sin(2*pi*freq*(x/frate))
#    #==========================================================================
# 
# nchannels = 1
# sampwidth = 2
# framerate = int(frate)
# nframes = data_size
# comptype = "NONE"
# compname = "not compressed"
# 
# wavfile.write("test01.wav", frate, sine_list_x)
#===============================================================================

import numpy as np
from scipy.io.wavfile import write

def fib(n):
    list = np.zeros(n)
    for i in range(n):
        if i < 2:
            list[i] = 1
        else:
            list[i] = list[i - 1] + list[i - 2]
    
    return list


data = fib(44100)
#===============================================================================
# data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
#===============================================================================
scaled = np.int16(data/np.max(np.abs(data)) * 65536)
write('test.wav', 44100, scaled)