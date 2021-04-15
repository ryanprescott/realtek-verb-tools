import sys
import re

if (len(sys.argv) == 1):
    print("Usage: ./cleanverbs.py [path_to_qemu_dump]")
    exit()

try:
    f = open(sys.argv[1], "r")
except Exception as e:
    print(str(e))
    exit()

raw_verbs = f.read()
corb_matches = re.findall('caddr:(0x[0-9a-f]+) nid:(0x[0-9a-f]+) control:(0x[0-9a-f]+) param:(0x[0-9a-f]+)( response:(0x[0-9a-f]+)|)', raw_verbs);

for corb_match in corb_matches:
    nid = int(corb_match[1], 16)
    control = int(corb_match[2], 16)
    param = int(corb_match[3], 16)
    if nid == 0x20 and control >= 0x400 and control <= 0x5ff:
        print(corb_match[1] + ' ' + corb_match[2] + ' ' + corb_match[3])

f.close()