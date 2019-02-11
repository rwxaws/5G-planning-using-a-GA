# 5G Planning Using a Genetic Algorithm

This project tries to generate a distribution plan(s) for 5G base stations using a genetic algorithm.

Since 5G introduces types of base stations (Micro, Pico, Femto) and uses a different band(28 GHz), we must use a different approach to tackle the challenges present.

One of these challenges include the cost of deployment and maintenance of Macro base stations. This is solved by introducing the aforementioned types of cells.

This solution also solves the problem of coverage since these new cell types are cheaper and easier to deploy and maintain, moreover, they can fill the holes left by Macro cells.


# Project Structure

This project is divided as such:

- files (include all the files and directories used in this project)
  - crossover (include the crossover operators used by the genetic algorithm)
  - helper_funcs (functions that are used in the project and does NOT have an appropriate place)
    - helper.py
  - mutation (include the mutation operators used by the genetic algorithm)
  - selection (include the selection operators used by the genetic algorithm)
  - network_funcs (functions that calculate certain network related values such as: rain attenuation and the distance between cells and/or users)
  - objs (defines the classes that are used in the project)
    - user.py
    - cell.py
  - main.py (the main file, from which the algorithm is implemented)
- README.md (the file you are currently reading)