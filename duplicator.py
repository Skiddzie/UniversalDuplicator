import os
import keyboard
from zplTemplate import templateFill
while(True):
    barcode = ""
    while True:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
            break  # Exit the loop when 'enter' is pressed
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name != 'enter':
                # Append the key's name to the barcode string
                barcode += event.name

    print("Barcode:", barcode)

    
    template = templateFill(barcode)

    print(template)

    with open(r'zpl.txt', 'w') as f:
        f.write(template)
    os.startfile(r"zpl.txt", "print")