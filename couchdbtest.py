import couchdb

# Connect to CouchDB
server = couchdb.Server("http://admin:password@127.0.0.1:5984/")

# Create or use an existing database
db_name = "student_data"
if db_name in server:
    db = server[db_name]
else:
    db = server.create(db_name)

# Data templates
student_1 = {'name': 'Abundance', 'matno': '20cj027424'}
student_2 = {'name': 'Abundance2', 'matno': '20cj0274242'}

# Create (C)
doc_id_1 = db.save(student_1)
doc_id_2 = db.save(student_2)

# Read (R)
retrieved_student_1 = db[doc_id_1]
print("Retrieved Student 1:", retrieved_student_1)

for doc_id in db:
    doc = db[doc_id]
    print("All Documents:", doc)

# Update (U)
retrieved_student_2 = db[doc_id_2]
retrieved_student_2['name'] = 'Updated Name'
db.save(retrieved_student_2)
updated_student_2 = db[doc_id_2]
print("Updated Student 2:", updated_student_2)

# Delete (D)
del db[doc_id_1]
try:
    deleted_student_1 = db[doc_id_1]
except couchdb.http.ResourceNotFound:
    print("Student 1 deleted successfully")
