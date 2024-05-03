import os
import time
paths = ["%s %s" % (time.ctime(t), f) for t, f in
         sorted([(os.path.getatime(x),x) for x in os.listdir(".")])]
print("Direcorty listing, sorted by creation date: ")
for x in range(len(paths)):
    print(paths[x])
