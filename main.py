from PIL import Image, ImageDraw

def generate_art():
    print('Generating Art!')
    image_size_px = 128
    image_bg_color = 255, 255, 255
    image = Image.new("RGB", size=(image_size_px, image_size_px), color=(image_bg_color) )
    
    draw = ImageDraw.Draw(image)
    line_xy = ((0, 0 ), (image_size_px, image_size_px))
    draw.line(line_xy, fill=(0, 0, 0))

    image.save('test_image.png')

if __name__ == "__main__":
    generate_art()