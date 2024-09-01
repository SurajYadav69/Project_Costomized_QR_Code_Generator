# Project_Costomized_QR_Code_Generator
This script helps you create QR codes with your own logo and color. You enter the logo file, the URL you want to encode, and the color for the QR code. It handles errors like missing files or bad color choices. Finally, it saves the customized QR code with a name you choose.


How It Works
Enter the Logo File Path: The script asks you to provide the file path to the logo you want to use.

Handle Errors: If the logo file is missing or there’s another issue, the script will show an error message and stop.

Resize the Logo: The script resizes the logo to fit nicely on the QR code.

Input URL: You’ll be asked to enter the URL or text you want the QR code to link to.

Choose QR Code Color: You can pick the color you want for the QR code. If the color is not valid, the script will alert you.

Generate the QR Code: The script creates the QR code with the logo and color you’ve chosen.

Save the QR Code: You’ll enter a name for the file, and the script will save the QR code image with your logo.

Code Explanation
Import Modules: The script uses qrcode to create QR codes and PIL to handle images.

Open Logo: The script opens the logo image from the path you provide. If it can’t find the file, it shows an error.

Resize Logo: It resizes the logo to a fixed width while keeping its original proportions.

Create QR Code: A QR code object is created with high error correction to ensure it’s readable even if the logo partially covers it.

Add Data: The URL or text you provide is added to the QR code.

Set Color: The QR code is colored based on your choice. If the color is not valid, it shows an error message.

Paste Logo: The resized logo is placed in the center of the QR code.

Save Image: Finally, the script saves the QR code image with the name you provide.

Usage
Run the script.
Follow the prompts to enter the logo file path, URL, and color.
Enter the file name for saving the QR code.
Example
If you enter:

Logo path: logo.png
URL: https://example.com
Color: blue
File name: my_qr
The script will generate a QR code with the provided logo, color it blue, and save it as my_qr_QR.png.
