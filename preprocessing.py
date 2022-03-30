from pathlib import Path
import os
from posixpath import basename 
import random
import shutil
import cv2


newWidth = 200
newHeight = 200
dim = (newWidth,newHeight)

trainPercent = 0.7
testPercent = 0.15

trainFolder = os.path.join(os.getcwd(),"train")
testFolder = os.path.join(os.getcwd(),"test")
validFolder = os.path.join(os.getcwd(),"valid")



if (os.path.exists(trainFolder)):
    shutil.rmtree(trainFolder)
if (os.path.exists(testFolder)):
    shutil.rmtree(testFolder)
if (os.path.exists(validFolder)):
    shutil.rmtree(validFolder)

subfolders = [ f.path for f in os.scandir(os.getcwd()) if f.is_dir() ]

os.mkdir(trainFolder)
os.mkdir(testFolder)
os.mkdir(validFolder)

for fldr in subfolders:
    files = os.listdir(fldr)
    random.shuffle(files)
    trainCount = round(len(files)*trainPercent)
    testCount = round(len(files)*testPercent)
    newTrainPath = os.path.join(trainFolder,os.path.basename(fldr))
    newTestPath = os.path.join(testFolder,os.path.basename(fldr))
    newValidPath = os.path.join(validFolder,os.path.basename(fldr))
    os.mkdir(newTrainPath)
    os.mkdir(newTestPath)
    os.mkdir(newValidPath)
    for i in range(len(files)):
        fileFullPath = os.path.join(fldr,files[i])
        ext = Path(files[i]).suffix
        print(fileFullPath)
        img = cv2.imread(fileFullPath,cv2.IMREAD_COLOR)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        if (i < trainCount):
            cv2.imwrite(os.path.join(newTrainPath,os.path.basename(fldr) + "_" + str(i) + "train" + ext),resized)
        elif (i < trainCount + testCount):
            cv2.imwrite(os.path.join(newTestPath,os.path.basename(fldr) + "_" + str(i - trainCount) + "test" + ext),resized)
        else:
            cv2.imwrite(os.path.join(newValidPath,os.path.basename(fldr) + "_" + str(i - trainCount - testCount) + "valid" + ext),resized)