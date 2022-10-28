import easyocr
reader = easyocr.Reader(['ru', 'en'])
bounds = reader.readtext("<ПУТЬ К ФАЙЛУ>", paragraph=True)
import PIL
from PIL import Image, ImageDraw

im = PIL.Image.open("<ПУТЬ К ФАЙЛУ>")

def draw_boxes(image,bounds,color='red',width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0,*p1,*p2,*p3,*p0], fill=color,width=width)
    return image.show()
draw_boxes(im,bounds)
