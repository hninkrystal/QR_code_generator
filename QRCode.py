from sys import platform
import os
import qrcode

def qrcodegenerator(input_string, file_name='qr_code.png'): #function for generating qr code
    qr = qrcode.QRCode(
        version=1, #controlling the size of the qrcode
        box_size=10, #size of box where qrcode is drawn in
        border=4, #border thickness
    )
    
    qr.add_data(input_string) #add string to the qrcode
    qr.make(fit=True) #adjust the qrcode size
    
    image = qr.make_image(fill='black', back_color='white') #create image from qrcode
    image.save(file_name) #save image to a file
    print(f"QR code is generated and saved as {file_name}")
input_String = "https://github.com"
if platform == "linux" or platform == "linux2":
    qrcodegenerator(input_String, "./QRCode.png")
elif platform == "win32":
    current_directory = os.getcwd()
    qrcodegenerator(input_String, current_directory + "\\QRCode.png")

