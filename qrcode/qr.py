import os

import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
#   version : Size (1 is small , 40 is huge)
#   How big is each "pixel"
#   White border thickness


def menu():
    print(" QR Code Generator ")
    print("1.Url")
    print("2.Wifi Password")
    print("3.Contact Details")
    print("4.Text")
    print("5.Exit")


def getdata():
    while True:
        menu()
        try:
            x = int(input("Enter the choice: "))
        except ValueError:
            print("Error:Please enter a number:")
            continue
        match x:
            case 1:
                return input("Enter the URL: ")
            case 2:
                ssid = input("Enter SSID:")
                password = input("Password: ")

                data = f"WIFI:S:{ssid};T:WPA;P:{password};;"
                return data
            case 3:
                f_name = input("First Name: ")
                l_name = input("Last name: ")
                phone = input("Phone No: ")
                email = input("Email: ")
                data = f"BEGIN:VCARD\nVERSION:3.0\nN:{f_name};{l_name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
                return data
            case 4:
                return input("Enter any text: ")
            case 5:
                exit(1)
            case _:
                return "I Love You"


def qr_to_ascii(qr):
    border_size = 2
    width = border_size * 2 + len(qr.modules[0])
    # top border
    for _ in range(border_size):
        print("██" * width)

    for row in qr.modules:
        # left border
        print("██" * border_size, end="")
        for cell in row:
            # if cell: # non inverted
            #     print("██", end="")
            # else:
            #     print("  ", end="")
            # inverted
            if cell:
                print("  ", end="")
            else:
                print("██", end="")
        # right border
        print("██" * border_size)
    # bottom border
    for _ in range(border_size):
        print("██" * width)


qr.add_data(getdata())
qr.make(fit=True)

display_ascii = False
save_png = False

x = int(input("How to display?\n1.Ascii\n2.Save PNG\n3.Both\nChoice: "))

match x:
    case 1:
        # qr.print_ascii(invert=True)
        display_ascii = True
    case 2:
        save_png = True
    case 3:
        display_ascii = True
        save_png = True

if display_ascii:
    qr_to_ascii(qr)
if save_png:
    # img = qr.make_image(fill_color="red", back_color="white")
    img = qr.make_image()
    img.save("myqr.png")
    print(f"Success! Saved at {os.path.join(os.getcwd(),"myqr.png")}")
