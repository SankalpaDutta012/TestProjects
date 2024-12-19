import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=56_rgF058QI")
img.save("FG_2_YT.png") 



import qrcode 
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10, border=3,)
qr.add_data("https://www.youtube.com/watch?v=56_rgF058QI")
qr.make(fit=True)
img = qr.make_image(fill_color = "red", back_color = "yellow")
img.save("FG_2_YT_2.png")
