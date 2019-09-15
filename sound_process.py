
import numpy as np
from scipy.io.wavfile import read

"""
A1-Part-1: Reading an audio file

Write a function that reads an audio file and returns 10 consecutive samples of the file starting from 
the 50001th sample. This means that the output should exactly contain the 50001th sample to the 50010th 
sample (10 samples). 

The input to the function is the file name (including the path) and the output should be a numpy array 
containing 10 samples.

If you use the wavread function from the utilFunctions module the input samples will be automatically 
converted to floating point numbers with a range from -1 to 1, which is what we want. 

Remember that in python, the index of the first sample of an array is 0 and not 1.

If you run your code using piano.wav as the input, the function should return the following 10 samples:  
array([-0.06213569, -0.04541154, -0.02734458, -0.0093997 ,  0.00769066,	0.02319407,  0.03503525, 
0.04309214, 0.04626606,  0.0441908], dtype=float32)
"""


def readAudio(inputFile):
    """
    Input:
        inputFile: the path to the wav file      
    Output:
        The function should return a numpy array that contains 10 samples of the audio.
    """

    print("readAudio")
    # Read a sound file and convert it to a normalized floating point array

    ## Your code here
    #if (os.path.isfile(inputFile) == False):                  # raise error if wrong input file
    #    raise ValueError("Input file is wrong")

    fs,data = read(inputFile,'r')
    #print("Sampling Rate ",fs)
    
    #Total size of Data
    #print("Data ",len(data))    
    
    # Data Type of Wav Sample
    #dtype = data.dtype
    #print("Data Type is",dtype)
    
    # Channel Type : Mono or not
    #channel_type = len(data.shape)
    #print("channel_type", channel_type)   
    
    #scale down and convert audio into floating point number in range of -1 to 1
    
    data = np.asarray(data)

    data = np.float32(data)/((2**15) -1)
    
    
    # Return the 10 samples start from 50000
    return data[50000:50010]
    #Nomarize the data

    
def minMaxAudio(inputFile):

    """
    Input:
        inputFile: file name of the wav file (including path)
    Output:
        A tuple of the minimum and the maximum value of the audio samples, like: (min_val, max_val)
    """
    ## Your code here

    #print("minMax Audio")
    fs,data = read(inputFile,'r')
    #scale down and convert audio into floating point number in range of -1 to 1
    data = np.float32(data)/((2**15) -1)
    
    max = np.max(data)
    min = np.min(data)
    return min,max    
 
    
def hopSamples(x,M):
    """
    Inputs:
        x: input numpy array
        M: hop size (positive integer)
    Output:
        A numpy array containing every Mth element in x, starting from the first element in x.
    """
    op = []
  
    for i in range (len(x)):
        if (i % M) == 0:
            op.append(x[i])
    op = np.asarray(op)
    print("Op data Type ",type(op))        
    return op        
    

    

        
    
#Upload the Data from Database and pass the path
SoundPath = 'E:/2019/working_dir/audio_process/sms-tools/sounds/oboe-A4.wav'
ret = readAudio(SoundPath)


print(ret)


min,max = minMaxAudio(SoundPath)
print("(Min , Max)",min,max)

x=np.arange(40)
res = hopSamples(x,2)
print("Fianl result", res)
