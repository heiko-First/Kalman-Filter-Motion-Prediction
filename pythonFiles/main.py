# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 16:19:20 2025

@author: heiko
"""
import numpy as np


#Data init 
xPosGroundTruth = []
yPosGroundTruth = []
xVelGroundTruth = []
yVelGroundTruth = []
g = 9.81 # grafaty [m/s*s]
v_0 = 15 # Speed of the Ball [m/s]
y_0 = 0 # [m] 
phi_grad = 30 # Throw Angle [°] 
sampleRate = 1/30 # [s] 


#Physical equations 
phi_rad = (2 * np.pi * phi_grad) / 360# [rad]

c1 = (2*y_0*g) / (v_0**2)
c2 = v_0**2 / g 
travleTime = abs(v_0/g *( np.sin(phi_rad) + np.sqrt(np.sin(phi_rad)**2 + c1) )) # [s]
travleDistanz = abs(c2 * np.cos(phi_rad) * (np.sin(phi_rad) + np.sqrt(np.sin(phi_rad)**2) + c1)) # [m]

samplelTravleTime = np.arange(0, travleTime + sampleRate, sampleRate)

for i in range(len(samplelTravleTime)): 
    t = samplelTravleTime[i]
    xPosGroundTruth.append(v_0 * np.cos(phi_rad) * t)
    yPosGroundTruth.append(-0.5 * g * t**2 + v_0*np.sin(phi_rad) * t + y_0)
    
    xVelGroundTruth.append(v_0 * np.cos(phi_rad))
    yVelGroundTruth.append(v_0 * np.sin(phi_rad) - t * g)
 