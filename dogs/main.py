import configparser
import os

configuration = configparser.ConfigParser()
configuration.read("configuration.ini")

print(configuration["FILE_SETTINGS"]["output_filepath"])

print(os.environ.get("SECRET_USERNAME"))

print("End")