# LZW Decoder: This program decodes the input lzw file using the LZW algorithm. The initial dictionary consists of
#              all the ASCII characters from 0 to 255.
# Arguments: The program needs 2 arguments, Name of the input lzw file and N: size of the code.
# Author:   Sumant Sanjay Tapas
# UNCC ID:  800905142
# Email ID: stapas@uncc.edu

import sqlite3
from sys import argv
import struct


# Function to initialize dictionary[0 to 255] = code for individual characters


def db_init(cur):
    cur.execute('''CREATE TABLE dict (
        code INTEGER,
        stringVal TEXT)''')
    for k in range(0, 255):
        conn.execute("insert into dict (code,stringVal) values (?,?)", (str(k), chr(k)))


# Main Program
# The program uses SQLite3 database to create the dictionary.
# The ':memory:' parameter specifies that the database is created in RAM and is temporary
conn = sqlite3.connect(':memory:')         # Connection object for SQLite3 DB
code_Value = 255                           # Initial value of a new code generated
MAX_TABLE_VALUE = pow(2, int(argv[2]))     # Max table value depending on the command line parameter
cur = conn.cursor()                        # Get a cursor to point to the database.

db_init(cur)                                  # Initialize the dictionary
inputList = []                             # Declare list to store the codes from the input lzw file
inputFile = open(argv[1], "rb")            # Open the Input lzw file in Read Binary mode
code = inputFile.read()                    # Read the file

stri = '>'
for i in range(int(len(code)/2)):
    stri += 'H'

inputList = struct.unpack(stri, code)     # Extract the codes from the read file
index = 0
inputFile.close()                         # Close the input file

rdr = conn.execute("select stringVal from dict where code = ?", (inputList[0],))  # Check for the first code
data = (rdr.fetchone())
string = str(data[0])                     # Assign the string value from the code
print(string)
outputstring = string

for i in range(1, len(inputList)):          # For each code in inputList
    code = inputList[i]
    rdr = conn.execute("select stringVal from dict where code = ?", (code,))  # Check if the code exists
    data = (rdr.fetchone())
    if(data == None):                   # If not found, assign newString = string + first character of string variable
        newString = string+string[:1]
    else:                               # If found, assign newString = the fetched string
        newString = str(data[0])
    print(newString)
    outputstring += newString           # Construct the output string
    query = "select count(*) from dict"  # Get the dictionary size
    rdr = conn.execute(query)
    noOfEntries = rdr.fetchone()
    if int(noOfEntries[0]) < MAX_TABLE_VALUE:  # If the dictionary size less than max size
        code_Value += 1                        # Increament the code value
        # insert the new code and string to the dictionary
        conn.execute("insert into dict (code,stringVal) values (?,?)", (code_Value, string+newString[:1]))
    string = newString

outputfile = open(argv[1][:-4]+'_Decoded.txt', "w")  # Open output file to write decoded output in write mode
outputfile.write(outputstring)                       # Write to the file
outputfile.close()                                   # Close the output file
conn.close()                                         # Close the DB connection
