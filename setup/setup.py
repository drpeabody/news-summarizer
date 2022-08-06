import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("newspaper3k")
install("Flask")
import nltk
nltk.download('punkt')
