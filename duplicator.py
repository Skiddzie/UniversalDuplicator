import os

barcode = input(">")
template = """^XA
^CF0,60

^F(C255,0,0,255,N,0,0,0,0,0
^FO50,50^GB100,100,100^FS
^F(C0,0,255,255,N,0,0,0,0,0
^FO75,75^FR^GB100,100,100^FS
^F(C255,255,0,255,N,0,0,0,0,0
^FO93,93^GB40,40,40^FS
^FO220,50^FDEpson ZPL with Color Image Example^FS
^CF0,30
^FO220,115^FD1000 Shipping Lane^FS
^FO220,155^FDShelbyville TN 38102^FS
^FO220,195^FDUnited States (USA)^FS
^FO50,250^GB500,3,3^FS
^CFA,30
^FO50,300^FDJane Smith^FS
^FO50,340^FD100 Main Street^FS
^FO50,380^FDSpringfield TN 39021^FS
^FO50,420^FDUnited States (USA)^FS
^PQ1,0,1,Y

^BY5,2,270
^FO100,550^BC^FD"""+barcode+"""^FS

^XZ"""

print(template)
with open(r'zpl.txt', 'w') as f:
    f.write(template)
os.startfile(r"zpl.txt", "print")