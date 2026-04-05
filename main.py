# #worse approach
# f = open("hello.txt", "w")  #this helps to open the file, "w" also creates the file if it does not exist already
# f.write("Hello World!") #writing into the file we just created
# f.close()   #if we end work on the file, it is a good practice to close it to avoid the confusion in OS
#
# f = open("hello.txt", "r")  #opens the file for reading
# result = f.read()   #saves the data from reading into the "result" variable
# print(result)
# #there is no close function and therefore, the issues with the file may occur later; it is better to use a context manager
#
# #Better approach
# with open("hello2.txt", "w") as f:  #context manager helps to execute the body and will close the file automatically so we do not have to worry about unclosed file
#     f.write("Hello World")
#
# with open("hello2.txt", "r") as f:
#     result = f.read()
#     print(result)
#
# print("End!")


#import pandas

#work with data from tables
# import pandas as pd
#
# result = pd.read_csv("customers-100.csv")
#
# print("End!")
#
# d = {"name": ["Ales", "Honza"], "age": [30, 40]}    #simple dictionary
#
# new_customers = pd.DataFrame(d) #new instance of DataFrame class; input parameters - data in form of dictionary
# new_customers.to_csv("customers-new.csv", index=False)  #the content of new_customers variable will be written into the file and format given in the parenthesis

# work with json
# import json
#
# d = {"name": "Honza", "age": 5}
#
# with open("data.json", "w") as f:   #to write in json file, we need to use unique combination of context manager and the function for json files
#     json.dump(d, f)
#
# with open("data.json", "r") as f:   #to write in json file, we need to use unique combination of context manager and the function for json files
#     new_d = json.load(f)
#
# print(new_d)

#work with databasis

#simple work with DB
import pandas
from sqlalchemy import create_engine
engine = create_engine("sqlite:///C:/Users/vsvar/OneDrive/Dokumenty/Python_projects/write_read_files/mydb.sqlite", echo=False)

with engine.connect() as conn:
    d = {"name": ["Ales", "Honza"], "age": [30, 40]}
    df = pandas.DataFrame.from_dict(d)
    df.to_sql(name="Users", con=conn, if_exists="append")


