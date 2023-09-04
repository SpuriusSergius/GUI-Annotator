import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageColor
import re

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
print(file_list)

for file in file_list:
  tree = ET.parse(file + ".xml")
  root = tree.getroot()
  print("Root is",root)
  leaves_list = []
  get_leaves(root, leaves_list)
  print(leaves_list)
  # with Image.open(file + ".png") as im:
  #   print(im.format, im.size, im.mode)
  #   draw = ImageDraw.Draw(im)
  #   for element in leaves_list:
  #     print(element.attrib['bounds'])
  #     bounds = re.findall('[0-9]+', element.attrib['bounds'])
  #     bounds = list(map(int, bounds))
  #     print(bounds)
  #     draw.rectangle(bounds, fill = None, outline = ImageColor.getrgb("yellow"), width=5)
  #   im.save(file + ".annotated.png")
