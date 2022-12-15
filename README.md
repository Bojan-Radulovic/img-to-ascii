# img-to-ascii
A python image to ASCII art converter
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Use](#use)
## General info
This program takes a PNG, JPG or JPEG image and outputs a TXT file containing the ASCII art representation of the image and a JPG image - an ASCII art representation of the original image in color
## Technologies
Project is created with:
* Python 3.9
## Use
Download main.py, install the required dependencies and run the script.
* Input the full name of the image you want to convert to ASCII (e.g. example.jpg). The image must be located in the same folder as main.py
* Next, input the number of characters that will be used to represent one row of the image. A bigger number means a more detailed image, but computation for bigger numbers can take a long time, the resault has a big resolution and looks less artistic. The recommended value is about 100
* Finally, input the brightenss enhancer factor - since the output image background is black, it is often a good idea to brighten up the output a little to closer represent the original image. The recommended value is around 2.5.
After this, two files will be generated: output.jpg and output.txt
