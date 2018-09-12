import os
import sys


word = sys.argv[1]
home_dir = os.environ['HOME']
with open(home_dir+'/.local/share/qutebrowser/userscripts/ejdict/EJDict/src/ejdic-hand-utf8.txt') as lines:
    for line in lines:
        if line.startswith(word+'\t'):
            print(line)
            break
    else:
        sys.exit(1)
