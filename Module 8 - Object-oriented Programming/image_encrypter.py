from PIL import Image

from lfsr import LFSR


class ImageEncrypter:
    # Initialize an ImageEncrypter object with an LFSR and image file name
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name
        self.image = None

    # Open the image specified by ‘file_name’ in constructor
    def open_image(self):
        self.image = Image.open(self.file_name)

    # Converts the image to a 2D array of R, G, B triples
    def pixelate(self):
        return self.image.load()

    # Get image dimensions
    def get_dimensions(self):
        return self.image.size

    # Encrypts the 2D pixelated “image” returned from pixelate()
    def encrypt(self):
        # Get PixelAccess object
        pixels = self.pixelate()

        # Get the width and height so we can traverse through each pixel
        width, height = self.get_dimensions()
        for x in range(width):
            for y in range(height):
                # Encrypt each pixel and store in a list (since tuple items can't be changed individually)
                current_pixel = pixels[x, y]
                encrypted_pixel = []
                for i in range(len(current_pixel)):
                    self.lfsr.step()
                    encrypted_pixel.append(current_pixel[i] ^ int(self.lfsr.get_seed(), 2))

                    # Rewrite to the encrypted pixel
                pixels[x, y] = tuple(encrypted_pixel)

    # Converts the encrypted 2D pixelated image into an image
    def save_image(self, file_name: str):
        self.image.save(file_name + "_transform.png")


# Executable code that invokes ImageEncrypter and encrypts/decrypts an image and saves the result to a file
def main():
    lfsr = LFSR("10011010", 5)
    image_encrypter = ImageEncrypter(lfsr, "football.png")
    image_encrypter.open_image()
    image_encrypter.encrypt()
    image_encrypter.save_image("football")


if __name__ == "__main__":
    main()
