from distutils import command
from importlib.resources import path
import json
from os import name
from pathlib import Path 
from difflib import get_close_matches
import sqlite3

from pyrsistent import v



with sqlite3.Connection("sql.db") as cnn:
    data = Path ('data.json').read_text()
    data_dict = json.loads(data) 
    crr = cnn.cursor()
    for k,v in data_dict.items():
        v=str(v)
        crr.execute("INSERT INTO dict values(?,?)",(k,v))
    cnn.commit()


data = Path ('data.json').read_text()
data_dict = json.loads(data)    
names = {}

a = input("please enter your word:")
with sqlite3.Connection("sql.db") as cnn:
    crr = cnn.cursor()
    crr.execute("SELECT * FROM dict")  
    for rows in crr:
        names.update({rows[0]:rows[1]})




if a in names.keys():
    print(names[a])
else:
    b = get_close_matches(a,(names.keys()))
    print (b[0],"is that you mean?")
    a1 = input("y/n:")
    if a1 == 'y':
        print(names[b[0]])
    else:
        print("sory we cannot find the word")






            





 

