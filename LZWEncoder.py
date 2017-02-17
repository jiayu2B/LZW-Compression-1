# LZW Encoder: This program encodes the input text file using the LZW algorithm. The initial dictionary consists of
#              all the ASCII characters from 0 to 255.
# Arguments: The program needs 2 arguments, Name of the input text file and N: size of the code
# Author:   Sumant Sanjay Tapas
# UNCC ID:  800905142
# Email ID: stapas@uncc.edu


from sys import argv
import struct


#  Function to initialize dictionary[0 to 255] = code for individual characters

# Main Program
# The program uses SQLite3 database to create the dictionary.
# The ':memory:' parameter specifies that the database is created in RAM and is temporary

code_Value = 255                    # Initial value of the code if a new code is to be added
intOutputCode = []                  # List to hold the output codes
index = 0

dictionary = {}
for k in range(0, 256):
    dictionary.update({chr(k): k})
# print(dictionary)
string = None  # Initialize the string to null
outputFileName = argv[1][:-3]+"lzw"         # Output file name
outputfile = open(outputFileName, "wb")     # Open the output file in Write Binary mode

MAX_TABLE_VALUE = pow(2, int(argv[2]))  # Max table value depending on the command line parameter
filename = argv[1]                      # Input file name
fileObj = open(filename, "r")           # Open the file in Read mode
result = fileObj.read()
for c in result:

    symbol = c
    if string != None:
        param = string+symbol  # If not first character, add the new symbol to the existing string and assign it to the param
    else:
        param = symbol         # Else if it is the first character, assign the new symbol to param
    if param in dictionary:
        string = param
    else:
        if string in dictionary:
            code = dictionary[string]
            outputfile.write(struct.pack('>H', int(code)))
        size = len(dictionary)
        if size < MAX_TABLE_VALUE:  # If size < Max dictionary size, insert the new code
            code_Value += 1                        # Increament the code value
            dictionary.update({param: code_Value})
        string = symbol
if string in dictionary:
    code = dictionary[string]
    outputfile.write(struct.pack('>H', int(code)))


outputfile.close()  # Close the output file
fileObj.close()
