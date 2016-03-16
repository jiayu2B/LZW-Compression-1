import sqlite3
from sys import argv
import struct
args = str(argv)

conn = sqlite3.connect(':memory:')  # Declare a SQLITE object with a database in the RAM
code_Value = 255  # initial value of a new code generated
MAX_TABLE_VALUE = pow(2, int(argv[2]))


# Function to initialize the dictionary to ascii values 0 to 255
def db_init():
    conn.execute('''CREATE TABLE dict (
        code INTEGER,
        stringVal TEXT)''')
    for k in range(0, 255):
        conn.execute("insert into dict (code,stringVal) values (?,?)", (str(k), chr(k)))

db_init()  # Initialize the dictionary
inputList = []  #
inputFile = open('G:\\UNCC\\Spring 16\\Algos\\Project\\LZW\\' + argv[1], "rb")
code = inputFile.read()

stri = '>'
print(len(code))
for i in range(int(len(code)/2)):
    stri += 'H'

inputList = struct.unpack(stri, code)
print(inputList)
index = 0


query = "select stringVal from dict where code = "+str(inputList[0])
rdr = conn.execute("select stringVal from dict where code = ?", (inputList[0],))  # conn.execute(query)
data = (rdr.fetchone())
string = str(data[0])
outputstring = string

for i in range(1, len(inputList)):
    code = inputList[i]
    #query = "select stringVal from dict where code = "+str(code)
    rdr = conn.execute("select stringVal from dict where code = ?", (code,))  # conn.execute(query)
    data = (rdr.fetchone())
    if(data == None):
        newString = string+string[:1]
    else:
        newString = str(data[0])
    print(newString)
    outputstring = outputstring+newString
    query = "select count(*) from dict"
    rdr = conn.execute(query)
    noOfEntries = rdr.fetchone()
    if(int(noOfEntries[0]) < MAX_TABLE_VALUE):
        code_Value = code_Value + 1 
        # query = "insert into dict (code, stringVal) values ("+str(code_Value)+",'"+string+newString[:1]+"')"
        conn.execute("insert into dict (code,stringVal) values (?,?)", (code_Value, string+newString[:1]))
        # conn.execute(query)
    string = newString
inputFile.close()
outputfile = open('G:\\UNCC\\Spring 16\\Algos\\Project\\LZW\\' + argv[1][:-4]+'_Decoded.txt', "w")
outputfile.write(outputstring)
outputfile.close()
print(outputstring)

conn.close()
