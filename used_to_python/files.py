#! usr/bin/env python3
words = ["potato","patata","sss","zzzz"]

files = open("iwascreatedwithpy.txt","w")
files.writelines(words + "\n")
files.close()
