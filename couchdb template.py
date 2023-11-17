import couchdb
server = couchdb.Server('http://admin:admin@localhost:5984/')  # Replace the URL with your CouchDB server URL , REPLACE admin_user YOUR USERNAME AND admin_password with PASSWORD
#CREATE A DATABASE
db_name = 'cen434'
try:
    db = server.create(db_name)
except couchdb.http.PreconditionFailed as e:
    db = server[db_name]  # If the database already exists, use it
#WRITE DATA
data = {
    'firstname': 'damilola',#Change values
    'email': 'damilola@gmail.com'
}

doc_id, doc_rev = db.save(data)
#READ DATA
doc = db.get(doc_id)
print(doc)

#UPDATE DATA
doc = db.get(doc_id)
doc['firstname'] = 'damilola'#CHANGE VALUES
db.save(doc)


#MODIFY DATA
def modify_data(doc_id, new_data):
    doc = db.get(doc_id)
    doc.update(new_data)
    db.save(doc)

new_data = {'level': '400level'}#CHANGE VALUES
modify_data(doc_id, new_data)

#DELETE A DOCUMENT
# doc = db.get(doc_id)
# db.delete(doc)