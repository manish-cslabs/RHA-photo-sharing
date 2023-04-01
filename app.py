from PIL import Image, ImageDraw, ImageFont
import requests
import io


# put_border_radius
def put_border_radius(image, border_radius, fill_color):
    # create a draw object
    draw = ImageDraw.Draw(image)
    # draw a rounded rectangle
    draw.rounded_rectangle((0, 0 ) + image.size, radius=border_radius, fill=fill_color, outline=(0, 0, 0, 0))

    

# get a random image 
image_response = requests.get('https://source.unsplash.com/random/300x200')
image = Image.open(io.BytesIO(image_response.content))
# decorate the image
padding = 80
border_radius = 15
fill_color = "green"
# get container size
container_size = (image.width + padding, image.height + padding *3)
# create a new image
container = Image.new('RGBA', container_size, (0, 0, 0, 0))

# put_border_radius
put_border_radius(container, border_radius, fill_color)


# paste image in container at the center
container_width, container_height = container.size
image_width, image_height = image.size
x = (container_width - image_width) // 2
y = 30  # or any desired y-coordinate
container.paste(image,(x,y)) 


# Add text to the container using the ImageDraw module
draw = ImageDraw.Draw(container)
text = "You have checked in \n successfully!"
font = ImageFont.truetype("arial.ttf", 18)
# get text box size
text_box  = draw.textbbox((0, 0), text, font=font)
text_width, text_height = (text_box[2] - text_box[0]), (text_box[3] - text_box[1])
text_position = ((container.width - text_width) / 2, image.height + padding)
draw.text(text_position, text, font=font, fill="white", align='center')


draw = ImageDraw.Draw(container)
text = "Thank you <username>!"
font = ImageFont.truetype("arial.ttf", 22)
# get text box size
text_box  = draw.textbbox((0, 0), text, font=font)
text_width, text_height = (text_box[2] - text_box[0]), (text_box[3] - text_box[1])
text_position = ((container.width - text_width) / 2, image.height + padding*1.6)
draw.text(text_position, text, font=font, fill="Black", align='center')


draw = ImageDraw.Draw(container)
text = "This is your #7 drive with RHA."
font = ImageFont.truetype("arial.ttf", 15)
# get text box size
text_box  = draw.textbbox((0, 0), text, font=font)
text_width, text_height = (text_box[2] - text_box[0]), (text_box[3] - text_box[1])
text_position = ((container.width - text_width) / 2, image.height + padding*2)
draw.text(text_position, text, font=font, fill="white", align='center')


# save the image
container.save('decorated_image.png')

