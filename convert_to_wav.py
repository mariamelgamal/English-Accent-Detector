import os
import pandas as pd
import numpy as np
import pydub

from os import path,listdir
from pydub import AudioSegment


# files
# file_path = "cv-valid-dev"
# df = pd.read_csv("cv-valid-dev-acc-mp3.csv")
# sources = np.array(df['filename'])



file_path = "cv-valid-train/"
dst_path = "cv-valid-train-wav/"
files = os.listdir(file_path)

# AudioSegment.converter = "/usr/local/bin/ffmpeg"
# sound = AudioSegment.from_mp3("cv-valid-dev/sample-003058.mp3")
# sound.export("cv-valid-dev-wav/sample-003058.wav", format="wav")

for f in files:
    x = f.split(".")
    dst = dst_path+x[0]+".wav"
    # print(x[0]+".wav")
    # print(dst)

    AudioSegment.converter = "/usr/local/bin/ffmpeg"
    sound = AudioSegment.from_mp3(file_path+f)
    sound.export(dst, format="wav")
    print("exported",x)
