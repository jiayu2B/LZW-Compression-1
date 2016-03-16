import sqlite3
from sys import argv
import struct


conn = sqlite3.connect(':memory:')
code_Value = 255
intOutputString = []
index = 0


def db_init(cur):
    cur.execute('''CREATE TABLE dict (
        code INTEGER,
        stringVal TEXT)''')
    for i in range(0, 255):
        conn.execute("insert into dict (code,stringVal) values (?,?)", (str(i), chr(i)))


cur = conn.cursor()
db_init(cur)

string = None


MAX_TABLE_VALUE = pow(2, int(argv[2]))
filename = "G:\\UNCC\\Spring 16\\Algos\\Project\\LZW\\" + argv[1]
fileobj = open(filename, "r")
while True:
    c = fileobj.read(1)
    if(not c):
        break
    else:
        symbol = c
        if string != None:
            param = string+str(symbol)
        else:
            param = str(symbol)
        query = "select count(*) from dict where stringVal = '"+param+"'"
        rdr = conn.execute("select count(*) from dict where stringVal = ?", (param,))
        count = rdr.fetchone()
        if int(count[0]) > 0:
            string = param
        else:
            query = "select code from dict where stringVal = '"+string+"'"
            # rdr = conn.execute(query)
            rdr = conn.execute("select code from dict where stringVal = ?", (string,))
            codeVal = rdr.fetchone()
            intOutputString.insert(index, int(codeVal[0]))
            print(int(codeVal[0]))
            query = "select count(*) from dict"
            rdr = conn.execute(query)
            noOfEntries = rdr.fetchone()
            if int(noOfEntries[0]) < MAX_TABLE_VALUE:
                code_Value += 1
                conn.execute("insert into dict (code,stringVal) values (?,?)", (str(code_Value), param))
            string = symbol
    index += 1
query = "select code from dict where stringVal = '"+string+"'"
codeVal1 = conn.execute("select code from dict where stringVal = ?", (string,))# conn.execute(query)

final = codeVal1.fetchone()
print(int(final[0]))
intOutputString.insert(index, int(final[0]))
print(intOutputString)


outputFileName = "G:\\UNCC\\Spring 16\\Algos\\Project\\LZW\\"+argv[1][:-3]+"lzw"
outputfile = open(outputFileName, "wb")

for i in range(len(intOutputString)):
    outputfile.write(struct.pack('>H', intOutputString[i]))


outputfile.close()
fileobj.close()
cur.close()
#conn.close()
