# Badge Verification and Conversion

This Python script provides two main functions to handle badge images: verification with restrictions and conversion without restrictions. It uses the Pillow (PIL) library for image processing.

## Verification with Restrictions

### Function: `is_valid_badge(image_path, output_directory)`

This function verifies that a badge image meets specific criteria with restrictions:

1. Image size must be 512x512 pixels.
2. Non-transparent pixels are only allowed within a circular area.
3. The image must have a "happy" feeling, based on color brightness.

**Parameters:**
- `image_path`: The path to the input image file to be verified.
- `output_directory`: The directory where the verified image will be saved if it meets the criteria.

## Conversion without Restrictions

### Function: convert_to_happy_badge(input_image_path, project_directory)

This function converts an input image into a circular badge without any restrictions. The resulting badge has a size of 512x512 pixels and a circular shape.

**Parameters:**
    input_image_path: The path to the input image file to be converted.
    project_directory: The directory where the converted image will be saved.


## Example Usage
You can use the provided example usage code for each function as a reference to test your badge images.

## Dependencies
    This script relies on the Pillow library for image processing. You can install it using pip install Pillow.

Feel free to use, modify, and integrate these functions into your projects as needed. Enjoy creating and verifying badge images!
