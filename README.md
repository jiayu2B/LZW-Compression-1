LZW Compression ReadME.txt


Program and Data Structure design:

The encoder and decoder are implemented in python 3.4. The dictionary is implemented using SQLite3.
SQLite3 ships by default with python 3.4. The import sqlite3 will import the library functions for sqlite3.
The great feature of sqlite3 is that it allows to create a temporary database in RAM by passing ':memory:'
paramter while creating the connection to the database.

A dict table holds the code and corresponding string value. The code if of type INTEGER and stringVal is of type TEXT.
The db_init(cur) function in encoder and decoder creates the database table and initializes the 'dict' table to initial
value of all ASCII characters ranging from 0 to 255.

The encoder reads 1 character at a time from the input file. Computes the output codes and stores them in a list.
Once the entire input file is read, the output codes are written in the output file using 16 bit binary notation.
The struct.pack() function encodes the characters in 16 bit binary.

The decoder reads 2 bytes at a time from the input lzw file and stores the value in a list. The struct.unpack() function 
decodes the 16 bit binary output.

The program works for all text files which have ASCII characters. 
The program may fail when the input file contains non ASCII characters such as '♥','♠'

Break down of files:

The LZWEncoder.py is the file for encoder. It requires 2 command line paramters, input file name and the length N.
The LZWDecoder.py is the file for decoder. It requires 2 command line paramters, input file name and the length N.  


How to Run the programs:

The programs are implemented using python 3.4. Following are the ways to run the programs on different OSs.  

Windows:
1. Open Powershell
2. set the environment variable to - [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python34") where 
   'C:\Python34' is the path is the path to your python 3.4 interpreter.
For Encoder:
3. Type in the following command in the directory of the file LZWEncoder.py : pyhton LZWEncoder.py input.txt 12 
For Decoder:
3. Type in the following command in the directory of the file LZWDecoder.py : pyhton LZWDecoder.py input.lzw 12 

Linux:
1. Open Terminal
2. Check for the python version by using the following code:
   $ python --version
   It should be 3.4   
For Encoder:
3. Type in the following command in the directory of the file LZWEncoder.py: pyhton LZWEncoder.py input.txt 12 
For Decoder:
3. Type in the following command in the directory of the file LZWDecoder.py: pyhton LZWDecoder.py input.lzw 12 
   
Where, input.txt/input.lzw is the input file and N is the max size of the dictionary
Also, the program expects the input.txt/input.lzw file in the same directory as the LZWEncoder.py/LZWDecoder.py file

