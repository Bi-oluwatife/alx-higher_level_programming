#!/usr/bin/python3
import sys
len = len(sys.argv) - 1
if len == 0:
    print("{} arguments.".format(len))
elif len > 0:
    word = 1
    print("{} arguments:".format(len))
    while word <= len:
        print("{}: {}".format(word, sys.argv[word]))
        word +=1
