import os
import sys


word = sys.argv[1].lower()
us_dir = os.environ['HOME']+'/.local/share/qutebrowser/userscripts'

with open(us_dir+'/ejdict/EJDict/src/ejdic-hand-utf8.txt') as lines:
    for line in lines:
        if line.startswith(word+'\t'):
            print(line)
            sys.exit(0)
with open(us_dir+'/ejdict/EJDict/src/ejdic-hand-utf8.txt') as lines:
    for line in lines:
        # 複数形, 三人称単数形
        if word[-1] == 's':
            if line.startswith(word[:-1]+'\t'):
                print(line)
                break
        if word[-2:] == 'es':
            if line.startswith(word[:-2]+'\t'):
                print(line)
                break
        # 進行形
        if word[-3:] == 'ing':
            if line.startswith(word[:-3]+'\t'):
                print(line)
                break
            elif line.startswith(word[:-3]+'e\t'):
                print(line)
                break
        # 過去形
        if word[-1] == 'd':
            if line.startswith(word[:-1]+'\t'):
                print(line)
                break
        if word[-2:] == 'ed':
            if line.startswith(word[:-2]+'\t'):
                print(line)
                break
    else:
        sys.exit(1)
