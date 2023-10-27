# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:38:22 2023

@author: D
"""
import wmi
import os
import sys
import json
from pprint import pprint
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from zipfile import ZipFile
import shutil

def get_fs_info():
    tmplist = []
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                tmpdict = {}
                tmpdict["DeviceID"] = logical_disk.DeviceID
                tmpdict["FileSystem"] = logical_disk.FileSystem
                tmpdict["DiskTotal"] = round(int(logical_disk.Size) / (1024 * 1024 * 1024), 2)
                tmpdict["FreeSpace"] = round(int(logical_disk.FreeSpace) / (1024 * 1024 * 1024), 2)
                tmpdict["VolumeName"] = logical_disk.VolumeName
                
                tmplist.append(tmpdict)
    return tmplist

def system_info():
    for disks in get_fs_info():
        for key, value in disks.items():
                print(key, ":         ", value)
        print("")


def create_file():
    print("File name:")
    a = input()
    my_file = open(a+".txt", "w+")
    my_file.close()
    
def write_file():
    print("Write in file name:")
    a = input()
    my_file = open(a+".txt", "a+")
    print("Input into file:")
    b = input()
    my_file.write(b+"\n")
    my_file.close()
    
def read_file():
    print("Read file name:")
    a = input()
    if (os.path.isfile(a+".txt") == 0):
        print("No such file")
    else:
        my_file = open(a+".txt", "r+")
        file_contents = my_file.read()
        my_file.close()
        print(file_contents)

def delete_file():
    print("Delete file name:")
    a = input()
    my_file = a+".txt"
    if (os.path.isfile(my_file) == 0):
        print("No such file")
    else:
        os.remove(my_file)
        print(my_file + " deleted")
        
def switch(file):
    if file == "1":
       create_file()
    elif file == "2":
       write_file()
    elif file == "3":
       read_file()
    elif file == "4":
       delete_file()
    elif file == "5":
        return main()    
    main()
    
    
def create_json():
    jsonString=json.dumps([{'pet':{'species':'dog'}},{'pet':{'species':'house_cat','name':'Murka','age':4.5}}],separators=(',', ':'))

    print(jsonString)    
    with open('test.json', 'w') as f:
        f.write(json.dumps(jsonString))
    
def add_json():
    new_j_obj = [{"pet":{"species":"clownfish","name":"Nemo","age":0.3}}]
    with open("test.json", "r") as my_file:
        test_json = my_file.read()
    test_json = test_json.replace("\\", "")
    str_new_obj = json.dumps(new_j_obj)
    test_json = test_json[1:-2] + "," + str(str_new_obj)[1:]
    with open("test.json", "w") as my_file:
        my_file.write(test_json)

def read_json():
    with open("test.json", "r") as my_file:
        test_json = my_file.read()
    print(test_json)
    pprint(test_json, width=1, compact=True)

def delete_json():
    print("Delete test.json?\n1: Yes    AnyOther: No")
    a = input()
    if (int(a)==1):
        if (os.path.isfile("test.json") == 0):
            print("No such file")
        else:
            os.remove("test.json")
            print("test.json deleted")
    else:
        print("Aborted deletion")
        main()
        
def switch_JSON(json):
    if json == "1":
       create_json()
    elif json == "2":
       add_json()
    elif json == "3":
        read_json()
    elif json == "4":
        delete_json()
    elif json == "5":
        return main()
    main()
    

def create_xml():
    items = [
    {"first_name": "Ivan", "last_name": "Ivanov", "city": "Moscow"},
    {"first_name": "Sergey", "last_name": "Sidorov", "city": "Sochi"},
]
    root = ET.Element('root')
    for i, item in enumerate(items, 1):
        person = ET.SubElement(root, 'person' + str(i))
        ET.SubElement(person, 'first_name').text = item['first_name']
        ET.SubElement(person, 'last_name').text = item['last_name']
        ET.SubElement(person, 'city').text = item['city']
    tree = ET.ElementTree(root)
    tree.write('test.xml')
        
def add_xml():
    new_items = {"species": "house_cat", "name": "Murka", "age": "4.5"}
    tree = ET.parse("test.xml")
    xmlRoot = tree.getroot()
    child = ET.Element("pets")
    xmlRoot.append(child)
    g_child = ET.SubElement(child, "cat")
    ET.SubElement(g_child, 'species').text = new_items['species']
    ET.SubElement(g_child, 'name').text = new_items['name']
    ET.SubElement(g_child, 'age').text = new_items['age']    
    tree.write("test.xml")

def read_xml():
    with open('test.xml', 'r') as f:
        data = f.read()
    bs_data = BeautifulSoup(data, 'xml')
    print(bs_data.prettify())
    
def delete_xml():
    print("Delete test.xml?\n1: Yes    AnyOther: No")
    a = input()
    if (int(a)==1):
        if (os.path.isfile("test.xml") == 0):
            print("No such file")
        else:
            os.remove("test.xml")
            print("test.xml deleted")
    else:
        print("Aborted deletion")
        main()    
        
def switch_XML(xml):
    if xml == "1":
       create_xml()
    elif xml == "2":
       add_xml()
    elif xml == "3":
       read_xml()
    elif xml == "4":
       delete_xml()
    elif xml == "5":
        return main()    
    main()
    

def create_zip():
    my_file = open("file.txt", "w+")
    my_file.write("Did you ever hear the tragedy of Darth Plagueis the Wise?")
    my_file.close()
    my_file = open("another_file.txt", "w+")
    my_file.write("I thought not. It's not a story the Jedi would tell you. It's a Sith legend.")
    my_file.close()
    with ZipFile('test.zip', 'w') as myzip:
        myzip.write('file.txt')
        myzip.write('another_file.txt')

def add_zip():
    my_file = open("continuation.txt", "w+")
    my_file.write("Darth Plagueis... was a Dark Lord of the Sith so powerful and so wise, he could use the Force to influence the midi-chlorians... to create... life. He had such a knowledge of the dark side, he could even keep the ones he cared about... from dying.")
    my_file.close()
    with ZipFile("test.zip", mode="a") as archive:
        archive.write("continuation.txt")

    
def read_zip():
      with ZipFile("test.zip", mode="r") as archive:
        archive.extract("file.txt", path="dearchived from 'test.zip'/")
      with ZipFile("test.zip", mode="r") as archive:
          info = archive.getinfo("file.txt")
      print(f"File size: {info.file_size}")
      print(f"Compress size: {info.compress_size}")
      print(f"Date time: {info.date_time}")
      print(f"Filename: {info.filename}")
      
      
def delete_zip():
    print("Delete test.zip?\n1: Yes    AnyOther: No")
    a = input()
    if (int(a)==1):
        if (os.path.isfile("test.zip") == 0):
            print("No such file")
        else:
            os.remove("test.zip")
            print("test.zip deleted")
    else:
        print("Aborted deletion")
    print("Delete folder 'dearchived from 'test.zip''?\n1: Yes    AnyOther: No")
    a = input()
    if (int(a)==1):
        if (os.getcwd() +"\dearchived from 'test.zip'" == 0):
            print("No such directory")
        else:
            shutil.rmtree(os.getcwd() +"\dearchived from 'test.zip'",ignore_errors=True)
            print("folder 'dearchived from 'test.zip'' deleted")
    else:
        print("Aborted deletion") 
        main()

def switch_ZIP(zip_f):
    if zip_f == "1":
       create_zip()
    elif zip_f == "2":
       add_zip()
    elif zip_f == "3":
       read_zip()
    elif zip_f == "4":
       delete_zip()
    elif zip_f == "5":
        return main()    
    main()
        
    
def menu(point):
    if point == "1":
       system_info()
    elif point == "2":
        print("1    -   Create file:\n2    -   Write into file\n3    -   Read file\n4    -   Delete file\n5    -   Main menu\n")
        switch(input())
    elif point == "3":
        print("1    -   Create JSON file:\n2    -   Write into JSON file\n3    -   Read JSON file\n4    -   Delete JSON file\n5    -   Main menu\n")
        switch_JSON(input())
    elif point == "4":
        print("1    -   Create XML file:\n2    -   Write into XML file\n3    -   Read XML file\n4    -   Delete XML file\n5    -   Main menu\n")
        switch_XML(input())
    elif point == "5":
        print("1    -   Create zip archive:\n2    -   Add file into archive\n3    -   Dearchive and get info about file\n4    -   Delete archive and file\n5    -   Main menu\n")
        switch_ZIP(input())
    elif point == "6":
        sys.exit(0)
    main()
    
def main():
    print("\nAction:\n1:   Local disks information\n2:   Files\n3:   JSON\n4:   XML\n5:   zip\n6:   Exit")
    menu(input())
    
if __name__ == '__main__':
    main()