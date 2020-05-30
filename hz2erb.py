import numpy as np

# MATLAB's function converts from frequency in Hz to frequency in ERB.
def hz2erbMATLAB(hz):
    return ((1000 * np.log(10)) / (24.7 * 4.37)) * np.log10((1 + hz * 0.00437))

# Slaney's function converts from frequency in Hz to bandwith in ERB to determine the optimal bandwith of the gammatone filter.
def hz2erbSlaney(hz):
    return hz / 9.26449 + 24.7
    
# Glasberg and Moore's function is used by MATLAB in their gammatone filterbank to convert from frequency in Hz to bandwith in ERB.
# https://www.mathworks.com/help/audio/ref/gammatonefilterbank-system-object.html
def hz2erbGlasberg(hz):
    return 24.7 * (4.37 * hz / 1000 + 1)

# Slaney's function and Glasberg's function return nearly identical values.
# Slaney's function's decimal place accuracy is more than Glasberg's function.
print ("MATLAB: ", hz2erbMATLAB(440))
print ("Slaney: ", hz2erbSlaney(440))
print ("Glasberg and Moore: ", hz2erbGlasberg(440))
