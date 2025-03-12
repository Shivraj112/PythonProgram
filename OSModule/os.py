import os
f = os.open("myfile.txt",os.O_RDONLY)
contents = os.read(f,1024)
os.close(f)