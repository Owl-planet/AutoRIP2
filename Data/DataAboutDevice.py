import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
mydb = client("Cisco")
info = mydb.CiscoVerisi

record = {
    # Cisco bilgileri
}

# Tam olarak bitmedi...