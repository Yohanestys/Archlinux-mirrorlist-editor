#!/usr/bin/env python

from urllib import request

def generated_mirrorlist():
    page = request.urlopen("https://archlinux.org/mirrorlist/all/")
    new_file = ""

    for file in page:
        new_file += file.decode("UTF-8").strip("\n")
        new_file += "\n"

    return new_file
#print(new_file)

