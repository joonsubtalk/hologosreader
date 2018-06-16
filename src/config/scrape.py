# scaffold for CRA 1.0
import sys
import os, errno
from lxml import html
import requests
import subprocess

## ----------------------------------
## HELPERS
## ----------------------------------
def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

def renameReplaceFile(output, original):
    silentremove(original)
    os.rename(output, original)

def removeChars(chr, str):
    return str.replace(chr, "")

def removeCharList(arr, str):
    newStr = str
    for char in arr:
        newStr = removeChars(char, str)
    return newStr

## ----------------------------------

books = [ 'Judges',
'Micah',
'Proverbs',
'Revelation',
'Deuteronomy',
'Haggai',
'3 John',
'1 Kings',
'Mark',
'Matthew',
'1 Thessalonians',
'Daniel',
'Malachi',
'Colossians',
'Ruth',
'Genesis',
'2 Samuel',
'Obadiah',
'Esther',
'Exodus',
'Jeremiah',
'Ephesians',
'Habakkuk',
'Luke',
'Song of Solomon',
'Jonah',
'Acts',
'Job',
'Titus',
'2 Timothy',
'James',
'2 John',
'Isaiah',
'2 Thessalonians',
'1 Chronicles',
'1 Timothy',
'Leviticus',
'1 Peter',
'Psalms',
'Zephaniah',
'Joel',
'Nahum',
'Jude',
'2 Chronicles',
'Hosea',
'Zechariah',
'Nehemiah',
'John',
'1 John',
'Lamentations',
'Amos',
'1 Samuel',
'Joshua',
'1 Corinthians',
'Ezra',
'Romans',
'2 Corinthians',
'Hebrews',
'Ezekiel',
'2 Peter',
'Philippians',
'Numbers',
'Philemon',
'Galatians',
'2 Kings',
'Ecclesiastes']

rmchar = [
    '"',
    ':',
    '{'
]
cnt = 0

# with open('ESV.js', 'r') as input_file, open('ESV_count.js', 'w') as output_file:
#     for line in input_file:

#         removeCharList(rmchar,line)

#         if line.strip() == books[cnt]:
#             output_file.write(books[cnt] + '\n')
#             cnt+=1
#         else:
#             # line "11": {
#             idx = line.find(':')

#             if line[idx+2] == '{':
#                 output_file.write(line)
#             else:
#                 justTheVerse = line[idx+3:len(line)-3]
#                 output_file.write(str(len(justTheVerse))+'\n')

# jchun1390
# Mv90/OFW

# just cont
with open('ESV_count.js', 'r') as input_file, open('ESV_cond.js', 'w') as output_file:
    vcnt = 0
    for line in input_file:

        # removeCharList(rmchar,line)
        if line.strip().isdigit():
            vcnt += int(line)
        else:
            if vcnt > 0:
                output_file.write(str(vcnt) + '},\n'+str(line)+'\n')
            else :
                output_file.write(line+'\n')
            vcnt = 0

## ----------------------------------
