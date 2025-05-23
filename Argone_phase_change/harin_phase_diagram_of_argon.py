#p-T diagram of Argon
#Author :- Harin Patoliya
#Referance for data and equation ::- https://doi.org/10.1063/1.556037

#Import requried libaries

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import csv
from tabulate import tabulate

#reading csv file and extracting required data

with open("Argon_Data.csv", "r") as csvfile:

     reader = csv.reader(csvfile, delimiter=",")
     next(reader, None)

     for line in reader:for i in range(2):
         print('')
         if line[0] == 'T_triple':
            T_triple = float(line[1])

         elif line[0] == 'P_triple':
              P_triple = float(line[1])

         elif line[0] == 'T_fus':
              T_fus = float(line[1])

         elif line[0] == 'T_boil':
              T_boil = float(line[1])

         elif line[0] == 'T_critic':
              T_critic = float(line[1])

         elif line[0] == 'P_critic':
              P_critic = float(line[1])

         else:
              print('Upload correct file')

#display data
print('Following data is read from file')
print('')


a = [T_triple, P_triple, T_fus, T_boil, T_critic, P_critic]


data = list(zip(a))
transposed_data = list(zip(*data))

headers = ['T_triple(K)', 'P_triple(Pa)', 'T_fus(K)', 'T_boil(K)', 'T_critic(K)', 'P_critic(Pa)']

table_transposed = tabulate(transposed_data, headers, tablefmt="pretty")

print(table_transposed)

normal_P = 101325 # Pa
normal_T = 298.15 # K


v_press = [P_triple, normal_P, P_critic]
v_pressure = [j/100000 for j in v_press]                                          #experimental vapor line pressure data(bar)
v_temperature = [T_triple, T_boil, T_critic]                                      #experimental vapore line temperature data(K)


#define antoine equation
def AntoineEquation(temperature_K, A, B, C):
    a = 10**(A - B / (C + temperature_K))
    return a

#Antoine Equation parameter from NIST databank for Temperature range 83.78 - 150.72 K

A = 3.29555
B = 215.24
C = -22.233

initial_guess = [A, B, C]                                                        #intial gause value of Antoine Eqation to reduce itteration step

value,_ = curve_fit(AntoineEquation, v_temperature, v_pressure, p0=initial_guess)    #curvefitting

A_fit, B_fit, C_fit = value                                                     #extraction of suitable value of antoine parameters from curve fitting



temperature_fit = np.linspace(T_triple, T_critic, 100)
pressure_fit = 10**5 *AntoineEquation(temperature_fit, A_fit, B_fit, C_fit)     #new vapore pressure data according to new antoine parameters

for i in range(2):
    print('')


print(f"Fitted Antoine parameters A  = {A_fit}, B  = {B_fit}, C  = {C_fit}")

for i in range(2):
    print('')

#Hardy melting line

for i in range(2):
    print('')
def Hardymeltline(temp): 

    a1 = -7476.2665
    a2 = 9959.0613
    return (1 + a1 * ((temp/T_triple)**1.05 - 1) + a2 * ((temp/T_triple)**1.275 - 1)) * P_triple

#calculation of melting pressure
melting_temp = np.linspace(T_triple, 1.2 * T_triple, 150)
melting_press = Hardymeltline(melting_temp)

#Chen sublimation line

def Chensublimationline(sub_temp):

    a1 = -11.391604
    a2 = -0.39513431
    return P_triple * np.exp((T_triple/sub_temp) * (a1 * (1 - (sub_temp/T_triple)) + a2 * (1 - (sub_temp/T_triple)**2.7)))

#calculation of sblimation pressure
sublim_temp = np.linspace(60, T_triple, 20)
sublim_press = Chensublimationline(sublim_temp)

#Gilgen vapor pressure line
def Gilgenvaporline(temp):

    a1 = -5.9409785
    a2 = 1.3553888
    a3 = -0.46497607
    a4 = -1.5399043

    return P_critic * np.exp((T_critic/temp)*(a1*(1-(temp/T_critic))+a2*(1-(temp/T_critic))**1.5+a3*(1-(temp/T_critic))**2+a4*(1-(temp/T_critic))**4.5))

#calculation of vapor presssure
vapor_temp = np.linspace(T_triple, T_critic, 100)
vapor_press = Gilgenvaporline(vapor_temp)

#plotting p-T diagram

plt.plot(temperature_fit, pressure_fit, label='Fitted Antoine Equation')
plt.plot(vapor_temp, vapor_press, label = 'Gilgen Vapor pressure line', linestyle = '--', zorder=2.5, color='black')
plt.plot(sublim_temp, sublim_press, label = 'Chen Sublimation line')
plt.plot(melting_temp, melting_press, label = 'Hardy Melting line')
plt.yscale('log')

#adding markers

plt.scatter(T_boil, normal_P, color='black', zorder=2.5)
plt.scatter(T_fus, normal_P, color='blackfor i in range(2):
    print('')', zorder=2.5)
plt.scatter(T_critic, P_critic, color='#8B00FF', zorder=2.5)
plt.scatter(T_triple, P_triple, color='#8B00FF', zorder=2.5)

#plotting of auxalary lines

plt.axhline(y=100000, xmin=0, xmax=0.32, color='black', linestyle='dotted')
plt.axhline(y=68891.0, xmin=0, xmax=0.3, color='black', linestyle='dotted')
plt.axvline(x=83.8058, ymin=0 , ymax=0.41, color='black', linestyle='dotted')
plt.axvline(x=87.3033, ymin=0 , ymax=0.45, color='black', linestyle='dotted')

#adding text

plt.text(65, 555555, "SOLID")
plt.text(85, 555555, "LIQUID")
plt.text(120, 555555, "GAS")
plt.text(81.0, 1000, "83.8K", rotation=90)
plt.text(87.9, 1000, "87.3K", rotation=90)
plt.title('p-T diagram of Argon')


plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (Pa)')
plt.legend()
plt.show()

for i in range(2):
    print('')
print('--->It is clear from the p-T that Antoine eqation with fitted parameters and a Gilgen equation both give same result.')


#calculating vapor pressure using experimental antoine parameters from NIST.

temperature = np.linspace(T_triple, T_critic, 100)
pressure = 10**5 * AntoineEquation(temperature, A, B, C)

plt.plot(temperature, pressure, label ='Original Antoine equation')
plt.plot(vapor_temp, vapor_press, label = 'Gilgen equation')
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (Pa)')
plt.legend()
plt.title('Comparison of two model from experimental value')

print('--->It can be concluded from comparison that at higher temperature( >130 K ) there is deviation in vapor pressure and for temperature ( <130 K ) both equations estimate almost same values.')