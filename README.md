# scicomp-p2-migration
Scientific Computing Project 2: Volatile Migration and Loss of Water and Carbon Dioxide on Mercury

This project is intended to detail the proporiton of molecules lost to process such as photoionization, photodissociation, and thermal escape. Due to Mercury being close to the sun, many molecules do not reach stability. This project is intended to investigate the main causes of loss and the significance of each process.

## Dependencies and Repository Overview
To run the software, you will need the following libaries:
* matplotlib
* numpy
* scipy
* ipykernel

All of the libraries are included in the `requirements.txt` file and can be installed by entering the following into terminal:

```bash
pip install -r requirements.txt
```

The repository has a set of 5 Python script files located in the `src` folder and a Jupyter Notebook for running the simulation.

## agent.py
`agent.py` is script containing the class setup for the volatile simulation for the various features a volatile will have such as temperature, position, velocity, launch angle, and travel time.

## expectation.py
`expectation.py` is script containing functions for caculating statistical parameters for the simulation after it has been executed such as mean and standard deviation. It also contains the function for running the simulation.

## helpers.py
`helpers.py` is script which contains a set of helper functions that aid in kinematic calculation for the traveling volatiles.

## migrate.py
`migrate.py` is script containing functions for the various methods of loss in the simulation such as photodestruction, Jeans escape, and cold trap loss.

## model.py
`model.py` is script containing all of the functions for visualizing the data

## migration.ipynb
`migration.ipynb` is a Jupyter notebook containing a computational essay explaining the modeling abstractions and decisions as well as a way to run the model and a reflection on the results. All of the initial conditions listed in the paper have been placed in the notebook, and all relevant design decisions have been explained.

To run the simulation, you may run through all the cells in `migration.ipynb` to get all of the proper figures

If you have any questions, please feel free to reach out to Kevin Lie-Atjam (klieatjam@olin.edu)
