"""
VCF_TO_DAT_S30.py
Convert vCards into suitable for Nokia Series 30+ format.
Inpired by:
https://gist.github.com/in4lio/1e16ead4ebe459919ae6551544cc3b22

The MIT License (MIT)
Copyright (c) 2017 mahdi0khosravi@gmail.com
"""

import sys
import os

CARD = """
BEGIN:VCARD
VERSION:2.1
FN:%s
TEL;VOICE;CELL:%s
END:VCARD"""

class contact():
    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone

with open("./contacts.vcf") as f:
    lines = f.readlines()

    name  = ""
    telephone = ""
    contacts = []
    for line in lines:
        line = line[:-1]

        if "BEGIN:VCARD" in line:
            name = ""
            telephone = ""
        elif "FN" in line:
            name = line.split(":")[1]
        elif "TEL" in line:
            telephone = line.split(":")[1]
        elif "END:VCARD" in line:
            contacts.append(contact(name, telephone))

for item in contacts:
    print(CARD % (item.name, item.telephone))
