Package's Archtechiure:

ML_Challenge/
                __init__.py
                main.py
                README.rd
                requirements.txt

                data/
                    datasetName.pickle
                
                graph/
                    graph.py
                    node.py
                
                utils/
                    utils.py 
                
                test/
                    test_graph.py
                    test_node.py
                    test_utils.py


To use this project, you have to create a virtual enviroment and install the requirements as follow:

> virtualenv venvName
> source venvName/bin/activate
> pip3 install -r requirements.txt

The test directory contains unit tests, to run one of them, use the commandes
    > python3 -m unittest test_graph.py

To use the code run the following commande:
    > python3 main.py datasetName.pickle n

Note: n the minimum number of tokens shared between two nodes to have an edge between them