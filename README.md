# Project_Costomized_QR_Code_Generator
This script helps you create QR codes with your own logo and color. You enter the logo file, the URL you want to encode, and the color for the QR code. It handles errors like missing files or bad color choices. Finally, it saves the customized QR code with a name you choose.



Features:-
High Error Correction: The QR code is generated with high error correction capability (30%) using the ERROR_CORRECT_H setting. This means that up to 30% of the QR code can be obscured (e.g., by a logo) without affecting its ability to be scanned.

Logo Integration: You can embed a logo or image within the QR code. The tool automatically resizes the logo to ensure it fits well within the QR code without compromising its readability.

Customizable Colors: Choose any color for your QR code to better suit your needs, making it more visually appealing or consistent with your brand identity.

Error Handling: The script includes multiple checks and error-handling mechanisms to guide you through the process, ensuring that issues like incorrect file paths or unsupported image formats are managed gracefully.




Requirements:-
To run this project, you'll need:

Python 3.x: The script is written in Python, so you need Python installed on your computer.

qrcode: This library is used to generate QR codes. You can install it using the following command:

bash
Copy code
pip install qrcode[pil]
Pillow: A Python Imaging Library (PIL), which is used to handle image files (e.g., your logo). Install it with:


How It Works
Logo Support:

The tool supports various image formats (e.g., PNG, JPEG) for your logo.
When you input the logo file path, the tool attempts to open the image and convert it to a format suitable for embedding within the QR code.
If the logo is too large, the tool automatically resizes it. The resizing ensures that the logo does not occupy more than 20% of the QR code's area, maintaining the balance between customization and scannability.
Error Handling:

File Not Found: If you enter a file path that doesn't exist, the tool will notify you and prompt you to check the file path.
Invalid Image: If the file isn't a valid image, the tool will alert you and ask for a correct image file.
Empty URL/Text: The script checks if the URL or text input is empty and will prompt you to enter valid data.
Invalid Color: If you choose a color that isn't recognized, the tool will notify you to choose a valid color name.
Saving the QR Code:

After creating the QR code and embedding the logo, the tool asks for a file name to save the final image.
The output file is saved in PNG format, ensuring compatibility with various applications and platforms.
Step-by-Step Usage
Run the Script:

Use the command line to navigate to the directory where the script is located.
Run the script with the following command:



Provide the Logo File Path:

Enter the full path to your logo image. Make sure the path is correct to avoid errors.
Enter the URL or Text:

Input the URL or text you want the QR code to contain. This could be a website link, contact information, or any other data.
Choose a QR Code Color:

Enter a color name (e.g., black, blue, red). This color will be used for the QR code.
Save the QR Code:

Provide a name for the output file. The script will save the QR code as a PNG image with your chosen file name.
Example Walkthrough
Let's say you have a logo at C:\Users\YourName\Images\logo.png, and you want to create a QR code for https://example.com with a blue color. Here’s how the interaction would look:




Enter the file path for the logo: C:\Users\YourName\Images\logo.png
Enter the URL or text for the QR code: https://example.com
Enter the QR code color: blue
Enter the output file name (without extension): my_custom_qr
QR code saved as my_custom_qr_QR.png
The final image, my_custom_qr_QR.png, will be stored in the directory from which you ran the script.

Troubleshooting
File Not Found: Double-check the path to your logo file. Make sure it’s typed correctly, including the extension (e.g., .png).
Color Issues: Ensure the color you specify is a recognized name (e.g., red, blue, green). If you're unsure, refer to standard color names supported in web design.
QR Code Not Scanning: If the QR code doesn't scan, ensure the logo isn't too large, and try a more contrasting color combination (e.g., dark QR code on a white background).
