import os
from zplTemplate import templateFill

while(True):
    barcode = input(">")
    template = templateFill(barcode)

    print(template)

    with open(r'zpl.txt', 'w') as f:
        f.write(template)
    os.startfile(r"zpl.txt", "print")