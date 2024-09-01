# Project_Costomized_QR_Code_Generator
This script helps you create QR codes with your own logo and color. You enter the logo file, the URL you want to encode, and the color for the QR code. It handles errors like missing files or bad color choices. Finally, it saves the customized QR code with a name you choose.



## 🚀 **Features:**

- **High Error Correction**: QR code can be 30% obscured (e.g., by a logo) and still work.
- **Logo Integration**: Automatically resizes your logo to fit within the QR code.
- **Customizable Colors**: Choose any color to match your branding.
- **Error Handling**: Alerts for missing files, invalid images, or bad color choices.

---

## 📋 **Requirements:**

- **Python 3.x**
- **qrcode**: Install with `pip install qrcode[pil]`
- **Pillow**: Install with `pip install pillow`

---

## 🛠️ **How It Works:**

- **Logo Support**: Accepts various image formats (e.g., PNG, JPEG).
- **Error Handling**:
  - *File Not Found*: Alerts you if the file path is incorrect.
  - *Invalid Image*: Prompts for a valid image if necessary.
  - *Empty URL*: Ensures the URL/text is provided.
  - *Invalid Color*: Notifies if the color name is unrecognized.

- **Saving the QR Code**: Saves as a PNG file with the name you choose.

---

## 📌 **Step-by-Step Usage:**

1. **Run the Script**:
   - Use the command line to navigate to the script's directory.
   - Run with `python script_name.py`.

2. **Provide the Logo File Path**:
   - Enter the correct file path for your logo image.

3. **Enter the URL or Text**:
   - Input the URL or text to encode in the QR code.

4. **Choose a QR Code Color**:
   - Enter a color name (e.g., `black`, `blue`).

5. **Save the QR Code**:
   - Provide a file name; the QR code will be saved as a PNG.

---

## 📝 **Example**:

```plaintext
Enter the file path for the logo: C:\Users\YourName\Images\logo.png
Enter the URL or text for the QR code: https://example.com
Enter the QR code color: blue
Enter the output file name (without extension): my_custom_qr
```

🎉 Your QR code will be saved as `my_custom_qr_QR.png`.

---

## ❓ **Troubleshooting**:

- **File Not Found**: Double-check the logo file path.
- **Color Issues**: Ensure you enter a valid color name (e.g., `red`, `blue`).
- **QR Code Not Scanning**: Resize the logo or choose a contrasting color.

---

## 📞 **Contact Information:**

- **Phone**: +91 7498046973
- **Email**: [sty9594@gmail.com](mailto:sty9594@gmail.com)
