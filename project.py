import numpy as np
from matplotlib import pyplot as plt
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
#I am taking driver as input variable to note down the activity corresponds to them.
#In antecedent fuction i am taking input as number of hours the person driving the vehicle as
#it helps me to calculate the fatique value of an driver.
Driver=ctrl.Antecedent(np.arange(0,13,1),'driver')
relative_speed =ctrl.Antecedent( np.arange(0, 101, 1) ,'speed') # Relative speed in mph
distance =ctrl.Antecedent( np.arange(0, 101, 1),'distance')#distance in meters
#i am taking output as collison_risk
collision_risk=ctrl.Consequent(np.arange(0,101,1),"collision risk")
#defining memebership function
Driver['poor']=fuzzy.trimf(Driver.universe,(5,8,12))
Driver['average']=fuzzy.trapmf(Driver.universe,(5,7,9,12))
Driver['good']=fuzzy.trimf(Driver.universe,(1,3,6))
distance['close']=fuzzy.trimf(distance.universe,(0, 0, 50))
distance['moderate']=fuzzy.trimf(distance.universe,(0, 50, 100))
distance['far']=fuzzy.trimf(distance.universe,(50, 100, 100))
relative_speed['slow']=fuzzy.trimf(relative_speed.universe,(0,0,50))
relative_speed['medium']=fuzzy.trimf(relative_speed.universe,(0,50,100))
relative_speed['high']=fuzzy.trimf(relative_speed.universe,(50,100,100))
#for individual view
Driver.view()
distance.view()
collision_risk.automf(3)
collision_risk.view()
#Defining fuzzy rule
rule1=ctrl.Rule(Driver['poor']|distance['close']|relative_speed['high'],collision_risk['good'])
rule2=ctrl.Rule(Driver['poor']|distance['moderate']|relative_speed['high'],collision_risk['good'])
rule3=ctrl.Rule(Driver['poor']|distance['far']|relative_speed['high'],collision_risk['average'])
rule4=ctrl.Rule(Driver['good']|distance['close']|relative_speed['high'],collision_risk['average'])
rule5=ctrl.Rule(Driver['good']|distance['moderate']|relative_speed['high'],collision_risk['poor'])
rule6=ctrl.Rule(Driver['good']|distance['far']|relative_speed['high'],collision_risk['good'])
rule7=ctrl.Rule(Driver['average']|distance['close']|relative_speed['high'],collision_risk['good'])
rule8=ctrl.Rule(Driver['average']|distance['moderate']|relative_speed['medium'],collision_risk['poor'])
rule9=ctrl.Rule(Driver['average']|distance['moderate']|relative_speed['slow'],collision_risk['poor'])
wm=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
wm_1=ctrl.ControlSystemSimulation(wm)
#passing user input values to the fuzzy logic
wm_1.input['driver']=8
wm_1.input['distance']=20
wm_1.input['speed']=50
wm_1.compute()
print(wm_1.output['collision risk'])
collision_risk.view(sim =wm_1)



