#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import fmpy
from fmpy import read_model_description, extract
from fmpy.fmi2 import FMU2Slave
from fmpy.util import plot_result, download_test_file
import shutil
import time as TIME
import keyboard


# In[2]:


fmu_filename = 'Vehicle.fmu'
fmpy.dump(fmu_filename)


# In[22]:


def simulate_custom_input(show_plot=True):
    # define the model name and simulation parameters
    start_time = 0.0
    step_size = 0.001
    stop_time = 20  
    
    # read the model description
    model_description = read_model_description(fmu_filename)
    
    # collect the value references
    vrs = {}
    for variable in model_description.modelVariables:
        vrs[variable.name] = variable.valueReference       
    
    # get the value references for the variables we want to get/set
    accel = vrs['accelCMD'] # Steering and Acceleration Commands
    steer = vrs['steerCMD']
    
    # extract the FMU
    unzipdir = extract(fmu_filename)
    
    fmu = FMU2Slave(guid=model_description.guid,
                    unzipDirectory=unzipdir,
                    modelIdentifier=model_description.coSimulation.modelIdentifier,
                    instanceName='instance1')
    
    # initialize
    fmu.instantiate()
    fmu.setupExperiment(startTime=start_time)
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()
    
    time = start_time
    
    rows = []  # list to record the results

    # simulation loop
    while time < stop_time:

        # NOTE: the FMU.get*() and FMU.set*() functions take lists of
        # value references as arguments and return lists of values

        # set the inputs                
        if keyboard.is_pressed('5'):
            fmu.setReal([accel], [1.0])
        elif keyboard.is_pressed('2'):
            fmu.setReal([accel], [-1.0])
        else:
            fmu.setReal([accel], [0.0])
        
        #fmu.setReal([steer], [0.0])
        if keyboard.is_pressed('1'):
            fmu.setReal([steer], [1.0])
        elif keyboard.is_pressed('3'):
            fmu.setReal([steer], [-1.0])
        else:
            fmu.setReal([steer], [0.0])
        
        # Aborting with Escape
        if keyboard.is_pressed('Escape'):
            break
        
        # Timing the step
        start = TIME.time()
        # perform one step
        fmu.doStep(currentCommunicationPoint=time, communicationStepSize=step_size)
        
        end = TIME.time()
        
        # get the values for 'inputs' and 'outputs[4]'
        #inputs, outputs = fmu.getReal([vr_inputs, vr_outputs])

        # append the results
        #rows.append((time, inputs, outputs))

        # advance the time and sync
        time += step_size
        if end - start < step_size:
            TIME.sleep(step_size - (end - start))

    fmu.terminate()
    fmu.freeInstance()

    # clean up
    shutil.rmtree(unzipdir, ignore_errors=True)

    # convert the results to a structured NumPy array
    #result = np.array(rows, dtype=np.dtype([('time', np.float64), ('inputs', np.float64), ('outputs', np.float64)]))

    # plot the results
    #if show_plot:
    #   plot_result(result)

    return time

# Based on the following web page
# https://github.com/CATIA-Systems/FMPy/blob/feature/clocks-and-hybrid-cs/fmpy/examples/custom_input.py


# In[25]:


simulate_custom_input()


# In[ ]:




