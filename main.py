import xml.etree.ElementTree as ET

#Programming-Assignment-Data\com.apalon.ringtones Programming-Assignment-Data\com.dropbox.android Programming-Assignment-Data\com.giphy.messenger-1 Programming-Assignment-Data\com.giphy.messenger-2 Programming-Assignment-Data\com.google.android.apps.transalte Programming-Assignment-Data\com.pandora.android Programming-Assignment-Data\com.yelp.android
file_list = input("Provide the path of all png-xml file pairs, without file extensions, to be annotated separated by a single whitespace (ex: Programming-Assignment-Data\com.apalon.ringtones)\n")
file_list = file_list.split(" ")
print(file_list)

for file in file_list:
  tree = ET.parse(file +".xml")
  root = tree.getroot()
  print("Root is",root)
  for element in root.findall(".//*[@clickable='true']"):
    print(element.attrib['bounds'])