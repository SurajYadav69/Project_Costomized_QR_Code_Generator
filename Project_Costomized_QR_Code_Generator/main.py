# Project_Costomized_QR_Code_Generator

# Import modules
import qrcode
from PIL import Image

# Get the logo file path from the user
Logo_link = input("Carefully enter the file path for the logo you want to customize: ")

try:
    # Open the logo image
    logo = Image.open(Logo_link)
except FileNotFoundError:
    print(f"Error: The file '{Logo_link}' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred while opening the logo image: {e}")
    exit()

# Set the base width for resizing the logo
basewidth = 100

# Calculate the height to maintain aspect ratio
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))

# Resize the logo with a high-quality downsampling filter
logo = logo.resize((basewidth, hsize), Image.LANCZOS)

# Create a QRCode object with high error correction
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Get the URL or text to encode in the QR code from the user
url = input("Enter the URL you want to include in the QR code: ")

# Add the data to the QR code
QRcode.add_data(url)

# Generate the QR code
QRcode.make()

# Get the desired QR code color from the user
QRcolor = input("Which QR code color would you like that best complements your customized QR code?: ")

try:
    # Generate the QR code image with the specified color
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
except ValueError as e:
    print(f"Error: Invalid color '{QRcolor}'. Please enter a valid color name.")
    exit()
except Exception as e:
    print(f"An error occurred while generating the QR code: {e}")
    exit()

# Calculate the position to paste the logo (centered)
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)

# Paste the logo onto the QR code
QRimg.paste(logo, pos, logo)

# Save the final QR code image with the logo embedded
output_filename = input("Enter output file name (without extension): ") + "_QR.png"
QRimg.save(output_filename)

print(f"QR code generated and saved as '{output_filename}'!")
