import os 
import sys
import json  
import shutil  
from subprocess import PIPE, run 

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You have to pass a source and target directory")
    
    source, target = args[1:]
    main(source, target)