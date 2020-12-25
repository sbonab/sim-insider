# Vehicle Dynamics Model FMU 
# Introduction
I have used a python script to run an FMU of a vehicle on an uneven terrain. This happens real-time using the keyboard keys. 
FMPy library instantiates and runs the FMU forward in time. 
MapleSim Insight takes care of the visualization. 
FMU of the vehicle is generated from a MapleSim model, `Vehicle_Model.msim`.
I have modeled the vehicle dynamics using a 16 DOF (6 for the chassis, 4 independent suspension, 2 steering, 4 spin axes) vehicle model and Pacejka 2012 tires from the MapleSim Tire library.

## Instructions
The following instructions are for Windows operating system. To be able to run the Python script, you’d need to install the required libraries. To do this:
* Create a new conda environment.
* Conda activate the newly created env.
* Fully install the FMPy using the following command line:

`conda install -c conda-forge fmpy`

https://fmpy.readthedocs.io/en/latest/install/
* Install the keyboard and jupyter notebook:

`pip install keyboard`

`conda install –c conda-forge jupyterlab`

* With the new env activated, open a jupyter notebook session and browse to `NFS.ipynb`.
* Make sure that you have a working MapleSim Insight installation. Evaluating the cell with `simulate_custom_input()` should invoke an Insight session. Alternatively, you can open `Vis.simData` first where the visualization windows are set for you. Run the script, use the 5,2,1,and 3 Numpad keys to control the vehicle and have fun!

Checkout an example video output here

https://www.youtube.com/watch?v=vfkOTaQvEC4&ab_channel=SimInsider
