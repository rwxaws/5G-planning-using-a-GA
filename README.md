# 5G Planning Using a Genetic Algorithm

This project tries to generate a distribution plan(s) for 5G base stations using a genetic algorithm.

Since 5G introduces types of base stations (Micro, Pico, Femto) and uses a different band(28 GHz), we must use a different approach to tackle the challenges present.

One of these challenges include the cost of deployment and maintenance of Macro base stations. This is solved by introducing the aforementioned types of cells.

This solution also solves the problem of coverage since these new cell types are cheaper and easier to deploy and maintain, moreover, they can fill the holes left by Macro cells.


# Running the project
make sure you have python3+ installed as well as the following libraries
- matplotlib
- numpy

which can be installed using pip
``` py
pip3 install matplotlib numpy --user
```

to run the program make sure you are in the root of the project and run the main file as a module
``` py
python3 -m files.main
```
