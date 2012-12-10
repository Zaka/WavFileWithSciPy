#===============================================================================
# Onda senoidal mono
#===============================================================================
import numpy as np
from scipy.io.wavfile import write

freq = 440.0
frate = 9000.0
amp = 4000.0

seconds = 4.0
start = 0
stop = seconds * 44100.0
step = 1

data = amp * np.sin(2 * np.pi * freq * np.arange(start,stop,step)/frate)
#===============================================================================
# data = np.random.uniform(-1,1,5*44100) # 44100 random samples between -1 and 1
#===============================================================================
scaled = np.int16(data/np.max(np.abs(data)) * 65536)
write('test.wav', 44100, scaled)