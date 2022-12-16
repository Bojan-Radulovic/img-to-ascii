from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import math
from colorsys import rgb_to_hls, hls_to_rgb
from os import path

ascii_znakovi_txt = ["$", "@", "#", "S", "%", "?", "*", "+", "=", ";", ":", ",", "."]
ascii_string ="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI"
ascii_znakovi = []
for znak in ascii_string:
    ascii_znakovi.append(znak)
interval2 = len(ascii_znakovi_txt)/256
interval = len(ascii_znakovi)/256

one_char_width = 8
one_char_height = 18
def adjust_color_lightness(r, g, b, factor):
    h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def  getZnak(input):
    return ascii_znakovi[math.floor(input*interval)]


def getZnakTxt(input):
    return ascii_znakovi_txt[math.floor(input * interval2)]

font = ImageFont.truetype('C:\Windows\Fonts\lucon.ttf', 15)

text_file = open("output.txt", "w")
text_file.truncate(0)

unos_ispravan = False
while not unos_ispravan:
    ime_slike = input("Input the full name of the image (it has to be in the same folder as main.py): ").rstrip()
    unos_ispravan = True

    if ime_slike == "0":
        exit()

    if not (ime_slike.endswith(".jpg") or ime_slike.endswith(".jpeg") or ime_slike.endswith(".png")):
        print("Unsupported image format. Try again (or 0 to exit)")
        unos_ispravan = False

    elif not path.exists(ime_slike):
        print("Image doesn't exist. Try again (or 0 to exit)")
        unos_ispravan = False



im = Image.open(ime_slike)
im2 = im.copy()
width, height = im.size
ratio = width/height

wsmece = width
hsmece = height

new_width = ""
new_width2 = input("Width of output in characters (recommended: 100): ")
brightness = float(input("Brightness enhancer (recommended: 2.5): "))
if new_width2.upper() != "OG":
    new_width = int(new_width2)
    ratio = width / height
    height = (height/(width/new_width))*(one_char_width/one_char_height)
    width = new_width
    im = im.resize((int(width), int(height)), Image.NEAREST)
    width, height = im.size
else:
    new_width = wsmece
    ratio = width / height
    height = (height/(width/new_width))*(one_char_width/one_char_height)
    width = new_width
    im = im.resize((int(width), int(height)), Image.NEAREST)
    width, height = im.size

print()
print("Please wait...")

if new_width2.upper() =="OG":
    if wsmece > 1000:
        new_width_txt = 1000
        new_height_txt = (hsmece/(wsmece/new_width_txt))*(one_char_width/one_char_height)
        new_width_txt = int(new_width_txt)
        new_height_txt = int(new_height_txt)
        im2 = im2.resize((new_width_txt, new_height_txt), Image.NEAREST)
    else:
        new_width_txt = wsmece
        new_height_txt = (hsmece/(wsmece/new_width_txt))*(one_char_width/one_char_height)
        new_width_txt = int(new_width_txt)
        new_height_txt = int(new_height_txt)
        im2 = im2.resize((new_width_txt, new_height_txt), Image.NEAREST)
elif int(new_width2) > 1000:
    new_width_txt = 1000
    new_height_txt = (hsmece/(wsmece/new_width_txt))*(one_char_width/one_char_height)
    new_width_txt = int(new_width_txt)
    new_height_txt = int(new_height_txt)
    im2 = im2.resize((new_width_txt, new_height_txt), Image.NEAREST)
else:
    new_width_txt = int(new_width2)
    new_height_txt = (hsmece/(wsmece/new_width_txt))*(one_char_width/one_char_height)
    new_width_txt = int(new_width_txt)
    new_height_txt = int(new_height_txt)
    im2 = im2.resize((new_width_txt, new_height_txt), Image.NEAREST)

pix = im.load()
pix2 = im2.load()

one_char_width = 8
one_char_height = 14

output_image = Image.new('RGB', (one_char_width * width, one_char_height * height), color=(0, 0, 0))
d = ImageDraw.Draw(output_image)

one_char_width = 8
one_char_height = 18

ascii_znakovi.reverse()

for i in range(new_height_txt):
    for j in range(new_width_txt):
        if ime_slike.endswith(".jpg") or ime_slike.endswith(".jpeg"):
            r, g, b = pix2[j, i]
            h = int((r + b + g) / 3)
            pix2[j, i] = (h, h, h)
        else:
            r, g, b, a = pix2[j, i]
            h = int((r + b + g) / 3)
            pix2[j, i] = (h, h, h)
        text_file.write(getZnakTxt(h))
    text_file.write("\n")

for i in range(height):
    for j in range(width):
        if ime_slike.endswith(".jpg") or ime_slike.endswith(".jpeg"):
            r, g, b = pix[j, i]
            h = int((r + b + g) / 3)
        else:
            r, g, b, a = pix[j, i]
            h = int((r + b + g) / 3)
        # r, g, b = adjust_color_lightness(r, g, b, 5)
        one_char_width = 8
        one_char_height = 14
        d.text((j * one_char_width, i * one_char_height), getZnak(h), font=font, fill=(r, g, b))


# im.save("bw.jpg")
enhancer = ImageEnhance.Brightness(output_image)
output_image = enhancer.enhance(brightness)

width2, height2 = output_image.size
output_image = output_image.resize((int(width2), int(width2/ratio)))
output_image.save("output.jpg")

print("Done!")
