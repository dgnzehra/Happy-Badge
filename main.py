from PIL import Image, ImageDraw

'''
The following code below accepts the images only if they are 512x512
png format (if not png format it gives an error because png format has 4 dimensions RGBA)
There should be only non transparent pixels in the circle
The colors in the image should give a happy feeling (here happy feeling criteria is bright colors in the image)
'''
def is_happy_badge(image_path):
    # Load the image
    img = Image.open(image_path)

    issues = [] #an empty list, it is intended to store any issues or problems that are encountered during the analysis of the image

    # Check dimensions
    if img.size != (512, 512):
        issues.append("Image dimensions are not 512x512.")

    # Verify the circular boundary
    width, height = img.size
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    non_transparent = Image.new('RGBA', (width, height))
    non_transparent.paste(img, (0, 0), mask)
    non_transparent_pixels = non_transparent.getcolors(width * height)

    # Check if non-transparent pixels are within the circle
    if len(non_transparent_pixels) != 1:
        issues.append("Non-transparent pixels are not within a circle.")

    # Analyze colors for a "happy" feeling (more bright colors are considered to evoke a "happy" feeling)
    colors = img.getdata()
    num_happy_colors = 0
    num_total_pixels = 0

    for color in colors:
        r, g, b, a = color
        if a != 0:
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            num_total_pixels += 1

            brightness_threshold = 150

            if brightness > brightness_threshold:
                num_happy_colors += 1

    happy_percentage = (num_happy_colors / num_total_pixels) * 100

    happy_threshold = 70

    return (
        happy_percentage >= happy_threshold
        and len(non_transparent_pixels) == 1
        and img.size == (512, 512)
    ), issues

def convert_to_happy_badge(input_image_path, output_image_path):
    img = Image.open(input_image_path)

    img = img.resize((512, 512), Image.ANTIALIAS)

    mask = Image.new('L', (512, 512), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 512, 512), fill=255)

    badge = Image.new('RGBA', (512, 512))
    badge.paste(img, (0, 0), mask)

    badge.save(output_image_path, 'PNG')

input_path = 'input_image_with_restrictions'
output_path = 'happy_badge_with_restrictions.png'

result, issues = is_happy_badge(input_path)

if result:
    convert_to_happy_badge(input_path, output_path)
    print("Image meets criteria and has been converted to a happy badge.")
else:
    print("Image does not meet the criteria for a happy badge. Issues:")
    for issue in issues:
        print("- " + issue)


'''
The following code below does not have any restrictions
It accepts all formats of images and all sizes
Also, does not check if the image evokes a happy feeling or not
'''
def convert_to_happy_badge(input_image_path, output_image_path):
    # Load the input image
    img = Image.open(input_image_path)

    # Resize the image to 512x512
    img = img.resize((512, 512), Image.LANCZOS)

    # Create a circular mask
    mask = Image.new('L', (512, 512), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 512, 512), fill=255)

    # Apply the mask to the input image
    badge = Image.new('RGBA', (512, 512))
    badge.paste(img, (0, 0), mask)

    # Save the resulting badge
    badge.save(output_image_path, 'PNG')

input_path = 'input_image_without_restrictions'
output_path = 'happy_badge_without_restrictions.png'
convert_to_happy_badge(input_path, output_path)
