import qrcode


img = qrcode.make("https://mahtabvariyani.vercel.app/")
img.save("mycode.png")