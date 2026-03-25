import qrcode

# Create QR object
x = qrcode.QRCode()

# UPI details
upi_id = "yourupi@bank"   # Replace with actual UPI ID
name = "Learn with Raju"
note = "Just for Coffee"
amount = "1"

# Create UPI payment link
link = f"upi://pay?pa={upi_id}&pn={name}&tn={note}&am={amount}&cu=INR"

# Add data to QR
x.add_data(link)
x.make(fit=True)

# Generate QR image
res = x.make_image(fill_color="black", back_color="white")

# Save QR code
res.save("upi_qr.png")

print("UPI QR Code Created Successfully!!!")
