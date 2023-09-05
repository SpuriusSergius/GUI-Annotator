import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageColor
import re

# function that creates a list of leaf nodes given a root node
def get_leaves(node, leaves_list):
  children = node.findall("*")
  if not children:
    leaves_list.append(node)
    return
  for child in children:
    get_leaves(child, leaves_list)


# I leave a copy of the input here for easy copy and paste:
# Programming-Assignment-Data\com.apalon.ringtones Programming-Assignment-Data\com.dropbox.android Programming-Assignment-Data\com.giphy.messenger-1 Programming-Assignment-Data\com.giphy.messenger-2 Programming-Assignment-Data\com.google.android.apps.transalte Programming-Assignment-Data\com.pandora.android Programming-Assignment-Data\com.yelp.android
file_list = input("Provide the path of all png-xml file pairs, without file extensions, to be annotated separated by a single whitespace (ex: Programming-Assignment-Data\com.apalon.ringtones)\n")
file_list = file_list.split(" ")

# iterate through all inputted files
for file in file_list:

  # parse the xml file and get the root element
  tree = ET.parse(file + ".xml")
  root = tree.getroot()

  # find the leaf elements of the xml file
  leaves_list = []
  get_leaves(root, leaves_list)

  # open corresponding PNG
  with Image.open(file + ".png") as im:
    draw = ImageDraw.Draw(im)

    # for each leaf element, use the element's bounds valye to draw a rectangle on the png given.
    for element in leaves_list:

      # bounds is a string, convert into a lust of integers
      bounds = re.findall('[0-9]+', element.attrib['bounds'])
      bounds = list(map(int, bounds))

      # draw the rectangle
      draw.rectangle(bounds, fill = None, outline = ImageColor.getrgb("yellow"), width=5)

    # save annotated PNG
    im.save(file + ".annotated.png")

print("Annotations complete. Annotated PNGs can be found in the same location as input with name \"[original_filename].annotated.png\"")