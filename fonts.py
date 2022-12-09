# Import the necessary libraries
from PIL import Image, ImageDraw, ImageFont
import string
import os

# Get a list of all files in the current directory
files = os.listdir('.')

# Filter the list to only include font files with a .ttf extension
font_files = [f for f in files if f.endswith('.ttf')]

# Create a list of all the letters (upper and lower case)
letters = list(string.ascii_letters)

# Create a list of all the digits
digits = list(string.digits)

# Create a list of all the punctuation characters
punctuation = list(string.punctuation)

# Define a dictionary that maps the punctuation characters to their abbreviated English names
punctuation_names = {
    '!': 'exclam',
    '"': 'doubleq',
    '#': 'num',
    '$': 'dollar',
    '%': 'percent',
    '&': 'ampersand',
    '\'': 'singleq',
    '(': 'lpar',
    ')': 'rpar',
    '*': 'asterisk',
    '+': 'plus',
    ',': 'comma',
    '-': 'hyphen',
    '.': 'period',
    '/': 'slash',
    ':': 'colon',
    ';': 'semicolon',
    '<': 'ltsign',
    '=': 'eqsign',
    '>': 'gtsign',
    '?': 'question',
    '@': 'atsign',
    '[': 'lsquare',
    '\\': 'backslash',
    ']': 'rsquare',
    '^': 'caret',
    '_': 'underscore',
    '`': 'grave',
    '{': 'lcurly',
    '|': 'vertbar',
    '}': 'rcurly',
    '~': 'tilde'
}

# Combine the letters, digits, and special characters into a single list
symbols = letters + digits + punctuation

# Print the list of symbols
for symbol in symbols:
    if symbol.isalnum() or symbol in string.punctuation:

        # Iterate over the font files
        for font_file in font_files:
        
            # Get the path to the subfolder for the font
            font_path = os.path.splitext(font_file)[0]
            
            # Open the font file
            font = ImageFont.truetype(font_file, size=450)

            # Create a new image with a white background
            image = Image.new('RGB', (600, 600), color='white')

            # Get a drawing context
            draw = ImageDraw.Draw(image)
        
        # Get the size of the symbol
            bbox = draw.textbbox(text=symbol, xy=(0,0), font=font)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            width_target = (600-width)/2
            height_target = (600-height)/2
       
        # Draw the letter "A" on the image
            draw.text((width_target, 0), symbol, fill='black', font=font)

        # Save the image to the subfolder
            os.makedirs(font_path, exist_ok=True)
            if symbol.isalnum():
                symbol_name = symbol.replace(' ', '')
            else:
                symbol_name = punctuation_names[symbol]
            image.save(os.path.join(font_path,f'{symbol_name}, char, whitebg, {font_path}.png'))
                                                # ^ You can modify filename formatting here