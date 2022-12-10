# Bulk-font2image-tool

![image](https://user-images.githubusercontent.com/115096590/206816863-71318b9d-75ee-4755-950e-388eae7e5fb0.png)

# About:

The purpose of this script is to create image files of each individual character of any .ttf format fonts automatically on multiple fonts at the same time just by running the script

With this script, you will get 600x600 pixel PNG files of the following images:
- English alphabet letters
- Numbers 0-9
- Special characters: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

By default the images are captioned (named) in the following format:

  letter/number/abbreviated name of special character, char, whitebg, name of the font

For example:
   - 4, char, whitebg, Arial
   - d, char, whitebg, TimesNewRoman
   - semicolon, whitebg, ComicSans (hehe)

The caption formatting can be changed in the last line of code, marked by the comment pointing to the segment
{symbol_name}, char, whitebg, {font-path}.png
  - If you refer this to the above examples, it is easy to figure out which part does what
  
  For example, if you want to remove everything but the name of the character, remove ", char, whitebg, {font_path}" portion from the code

The naming for the special characters have been abbreviated on purpose
  - If you wish to change any of the abbreviated names for special characters, you can just edit the fonts.py file where you find the list
  - Be aware that you cannot use many of those characters in the filename itself, which is the reason for giving them English names

# Instructions:

- Make an empty folder, name it whatever you want
- Paste the fonts.py script into that folder
- Go to C:\Windows\Fonts/ and select which fonts you would like to use
- Copy these fonts into the folder you just created
- Open Command Prompt into this directory
- Type: python fonts.py
- Hit Enter key

The script will automatically make subfolders based on the filename of each font and save images of each character into the subfolders.
- You might want to edit the names of the fonts separately if you want the output filenames to be cleaner
- Alternatively just remove the {font_path} portion to remove the font names from the filename as described above

This process might take a while if you have a lot of fonts so please be patient

# Final Thoughts:

- Please review the results keeping in mind that some fonts might escape the boundaries of the image
    This usually doesn't happen with most fonts

- Also remember that you are liable and responsible to check the license and terms of use for each font

- Have a banana and enjoy!


# Examples:

Times New Roman:

![h, char, whitebg, Times](https://user-images.githubusercontent.com/115096590/206815786-9fcaa162-b2ec-438d-8064-f2f2299716a9.png)
![4, char, whitebg, Times](https://user-images.githubusercontent.com/115096590/206815849-d9e21c2e-f3c2-4e77-bf39-50b38345964a.png)
![underscore, char, whitebg, Times](https://user-images.githubusercontent.com/115096590/206815896-64832ae1-bd3b-48dd-ad3f-9e07d69c7bdc.png)
![percent, char, whitebg, Times](https://user-images.githubusercontent.com/115096590/206815955-4b839501-6af0-4a35-b3d0-53994649fda5.png)

Courier New:

![b, char, whitebg, CourierNew](https://user-images.githubusercontent.com/115096590/206817908-9cbf903f-832c-4691-ad3f-0e8d947d107f.png)
![ltsign, char, whitebg, CourierNew](https://user-images.githubusercontent.com/115096590/206817918-2b80e9a9-afe2-4423-b315-d9355468e8b7.png)
![4, char, whitebg, CourierNew](https://user-images.githubusercontent.com/115096590/206817929-0f3433ed-6c90-4d68-9c63-5ce2ca309c80.png)
![rcurly, char, whitebg, CourierNew](https://user-images.githubusercontent.com/115096590/206817943-2f72fd7d-fa07-4e08-92b5-9a208930a3ee.png)


