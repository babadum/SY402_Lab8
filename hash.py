import os
import hashinfunc


unhashables = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/run", "/var/lib"]
for dirpath, dirs, files in os.walk("/"):
    for filename in files:
        fname = os.path.join(dirpath,filename)
        hashedFile = None
        #print(dirpath)
        if not dirpath in unhashables:
            try:
                #with open(fname) as myfile:
                try:
                    print(dirpath)

                    hashedFile = hashinfunc.hashFile(fname)
                    print(hashedFile)
                except Exception as e:
                    print(e)
                finally:
                   pass
            except Exception as e:
                print(e)
            finally:
                pass
        else:
            break
            
            
