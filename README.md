# GUI-Annotator
CSci 435 Programming assignment #1

Run main.py like you would with any python program. This code was tested with Python 3.11.4. A "requirements.txt" file is provided to install the required Pillow package. The code also uses the re and xml packages from the Python standard library.

When running the code, follow the prompt. Proper input for each file pair is the path and file name without the file type extension. Multiple pairs should be separated by a single space. Note that extra spaces, including before and after the input, will lead to an error. Once input is entered, the code will run and notify when the annotations are created. Annottated PNGs will be found in the same location as the input files and saved as *original-file-name*.annotated.png. 

I chose Python because the project requirements were simple and could be met with a basic script. It was made clear to me that files should be accepted as parameters so I used Python's input() function for simplicity. I used xml.etree.ElementTree from Python's standard library because it was most easily available and let me convert the xml file into a tree. Location information was provided in strings and had to be converted into a list of ints. I used regex from Python's re library for this because it is easy to use and the format of the strings was consistent. I used Pillow to annotate the PNGs because it is a popular image editor library for Python.
