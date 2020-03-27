import os 
os.system('mkdir -p /tmp/database')
from Main import db
db.create_all()
if db:
    print("Database Created")
