import matplotlib.pyplot as plt
from extract import extract
from graphify import graphify

db = "GEODASY.mdb"
holes, test_data = extract(db, "HP", "LS4170")
graphify(holes, test_data)


