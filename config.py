from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = {
    'dbname': os.environ['DBNAME'],
    'user':os.environ['DBUSER'],
    'password':os.environ['DBPASS'],
    'host' : os.environ['DBHOST'],
    'port' : os.environ['DBPORT']
}