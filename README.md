# APK Payload Hiding Tool

This tool allows you to hide an APK payload inside an image file. The resulting image file can then be opened to execute the hidden APK payload.

## Disclaimer

This tool is for educational and research purposes only. The developers of this tool are not responsible for any misuse or damage caused by this tool. Any actions and/or activities related to the material contained within this tool is solely your responsibility.

## How to Use

1. Run the `hide_apk_in_image` function with the paths to your APK file, image file, and the output file.
2. The tool will find the offset of the APK payload in the image and replace the bytes at the offset with the bytes from the APK file.
3. The resulting image file will contain the hidden APK payload.
