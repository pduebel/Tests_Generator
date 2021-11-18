# geodasy-tests-generator

Python script to extract geotechnical test data from a MS Access database, used by GEODASY logging software, using user supplied test type and project id.

# Screenshots

<figure><figcaption>Example HP/SV graph.</figcaption><img src='https://user-images.githubusercontent.com/56090238/142058525-09e7bbcb-f1f6-48ef-ab45-4cf532b9a1f3.png' alt='Example shear vane graph' width=400></figure> <figure><figcaption>Example SHDP/SPT graph</figcaption><img src='https://user-images.githubusercontent.com/56090238/142058623-10389326-f6dc-415e-b9e9-c78c80086f16.png' alt='Example dynamic probe graph' width=400></figure>

# Installation

Dependencies:

* Matplotlib
* Pyodbc

To install these libraries run the following commands in the terminal:
```
pip install pyodbc
pip install matplotlib
```

Then to clone the repository:
```
git clone https://github.com/pduebel/geodasy-tests-generator.git
```

# Usage

To create the graphs, first open up `test_graph_generator.py` and change the configuration variables:

* `test` - the type of test you want to create a graph for, can be HP, SV, SHDP, or SPT
* `proj` - the id of the project you'd like to create the graphs for, as recorded in GEODASY
* `db` - the filepath to the MS Access database that is used by the GEODASY software

Then, simply run `test_graph_generator.py` and save your graphs.

