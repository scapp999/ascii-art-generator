from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, width=100):
    w, h = image.size
    ratio = h / w / 1.65
    new_height = int(width * ratio)

    image = image.resize((width, new_height))
    return image


def convert_to_gray(image):
    return image.convert("L")


def image_to_ascii(image):
    pixels = image.getdata()
    ascii_text = ""

    for pixel in pixels:
        ascii_text = ascii_text + ASCII_CHARS[pixel // 25]

    return ascii_text


def main():

    image_path = "image.jpg"

    try:
        img = Image.open(image_path)
    except Exception as error:
        print("Image not found")
        print(error)
        return

    img = resize_image(img)
    img = convert_to_gray(img)
    ascii_string = image_to_ascii(img)

    width = img.width

    result = ""
    i = 0

    while i < len(ascii_string):
        result = result + ascii_string[i:i + width] + "\n"
        i = i + width

    print(result)

    file = open("ascii_result.txt", "w")
    file.write(result)
    file.close()

    print("File saved successfully!")


if __name__ == "__main__":
    main()
