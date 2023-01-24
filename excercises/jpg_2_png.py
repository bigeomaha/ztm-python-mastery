from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')
filtered_img = img.filter(ImageFilter.EMBOSS)
filtered_img.save('./images/blur.png', 'png')