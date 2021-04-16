# realtek-verb-tools
These tools are used for troubleshooting sound issues with Realtek chipsets on Linux.

## cleanverbs
This tool takes output dumped from [a specially modified version of QEMU](https://github.com/jcs/qemu) and removes unnecessary output to leave only Realtek amplifier coefficient  verbs passed through to a sound card connected via VFIO.

Usage: python3 ./cleanverbs.py output-from-qemu-file

**For more information on how to get this QEMU output in the first place, check [my tutorial](https://github.com/ryanprescott/realtek-verb-tools/wiki/How-to-sniff-verbs-from-a-Windows-sound-driver).**

## applyverbs
This tool takes output from cleanverbs and applies each verb to the sound card.

Usage: python3 ./applyverbs.txt output-from-cleanverbs [-d]

The -d flag gives more verbose output and also adds a delay so you can see which verbs are necessary to activate the speakers.
