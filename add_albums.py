import json
from operator import itemgetter

def record_album_name(album_name):
    data[album_name] = {
        "Artist": "",
        "Cover": "",
        "Date": "",
        "Rating": -1,
        "Link": ""
    }
    return 1

def add_titles():
    exit = False
    while(exit != True):
        album_name = input("album name: ")
        if(album_name == "/"):
            exit = True
        else:
            record_album_name(album_name)
        with open(file_name, "w") as out:
            json.dump(data, out, indent=4)

def fix_formating():
    for key, value in data.items():
        value["Rating"] = int(value["Rating"])
    with open(file_name, "w") as out:
        json.dump(data, out, indent=4)

def fill_in_data():
    for key, value in data.items():
        print(key.capitalize()+":\n")
        for k, v in value.items():
            match k:
                case "Artist":
                    if(v==""):
                        i = input("\nartist:")
                        if(i!="/"):
                            value[k]=i
                case "Cover":
                    if(v==""):
                        i = input("\ncover:")
                        if(i!="/"):
                            value[k]=i
                case "Rating":
                    if(v==-1):
                        i = input("\nrating:")
                        if(i!="/"):
                            value[k]=int(i)
                case "Date":
                    if(v==""):
                        i = input("\ndate:")
                        if(i!="/"):
                            value[k]=i
                case "Link":
                    if(v==""):
                        i = input("\nlink:")
                        if(i!="/"):
                            value[k]=i
        with open(file_name, "w") as out:
            json.dump(data, out, indent=4)

def sort():
    pass


def start():
    i = input("what are you doing?\n(1)inputing titles\n(2)fix formating\n(3)fill in data\n(4)sorting\n")
    match i:
        case "1":
            add_titles()
        case "2":
            fix_formating()
        case "3":
            fill_in_data()
        case "4":
            sort()
        case _:
            print("no input matched")
            start()

file_name = "DATA/album_recs.json"

file = open(file_name)
data = json.load(file)

start()

