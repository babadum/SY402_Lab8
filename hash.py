import os
import hashinfunc

for dirpath, dirs, files in os.walk("/"):
    for filename in files:
        fname = os.path.join(dirpath,filename)
        hashedFile = None
        with open(fname) as myfile:
            try:
                hashedFile = hashinfunc.hashFile(myfile.read())
            except:
                print("error hashing")
            print(hashedFile)
            
