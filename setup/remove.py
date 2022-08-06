import subprocess
import nltk
import os, sys


punkt_path = next(p for p in nltk.data.path if os.path.exists(p))

def delete(isDir, path):
    args = ["rm", path]
    if isDir:
        args = ["rm", "-r", path]

    return_code = ""
    try: 
        return_code = subprocess.check_call(args)
    except:
        pass
    if return_code == 0:
        print("Successfully deleted: " + path)
    else:
        print("Delete failed")
    

def uninstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package])

delete(False, os.path.join(punkt_path, "tokenizers", "punkt.zip"))
delete(True, os.path.join(punkt_path, "tokenizers", "punkt"))
uninstall("Flask")
uninstall("newspaper3k")
uninstall("google-search-results")