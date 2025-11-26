import os
import shutil

def outdated(src, dst):
    try:
        dtime = os.path.getmtime(dst)
    except OSError:
        return True
    return dtime < os.path.getmtime(src)

if outdated(src := "src/index.html", dst := "docs/index.html"):
    shutil.copyfile(src, dst)
