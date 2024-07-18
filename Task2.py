from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    width, height = image.size

    encrypted_image = Image.new(mode=image.mode, size=(width, height))
    pixels = encrypted_image.load()

    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            # swapping R and G values
            encrypted_pixel = (pixel[1], pixel[0], pixel[2])  # Swap R and G channels
            pixels[i, j] = encrypted_pixel

    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    width, height = image.size

    decrypted_image = Image.new(mode=image.mode, size=(width, height))
    pixels = decrypted_image.load()

    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            #reversing the encryption process
            decrypted_pixel = (pixel[1], pixel[0], pixel[2])  # Swap R and G channels back
            pixels[i, j] = decrypted_pixel

    decrypted_image.save(output_image_path)

input_image = "input_image.png"
encrypted_image = "encrypted_image.png"
decrypted_image = "decrypted_image.png"

key = "123" 

# Encrypt the image
encrypt_image(input_image, encrypted_image, key)

# Decrypt the encrypted image
decrypt_image(encrypted_image, decrypted_image, key)
