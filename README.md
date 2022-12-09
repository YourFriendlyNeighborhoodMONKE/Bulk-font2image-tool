# Bulk-font2image-tool
The purpose of this script is to get image files of each individual character of any .ttf format fonts automatically on multiple fonts

With this script, you will get 600x600 pixel PNG files of the following images:
- English alphabet letters
- Numbers 0-9
- Special characters: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

By default the images are captioned (named) in the following format:
  letter/number/abbreviated name of special character, char, whitebg, name of the font
For example:
    4, char, whitebg, Arial
    d, char, whitebg, TimesNewRoman
    semicolon, whitebg, ComicSans (hehe)

The caption formatting can be changed in the last line of code, marked by the comment pointing to the segment
{symbol_name}, char, whitebg, {font-path}.png
  - If you refer this to the above examples, it is easy to figure out which part does what
  For example, if you want to remove everything but the name of the character, remove ", char, whitebg, {font_path}" portion from the code

The naming for the special characters have been abbreviated on purpose
  - If you wish to change any of the abbreviated names for special characters, you can just edit the fonts.py file where you find the list
  - Be aware that you cannot use many of those characters in the filename itself, which is the reason for giving them English names

INSTRUCTIONS:

- Make an empty folder, name it whatever you want
- Paste this script into that folder
- Go to C:\Windows\Fonts/ and select which fonts you would like to use
- Copy these fonts into the folder you just created
- Open Command Prompt into this directory
- Type: python fonts.py
- Hit Enter key

The script will automatically make subfolders based on the filename of each font and save images of each character into the subfolders
This process might take a while if you have a lot of fonts

FINAL THOUGHTS:

- Please review the results keeping in mind that some fonts might escape the boundaries of the image
    This usually doesn't happen with most fonts

- Also remember that you are liable and responsible to check the license and terms of use for each font

- Have a banana and enjoy!


