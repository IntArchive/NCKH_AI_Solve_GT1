import qrcode

# The link to be encoded
link = "https://nckhaisolvegt1.streamlit.app/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls error correction used for the QR Code
    box_size=10,  # size of each box
    border=4,  # thickness of the border
)

# Add the link data to the QR code
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')
img.save("/mnt/data/qrcode_link.png")

"/mnt/data/qrcode_link.png"
