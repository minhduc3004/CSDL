import numpy as np
import librosa
import glob
import csv
import os.path


labels = {}
samples = {}
FRAME_SIZE = 1024
HOP_LENGTH = 512
sr=44100
def get_instrument_name(path):
    return path.split('\\')[1]


def generate_label():
    dirs = glob.glob('data/*')
    count = 0
    for dirname in dirs:
        ins = get_instrument_name(dirname)
        labels[ins] = count
        samples[ins] = 0
        count += 1
    return labels

def label_names():
    generate_label()
    return labels.keys()


def detect_label(filename):
    ins = get_instrument_name(filename)
    return labels[ins]

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

    files = glob.glob('data/*/*.wav')
    for filename in files:
        try:
            note, sr = librosa.load(filename, sr = None)
        except EOFError:
            print("skipped", filename)
            continue
        
        zcrs = extract_zcr(note)
        scs = extract_sc(note)
        bandwiths = extract_bandwith(note)
        rmses = rmse(note,FRAME_SIZE,HOP_LENGTH)
        size = rmses.size
        
        # print(zcrs.size)
        # print(scs.size)
        # print(bandwiths.size)
        # print(rmses.size)

        label = detect_label(filename)
        for i in range(size):
            curline = [str(zcrs[i]),str(scs[i]),str(bandwiths[i]),str(rmses[i]),label]
            data.append(curline)
    
    with open("data.csv", 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerows(data)
    return data

if not os.path.isfile("data.csv"):
    generate_label()
    print("extracting features...")
    extract_feature()
    print("feature extraction done")
else:
    print("features exist")