import os

if not os.path.isfile('Gnrblex_AGS.exe'):
    print('Could not find Gnrblex_AGS.exe.')
    exit(1)

with open('Gnrblex_AGS.exe', 'rb+') as f:
    f.seek(0x48C8214)
    # Replace b'Please stop Please stop ' with
    #         b'Stop that!  Stop that!  '
    f.write(b'Stop that!\x00\x00Stop that!\x00\x00')
    f.close()
    print('Gnrblex_AGS.exe has been patched.')
