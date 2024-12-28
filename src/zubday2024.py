#!/usr/bin/env python3
#zubday2024.py

import math
import re

code = re.findall( 
    '[1-' + str(int(math.tau)) + ']',
    str(round(math.pi, 6))
)

magic_number = int(code[int(True)])

del code[magic_number]

code = ''.join(code)

magic_string = re.sub(
    '[^\\d]',
    '',
    str(
        (math.tau / math.pi) / 1000
    )
)

code = code + '1'

code = (
    str(6 - magic_number)
    + str(int(magic_string))
    + str(6)
    + magic_string
    + code
)

print(code)

