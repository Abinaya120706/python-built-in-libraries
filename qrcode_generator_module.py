import qrcode

# Create QR object
x = qrcode.QRCode()

# Message to encode
msg = "Students are very good !!! 👍"

# Add data
x.add_data(msg)
x.make(fit=True)

# Generate image
res = x.make_image(fill_color="black", back_color="white")

# Save QR code
res.save("QR.png")

print("Created Successfully!!!")
