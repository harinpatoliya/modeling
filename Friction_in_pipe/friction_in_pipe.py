# This code model a head loss calculation due to friction in pipe system.
#Author Harin Patoliya

#libaries
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#Data
mass_flowrate = 1.5 # (kg/s)
g = 9.81 # acceleration due to gravity (m/s^2)
diameter = 0.127 # pipe diameter (m)
e_by_d = 0.05 # roughness factor
effe_length = 375 # effective length of pipe system (m)

#fluid properties of 98% sulphuric acid at normal temperature and pressure
rho = 1830 # density (Kg/m^3)
mu = 26.7e-3 # viscosity (Pa.s)

#basic calculation
area = (np.pi*diameter**2)/4
velocity = mass_flowrate/(area*rho)
Re = diameter*velocity*rho/mu

#equation

#colebrook correlation
def colebrook_corr(f, e_by_d, Re):
    return (1/np.sqrt(f))+2*np.log10((e_by_d/3.7)+2.51/(Re*np.sqrt(f)))

#friction factor calculation
def friction_factor(Re, e_by_d):
    if Re < 2000:
       f = 64/Re
       return f
    else:
       f_guess = 0.02
       f = fsolve(colebrook_corr, f_guess, args=(e_by_d, Re))
       return f[0]    

# Darcy-weisbach equation for head loss
def head_loss(Re, e_by_d, effe_length, diameter, velocity, g):
    return friction_factor(Re, e_by_d)*(effe_length/diameter)*(velocity**2/(2*g))

#head loss calculation
head_loss_cal = head_loss(Re, e_by_d, effe_length, diameter, velocity, g) #(m)

print(f"Head loss in pipe system is {head_loss_cal:.3f} m")

# effect of reynolds number on head loss
laminar_Re = np.linspace(500, 1501, 100)
turbulent_Re = np.linspace(5000, 25001, 1000)

head_loss_laminar = []
head_loss_turbulent = []

#Head loss calculation in laminar flow condition
for i in laminar_Re:
    velocity = i*mu/(diameter*rho)
    hl = head_loss(i, e_by_d, effe_length, diameter, velocity, g)
    head_loss_laminar.append(hl)

#Head loss calculation in turbulent flow condition
for i in turbulent_Re:
    velocity = i*mu/(diameter*rho)
    hl = head_loss(i, e_by_d, effe_length, diameter, velocity, g)
    head_loss_turbulent.append(hl)
    
#Plotting results for laminar region
plt.figure()
plt.plot(laminar_Re, head_loss_laminar, label='Laminar Flow', color='blue')
plt.xlabel('Reynolds Number (Re)')
plt.ylabel('Head Loss (m)')
plt.title('Head Loss vs Reynolds Number')
plt.legend()
plt.grid(True)
plt.show()

#Plotting results for turbulent region
plt.figure()
plt.plot(turbulent_Re, head_loss_turbulent, label='Turbulent Flow', color='red')

plt.xlabel('Reynolds Number (Re)')
plt.ylabel('Head Loss (m)')
plt.title('Head Loss vs Reynolds Number')
plt.legend()
plt.grid(True)
plt.show()

#Generation of Moody's chart
Re_range = np.logspace(3, 8, 1000)  # from 1e3 to 1e8 on a log scale
e_by_d_range = [0.05, 0.03, 0.01, 0.009, 0.008, 0.005, 0.002]

plt.figure(figsize=(10, 6))

# Loop through each relative roughness and calculate friction factor vs Re
for roughness in e_by_d_range:
    f_vals = [friction_factor(Re, roughness) for Re in Re_range]
    plt.plot(Re_range, f_vals, label=f'ε/D = {roughness}')

# Add laminar line (f = 64 / Re)
laminar_range = np.linspace(500, 2000, 200)
f_laminar = [64/Re for Re in laminar_range]
plt.plot(laminar_range, f_laminar, label='Laminar Flow (f = 64/Re)', color='black', linestyle='--')

# Final plot settings
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Reynolds Number (Re)')
plt.ylabel('Friction Factor (f)')
plt.title("Moody Chart")
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

