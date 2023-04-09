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
# container = put_border_radius(container, border_radius)

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


# ~~~~~~~~~~ Badge image ~~~~~~~~~~~~
badge_image = Image.open("static/badges/cadet.png")
# resize the badge_image
new_size = tuple(dim - padding*2.5 for dim in image.size)
# new_size = tuple(dim // 1.6 for dim in container_size)
badge_image.thumbnail(new_size)
# paste image in container at the center
image_width, image_height = badge_image.size
x = (container_width - image_width) // 2
y = int(used_height - margin*1.3)
container.paste(badge_image, (x, y), badge_image)
used_height = y + image_height
# ~~~~~~~~~~ end: Badge image ~~~~~~~~~~~~

# Add text to the container using the ImageDraw module
draw = ImageDraw.Draw(container)
text = "I'M A ROBIN CADET"
font = ImageFont.truetype("arialbd.ttf", 15)
# get text box size
text_box = draw.textbbox((0, 0), text, font=font)
text_width, text_height = (
    text_box[2] - text_box[0]), (text_box[3] - text_box[1])
x = (container.width - text_width) / 2
y = int(used_height + margin*0.5)
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
y = int(used_height + margin *1.3)
draw.text((x, y), text, font=font, fill=(255, 255, 255), align='center')
used_height = y + text_height

# ~~~~~~ website box ~~~~~~
# Put the logo image
rha_logo_img = Image.open("static/website.png")
# resize the logo image
new_size = tuple(dim - padding for dim in container_size)
# new_size = tuple(dim // 1.6 for dim in container_size)
rha_logo_img.thumbnail(new_size)

# paste the logo image in the center of the container
# container_width, container_height = container.size
logo_width, logo_height = rha_logo_img.size
x = (container_width - logo_width) // 2
y = int(used_height + margin*1.5)
container.paste(rha_logo_img, (x, y))
used_height = y + logo_height


# save the image
container.save('decorated_image.png')
