from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import io
from image_edit_helper import put_border_radius, create_gradient_image


# Define the colors for the gradient
color1 = (0, 100, 40)
color2 = (0, 71, 77)
padding = 80
margin = 30
border_radius = 15
container_size = (400, 700)
container_width, container_height = container_size
used_height = 0


# Decorate the image ~~~~~~~~~~~~
# ~~~~~~~~~~~~~ container ~~~~~~~~~~~~~~~~~~~~~
# get container size
# container_size = (image.width + padding, image.height + padding * 5)
container = create_gradient_image(container_size, color1, color2)
# put_border_radius
container = put_border_radius(container, border_radius)

# ~~~~~~~~~~ logo image ~~~~~~~~~~~~
# Put the logo image
rha_logo_img = Image.open("static/rha-logo.png")
# resize the logo image
new_size = tuple(dim - padding*2.5 for dim in container_size)
# new_size = tuple(dim // 1.6 for dim in container_size)
rha_logo_img.thumbnail(new_size)

# paste the logo image in the center of the container
# container_width, container_height = container.size
logo_width, logo_height = rha_logo_img.size
x = (container_width - logo_width) // 2
y = int(used_height + margin)
container.paste(rha_logo_img, (x, y))
used_height = y + logo_height
# ~~~~~~~~~~ end: logo image ~~~~~~~~~~~~

# ~~~~~~~~~~ image ~~~~~~~~~~~~
# get a random image
# image_response = requests.get('https://source.unsplash.com/random/300x200')
# image = Image.open(io.BytesIO(image_response.content))
image = Image.open("static/checkin-sample2.jpg")
image = Image.open("static/checkin-sample3.jpg")
image = Image.open("static/checkin-sample.jpg")

# Crop the image
# Define crop dimensions
crop_width, crop_height = 275, 300
cropped_img = ImageOps.fit(image, (crop_width, crop_height), Image.ANTIALIAS)
## Add a white frame to the cropped image
# Define frame size
# frame_size = 10
# framed_img = ImageOps.expand(image, border=frame_size, fill="white")
# image = framed_img
image = cropped_img
border_radius = 35
image = put_border_radius(image, border_radius)

# paste image in container at the center
image_width, image_height = image.size
x = (container_width - image_width) // 2
y = int(used_height + margin)
container.paste(image, (x, y), image)
used_height = y + image_height
# ~~~~~~~~~~ end: image ~~~~~~~~~~~~


# Add text to the container using the ImageDraw module
draw = ImageDraw.Draw(container)
text = "I'M A ROBIN CADET"
font = ImageFont.truetype("arialbd.ttf", 15)
# get text box size
text_box = draw.textbbox((0, 0), text, font=font)
text_width, text_height = (
    text_box[2] - text_box[0]), (text_box[3] - text_box[1])
x = (container.width - text_width) / 2
y = int(used_height + margin)
draw.text((x, y), text, font=font, fill=(30, 228, 179), align='center')
used_height = y + text_height


draw = ImageDraw.Draw(container)
text = """I just checked-in to my \n 6th drive with RHA!"""
font = ImageFont.truetype("arialbd.ttf", 30)
# get text box size
text_box = draw.textbbox((0, 0), text, font=font)
text_width, text_height = (
    text_box[2] - text_box[0]), (text_box[3] - text_box[1])
x = (container.width - text_width) / 2
y = int(used_height + margin *1.5)
draw.text((x, y), text, font=font, fill=(255, 255, 255), align='center')
used_height = y + text_height

# ~~~~~~ website box ~~~~~~


# # Create a draw object for the image
# text = "Go to robinhoodarmy.com to learn more"
# font = ImageFont.truetype("arial.ttf", 15)
# # get text box size
# text_box = draw.textbbox((0, 0), text, font=font)
# text_width, text_height = (
#     text_box[2] - text_box[0]), (text_box[3] - text_box[1])


# # paste image in container at the center
# url_container = Image.new('RGB', (text_width+margin, text_height+margin), color=(0, 254, 176))
# draw = ImageDraw.Draw(url_container)

# draw.text((margin//2, margin//2), text, font=font, fill=(0, 0, 0), align='center')

# url_container_width, url_container_height = url_container.size
# x = (container_width - url_container_width) // 2
# y = int(used_height + margin*2)
# container.paste(url_container, (x, y))
# used_height = y + url_container_height
# Create a draw object for the image
text = "Go to "
bold_text = "robinhoodarmy.com"
remainig_text = "to learn more"
font = ImageFont.truetype("arial.ttf", 15)
bold_font = ImageFont.truetype("arialbd.ttf", 15)
remainig_text_font = ImageFont.truetype("arial.ttf", 15)
# get text box size
text_box = draw.textbbox((0, 0), text + bold_text + remainig_text, font=bold_font)
text_width, text_height = (
    text_box[2] - text_box[0]), (text_box[3] - text_box[1])


# paste image in container at the center
url_container = Image.new('RGB', (text_width+margin, text_height+margin), color=(0, 254, 176))
draw = ImageDraw.Draw(url_container)

draw.text((margin//2, margin//2), text, font=font, fill=(0, 0, 0), align='center')
draw.text((margin//2 + draw.textsize(text, font=font)[0], margin//2), bold_text, font=bold_font, fill=(0, 0, 0), align='center')
draw.text((margin//2 + + margin//2 + draw.textsize(text, font=font)[0] +draw.textsize(bold_text, font=font)[0], margin//2), remainig_text, font=font, fill=(0, 0, 0), align='center')

url_container_width, url_container_height = url_container.size
x = (container_width - url_container_width) // 2
y = int(used_height + margin*2)
container.paste(url_container, (x, y))
used_height = y + url_container_height


# save the image
container.save('decorated_image.png')
