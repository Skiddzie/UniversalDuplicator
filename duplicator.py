import os
while(True):
    barcode = input(">")
    template = """

    ^XA
    ^CF0,60
    ^F(C100,100,255,255,N,1,0,0,0,0
    ^FO0,0^FR^GB1000,56,30^FS

    ^CFA,40
    ^F(C0,0,0,255,Y,100,100,255,255,0
    ^FO150,5^FDProperty Of My Library^FS

    ^CFA,30


    ^BY3,2,150
    ^FO160,120^BC^FD"""+barcode+"""^FS

    ^XZ

    """

    print(template)
    with open(r'zpl.txt', 'w') as f:
        f.write(template)
    os.startfile(r"zpl.txt", "print")