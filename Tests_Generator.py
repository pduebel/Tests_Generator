import matplotlib.pyplot as plt
from extract import extract
from graphify import graphify

test = "SHDP"
proj = "LS4010"
db = "//Desktop-4d2r7ke/GEODASYV6/GEODASY.mdb"
holes, test_data = extract(db, test, proj)
graphify(test, holes, test_data)


