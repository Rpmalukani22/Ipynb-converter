import glob
import os
lst=[]
mypath="C://Users//Ruchitesh//Desktop//ML stuff//Applied AI ipynb"
with open("C://Users//Ruchitesh//Desktop//ML stuff//Applied AI ipynb//myfile.txt") as f:
    for line in f:
        if line.endswith(".ipynb\n"):
            lst.append(line.strip())
lst=[i.replace('\\','/') for i in lst]
#print(lst[0])
cmd=[('''jupyter nbconvert --to html "%s"'''%f )for f in lst]
#print(cmd[0])
[os.system(i) for i in cmd]
