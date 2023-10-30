from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

import re
import json
import os

def get_filename_from_path(file_path):
    return os.path.basename(file_path)

def get_directory_from_path(file_path):
    return os.path.dirname(file_path)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
input_file_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print('Stripping ', input_file_path,'\n')


def remove_comments(json_string):
    # Regular expression pattern to match and remove single-line and multi-line comments
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"

    # Remove comments using the pattern and return the result
    return re.sub(pattern, lambda match: match.group(1) if match.group(1) else '', json_string, flags=re.MULTILINE | re.DOTALL)

#Remove comments function
def remove_comments_from_json_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Remove comments and blank lines from the list of lines
    cleaned_lines = [re.sub(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", lambda match: match.group(1) if match.group(1) else '', line).strip() for line in lines]

    # Join the lines back together to form a single string
    cleaned_json = "\n".join(line for line in cleaned_lines if line)

    # If output_file is not provided, overwrite the input_file
    if output_file is None:
        output_file = input_file

    with open(output_file, 'w') as outfile:
        outfile.write(cleaned_json)

#Get directory of original file (without name)
directory_path = get_directory_from_path(input_file_path)

#Get name of original file (without directory)
filename = get_filename_from_path(input_file_path)

#Create new file name with "Cleaned_" prefix
newFileName = "Cleaned_"+ filename
newFile = os.path.join(directory_path, newFileName)

#Call the remove comments function
if __name__ == "__main__":
    output_file_path = newFile

    remove_comments_from_json_file(input_file_path, output_file_path)

#print new file info
print("Created new file: ", newFileName)
print("In:", directory_path)

#Prompt to open new JSON
openFile = input('\nOpen new file in Default Editor?\nY/N \n')
if "y" in openFile.lower():
    print(newFile)
    os.startfile(newFile, 'open')
elif "n" in openFile.lower():
    print("\nClosing")
else:
    print("\nClosing")
