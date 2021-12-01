import json
import os
import psutil
from zipfile import ZipFile
import datetime
import xml.etree.ElementTree as xml


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
    s = input("Введите текст для ввода в файл\n")
    with open(file_name, "w") as f:
        f.write(s)
    with open(file_name, "r") as f:
        print(f.read())
    try:
        os.remove(file_name)
    except Exception as ex:
        print(str(ex))
    else:
        print("Файл удален!")
def json_moves():
    file_name = "test.json"
    d = {
        "имя": "Иван",
        "возраст": 20
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
        print("JSON удален!")

def xml_moves():
    file_name = "test.xml"
    root = xml.Element("qwerty")
    d = {
        "name": "Ivan",
        "age": 20
    }
    userElem = xml.SubElement(root, "zxc")
    xml.SubElement(userElem, "name", name=d["name"])
    xml.SubElement(userElem, "Age").text = str(d["age"])
    tree = xml.ElementTree(root)
    tree.write("%s" % file_name)

    with open("%s" % (file_name), "r") as xml_file:
        tree = xml.fromstring(xml_file.read())
        for el in tree.findall('zxc'):
            for ch in list(el):
                if ch.attrib is not None and ch.attrib.get("name") is not None:
                    print("%s %s" % (ch.tag, ch.attrib.get("name")))
                if ch.text is not None:
                    print("%s %s" % (ch.tag, ch.text))

    try:
        os.remove(file_name)
    except Exception as ex:
        print(str(ex))
    else:
        print("XML удален!")

def zip_moves():
    file_name = "arch.zip"
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
    xml_moves()
    # zip_moves()
