from Analyses.syntax import analyse
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if os.path.exists(filename):
            analyse(filename)
        else:
            print("File not exists!")
    else:
        print("Usage: python main.py <filename>")