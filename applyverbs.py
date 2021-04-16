import subprocess
import os
import sys
import time
def validate(verbstring):
    try:
        verbsegments = verbstring.split(' ')
        int(verbsegments[0], 16) and int(verbsegments[1], 16) and int(verbsegments[2], 16)
        return verbsegments
    except Exception as e:
        print('One or more verb strings was invalid.')
        exit()   
if os.geteuid() != 0:
    print('You must run this script with sudo.')
    exit()
if len(sys.argv) == 1:
    print('Usage: ./applyverbs.py path_to_verbs [-d]')
    print('   -d:\tDebug mode. Adds a delay and prints verbs')
    exit()
try:
    f = open(sys.argv[1], 'r')
except Exception as e:
    print(str(e))
    exit()
debug = sys.argv.__contains__('-d')
verbstrings = f.read().splitlines()
verbsegments = list(map(validate, verbstrings))
f.close()
print('Applying verbs...')
for i in range(0, len(verbsegments)):
    segment = verbsegments[i]
    args = ['hda-verb', '/dev/snd/hwC0D0', *segment]
    result = subprocess.run(args, stderr=subprocess.DEVNULL, stdout=subprocess.PIPE).stdout.decode('utf-8')
    response = result[8:len(result)-1]
    if response == '0xffffffff':
        print('Fatal error: the codec is unresponsive. Please reboot the machine and try again.')
        exit()
    if debug:
        print('[' + str(i+1) + ']\t' + segment[0] + ' ' + segment[1] + ' ' + segment[2] + '\t' + '(' + response + ')')
        time.sleep(0.1)
print('Verbs applied!')
