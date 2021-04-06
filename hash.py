import os
import hashinfunc


unhashables = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]
for dirpath, dirs, files in os.walk("/"):
    for filename in files:
        fname = os.path.join(dirpath,filename)
        hashedFile = None
        
        with open(fname) as myfile:
            try:
                hashedFile = hashinfunc.hashFile(myfile.read())
                print(hashedFile)
            except Exception as e:
                print(e)
            finally:
            	pass
            
            
