import os
import hashinfunc

for dirpath, dirs, files in os.walk("/"):
    for filename in files:
        fname = os.path.join(dirpath,filename)
        with open(fname) as myfile:
            hashFile(myfile.read())
            
