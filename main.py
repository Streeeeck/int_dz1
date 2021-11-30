import sys
import json
import zipfile
import os
import psutil
import pandas as pd
import numpy as np
from zipfile import ZipFile
import datetime

def disk_info():
    for part in psutil.disk_partitions(all=False):
        s = psutil.disk_usage(part.mountpoint)
        print(
            part.device,
            "total "+str(int(s.total/1000000000))+" GB",
            "used  "+str(int(s.used/1000000000))+" GB",
            "free  "+str(int(s.free/1000000000))+" GB",
            "type  "+str(part.fstype),
            sep="\n\t"
        )

def file_moves():
    file_name = "test.txt"
    s = input()
    with open(file_name, "w") as f:
        f.write(s)
    with open(file_name, "r") as f:
        print(f.read())
    try:
        os.remove(file_name)
    except Exception as ex:
        print(str(ex))
    else:
        print("success!")
def json_moves():
    file_name = "test.json"
    d = {
        "a": 1,
        "b": [1],
        "c": "1"
    }

    with open(file_name, "w") as f:
        json.dump(d, f)
    with open(file_name, "r") as f:
        print(json.load(f))
    try:
        os.remove(file_name)
    except Exception as ex:
            print(str(ex))
    else:
        print("success!")

def xml_moves():
    file_name = "test.xml"
    df = pd.DataFrame(np.random.randn(4, 3), columns=["a", "b", "c"])
    print(df)

    df.to_xml(file_name, index=None)
    df = pd.read_xml(file_name)

    row = []
    for col in df.columns:
        row.append(input(col))

    df = df.append(pd.DataFrame([row], columns=df.columns, index=[df.index.stop]), ignore_index=False)
    df.to_xml(file_name, index=None)
    print(df)

    try:
        os.remove(file_name)
    except Exception as ex:
        print(str(ex))
    else:
        print("success!")

def zip_moves():
    file_name = "files.zip"
    file_paths = ["1.txt", "2.txt", "3.txt"]

    for file in file_paths:
        with open(file, "w") as f:
            f.write(file)
    with ZipFile(file_name, 'w') as zip:
        for file in file_paths:
            zip.write(file)
    file_name = file_name

    with ZipFile(file_name, 'r') as zip:
        for info in zip.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t' + "Windows" if str(info.create_system) else "Unix")
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')
if __name__ == '__main__':
    # disk_info()
    # file_moves()
    # json_moves()
    # xml_moves()
    zip_moves()
