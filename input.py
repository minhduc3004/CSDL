import numpy as np
import librosa
import glob
import csv
import os.path

FRAME_SIZE = 2048
HOP_LENGTH = 1024
sr=44100

def rmse(signal, frame_size, hop_length):
    rmse = []
    
    # calculate rmse for each frame
    for i in range(0, len(signal), hop_length): 
        rmse_current_frame = np.sqrt(sum(signal[i:i+frame_size]**2) / frame_size)
        rmse.append(rmse_current_frame)
    return np.array(rmse)

def extract_zcr(file):
    arr_zcr = librosa.feature.zero_crossing_rate(file, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
    return arr_zcr

def extract_sc(file):
    arr_sc = librosa.feature.spectral_centroid(y=file, sr=sr, n_fft=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
    return arr_sc

def extract_bandwith(file):
    arr_bandwith = librosa.feature.spectral_bandwidth(y=file, sr=sr, n_fft=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
    return arr_bandwith

def extract_feature():
    sr = 44100
    data = []

    fileInput = 'FileInput/1.wav'

    try:
        file, sr = librosa.load(fileInput, sr)
    except EOFError:
        print("skipped", fileInput)
        
    zcrs = extract_zcr(file)
    scs = extract_sc(file)
    bandwiths = extract_bandwith(file)
    rmses = rmse(file,FRAME_SIZE,HOP_LENGTH)

    size = rmses.size
    
    # print(zcrs.size)
    # print(scs.size)
    # print(bandwiths.size)
    # print(rmses.size)

    for i in range(size):
        curline = [str(zcrs[i]),str(scs[i]),str(bandwiths[i]),str(rmses[i])]
        data.append(curline)
    
    with open("dataInput.csv", 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerows(data)
    return data

if not os.path.isfile("dataInput.csv"):
    print("extracting features...")
    extract_feature()
    print("feature extraction done")
else:
    print("features exist")
