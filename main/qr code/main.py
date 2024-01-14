import qrcode
import PIL
upi_id = input("Enter the Upi ID ")
# upi_id upi://pay?pa={user_id}
upi = f"upi://pay?pa={upi_id}"
upi_qr = qrcode.make(upi)
upi_qr.save("payment.png")
upi_qr.show()