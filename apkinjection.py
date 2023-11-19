import binascii
import struct
import os

def hide_apk_in_image(apk_file, image_file, output_file):

   with open(apk_file, "rb") as f:
       apk_data = f.read()

   with open(image_file, "rb") as f:
       image_data = f.read()
   offset = image_data.find(b"\x50\x4B\x03\x04")

   image_data = bytearray(image_data)
   image_data[offset:] = apk_data

   with open(output_file, "wb") as f:
       f.write(image_data)

apk_file = input("Enter the path to the APK file: ")

image_file = input("Enter the path to the image file: ")

output_file = input("Enter the path to the output file: ")

hide_apk_in_image(apk_file, image_file, output_file)

print("The APK payload has been hidden in the image file.")
