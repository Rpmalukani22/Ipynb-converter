'''
Author : Ruchitesh Malukani
Installation requirements : nbconvert,pandoc,latex(In case of pdf)
'''
import glob
import os
lst=[]
mypath="Path:/To/Parent/Directory" # Paste your path here!
print(mypath)
os.chdir(mypath)
os.system("dir /s /b > myfile.txt")
os.system("notepad "+"myfile.txt")
with open(mypath+"myfile.txt") as f:
    for line in f:
        if line.endswith(".ipynb\n"):
            lst.append(line.strip())
lst=[i.replace('\\','/') for i in lst]
#print(lst[0])
cmd=[('''jupyter nbconvert --to html "%s"'''%f )for f in lst] #For pdf use --to pdf
#print(cmd[0])
[os.system(i) for i in cmd]
