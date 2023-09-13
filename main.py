from PIL import Image, ImageDraw
import os
# Creating the badge with restrictions
def is_valid_badge(image_path, output_directory):
    issues = []

    try:
        if not os.path.isfile(image_path):
            issues.append("Image file does not exist")

        with Image.open(image_path) as img:
            num_channels = len(img.getbands())
            if img.size != (512, 512):
                issues.append("Image size does not match the criteria")

            # Verify transparent and non-transparent pixels along with the circular area
            alpha = img.getchannel('A')
            for x in range(512):
                for y in range(512):
                    distance_squared = (x - 256) ** 2 + (y - 256) ** 2
                    if distance_squared <= 256 ** 2 and alpha.getpixel((x, y)) != 0:
                        pass
                    elif distance_squared <= 256 ** 2 and alpha.getpixel((x, y)) == 0:
                        issues.append("circular area has transparent pixels")
                    elif distance_squared > 256 ** 2 and alpha.getpixel((x, y)) == 0:
                        pass
                    elif distance_squared > 256 ** 2 and alpha.getpixel((x, y)) != 0:
                        issues.append("edges have non-transparent pixels")

        # Analyze happy feeling colors
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

        happy_threshold = 70 #this is a high value, I set it to lower values to get some sample output images
        if happy_percentage >= happy_threshold:
            print("happy badge")
        else:
            issues.append("not happy feeling badge")

        if not issues:
            verified_image_path = os.path.join(output_directory, "happy_badge_with_restrictions.png")
            img.save(verified_image_path)
            return "Image meets criteria"

    except Exception as e:
        issues.append(f"An error occurred: {str(e)}")

    if issues:
        for issue in issues:
            print(issue)


image_path = "C:/Users/dgnze/PycharmProjects/creatingBadge/input_images/purple_cat.png"
project_directory = "C:/Users/dgnze/PycharmProjects/creatingBadge//output_images"
verification_result = is_valid_badge(image_path, project_directory)
if verification_result:
    print(verification_result)


# Creating the badge without restrictions
def convert_to_happy_badge(input_image_path, project_directory):
    if not os.path.isfile(input_image_path):
        return "Input image file does not exist"

    try:
        img = Image.open(input_image_path)

        if not img.format:
            return "Input file is not a valid image"

        img = img.resize((512, 512), Image.LANCZOS)

        mask = Image.new('L', (512, 512), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 512, 512), fill=255)

        badge = Image.new('RGBA', (512, 512))
        badge.paste(img, (0, 0), mask)

        output_directory = os.path.join(project_directory, "output_images")
        os.makedirs(output_directory, exist_ok=True)
        output_image_path = os.path.join(output_directory, "happy_badge_without_restriction.png")

        badge.save(output_image_path, 'PNG')

        return "Image converted and saved successfully"
    except Exception as e:
        return f"An error occurred: {str(e)}"

input_path = "C:/Users/dgnze/PycharmProjects/creatingBadge/input_images/purple_cat.png"
project_directory = "C:/Users/dgnze/PycharmProjects/creatingBadge"
conversion_result = convert_to_happy_badge(input_path, project_directory)
print(conversion_result)





