from PIL import Image, ImageDraw


# create_gradient_image
def create_gradient_image(container_size, color1, color2):
    # get the size of the gradient image
    width, height = container_size

    # Create a new image with a white background
    gradient_image = Image.new('RGB', (width, height), color=(255, 255, 255))

    # Create a draw object for the image
    draw = ImageDraw.Draw(gradient_image)

    # Draw the vertical gradient on the image
    for y in range(height):
        # Calculate the color for this row
        r = int(color1[0] + (y / (height - 1)) * (color2[0] - color1[0]))
        g = int(color1[1] + (y / (height - 1)) * (color2[1] - color1[1]))
        b = int(color1[2] + (y / (height - 1)) * (color2[2] - color1[2]))
        color = (r, g, b)
        # Draw a line for this row with the calculated color
        draw.line((0, y, width, y), fill=color)

    # Save the gradient image
    # gradient_image.save('gradient_image.png')

    return gradient_image



# put_border_radius
def put_border_radius(image, border_radius):
    # create a new image
    img_container_size = (image.width, image.height)
    img_container = Image.new('RGBA', img_container_size, (0, 0, 0, 0))
    mask = Image.new("L", img_container_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0)+img_container_size,
                           radius=border_radius, fill=255, outline=255, width=5)

    # paste the image onto the img_container using the mask
    img_container.paste(image, (0, 0))
    img_container.putalpha(mask)

    return img_container


# from PIL import Image

# color1 = (0, 100, 40)
# color2 = (0, 71, 77)
# width, height = 300, 200

# # create a new gradient image
# gradient = Image.new('RGB', (width, height))

# # draw gradient
# for x in range(width):
#     for y in range(height):
#         r = int(color1[0] + (color2[0] - color1[0]) * x / width)
#         g = int(color1[1] + (color2[1] - color1[1]) * x / width)
#         b = int(color1[2] + (color2[2] - color1[2]) * x / width)
#         gradient.putpixel((x, y), (r, g, b))

# # save image
# gradient.save('gradient.png')
