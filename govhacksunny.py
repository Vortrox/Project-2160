#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Looking at the Motor Vehicle Census 2020 - ABS
motorCensus2020 = pd.read_excel('absmotorvehiclecensus2020.xlsx', header=[0, 1], index_col=[0, 1])
print(motorCensus2020)


# In[2]:


# Data dictionary
data = {
    'Leaded': [268626, 211379, 203724],
    'Unleaded': [11640435, 12186795, 12266226],
    'Total Petrol': [11909061, 12398174, 12469950],
    'Diesel': [1322395, 1850759, 1948298],
    'Other': [317993, 255215, 261001],
    'All fuel types': [13549449, 14504148, 14679249]
}

# Years
years = [2015, 2019, 2020]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Passenger Vehicles on Register')

# Adding a legend
ax.legend()

plt.savefig('passenger_register.png')

# Display the plot
plt.show()



# In[3]:


# Data dictionary
data = {
    'Leaded': [6014, 4483, 4134],
    'Unleaded': [12586, 16794, 16767],
    'Total Petrol': [18600, 21277, 20901],
    'Diesel': [37653, 46860, 49862],
    'Other': [2035, 1616, 1457],
    'All fuel types': [58288, 69753, 72220]
}

# Years
years = [2015, 2019, 2020]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Camper Vans on Register')

# Adding a legend
ax.legend()

plt.savefig('campervan_register.png')

# Display the plot
plt.show()




# In[4]:


data = {
    'Leaded': [81926, 60440, 58094],
    'Unleaded': [1139868, 966356, 924958],
    'Total': [1221794, 1026796, 983052],
    'Diesel': [1561423, 2194162, 2340491],
    'Other': [123789, 92460, 83473],
    'All fuel types': [2907006, 3313418, 3407016]
}

# Years
years = [2015, 2019, 2020]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Light Commercial Vehicles')

# Adding a legend
ax.legend()

plt.savefig('lightcommercial_register.png')

# Display the plot
plt.show()



# In[5]:


data = {
    'Leaded': [3342, 2466, 2327],
    'Unleaded': [4817, 4310, 4383],
    'Total': [8159, 6776, 6710],
    'Diesel': [130634, 158496, 168379],
    'Other': [1832, 1700, 1591],
    'All fuel types': [140625, 166972, 176680]
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Light Rigid Trucks on Register')

# Adding a legend
ax.legend()

plt.savefig('lightrigid_register.png')

# Display the plot
plt.show()



# In[6]:


data = {
    'Leaded': [10651, 7218, 6684],
    'Unleaded': [3738, 3323, 3222],
    'Total': [14389, 10541, 9906],
    'Diesel': [315940, 341893, 347492],
    'Other': [1370, 1325, 1436],
    'All fuel types': [331699, 353759, 358834]
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Heavy Rigid Trucks on Register')

# Adding a legend
ax.legend()
plt.savefig('heavyrigid_register.png')

# Display the plot
plt.show()


# In[7]:


data = {
    'Leaded': [270, 183, 183],
    'Unleaded': [902, 742, 703],
    'Total': [1172, 925, 886],
    'Diesel': [93647, 101913, 104008],
    'Other': [156, 200, 243],
    'All fuel types': [94975, 103038, 105137]
}


# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Articulated Trucks on Register')

# Adding a legend
ax.legend()

plt.savefig('articulatedtrucks_register.png')


# Display the plot
plt.show()


# In[8]:


data = {
    'Leaded': [1226, 915, 833],
    'Unleaded': [1685, 1558, 1466],
    'Total': [2911, 2473, 2299],
    'Diesel': [20007, 21847, 22261],
    'Other': [443, 349, 281],
    'All fuel types': [23361, 24669, 24841]
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Non-Freight Vehicles on Register')

# Adding a legend
ax.legend()

plt.savefig('nonfreight_register.png')

# Display the plot
plt.show()


# In[9]:


data = {
    'Leaded': [474, 290, 278],
    'Unleaded': [17067, 16598, 16031],
    'Total': [17541, 16888, 16309],
    'Diesel': [73528, 78731, 80822],
    'Other': [4080, 3760, 3342],
    'All fuel types': [95149, 99379, 100473]
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Buses on Register')

# Adding a legend
ax.legend()

plt.savefig('bus_register.png')

# Display the plot
plt.show()


# In[10]:


data = {
    'Leaded': [45481, 39339, 38577],
    'Unleaded': [761612, 830026, 840555],
    'Total': [807093, 869365, 879132],
    'Diesel': [0, 78, 67],  # Placeholder values, replace with actual data
    'Other': [122, 662, 1682],
    'All fuel types': [807215, 870105, 880881]
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Motorcycles on Register')

# Adding a legend
ax.legend()
plt.savefig('motorcycles_register.png')

# Display the plot
plt.show()


# In[11]:


data = {
    'Leaded': [418010, 326713, 314834],
    'Unleaded': [13582710, 14026502, 14074311],
    'Total': [14000720, 14353215, 14389145],
    'Diesel': [3555227, 4794739, 5061680],
    'Other': [451820, 357287, 354506],
    'All fuel types': [18007767, 19505241, 19805331]
}


# Create a figure and axis
fig, ax = plt.subplots()

# Plot each fuel type
for fuel_type, values in data.items():
    ax.plot(years, values, marker='o', label=fuel_type)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Vehicles')
ax.set_title('Total Vehicles on Register')

# Adding a legend
ax.legend()

plt.savefig('total_vehicles_register.png')

# Display the plot
plt.show()


# In[21]:


data = {
    'Passenger': [2.346907243, 1.759600081, 1.778026928],
    'Campervans': [3.491284656, 2.316746233, 2.017446691],
    'Light Commercial': [4.258298744, 2.790471954, 2.450032521],
    'Light Rigid': [1.302755556, 1.018134777, 0.900498076],
    'Heavy Rigid': [0.413025062, 0.374548775, 0.400185044],
    'Articulated Trucks': [0.164253751, 0.194103146, 0.231127006],
    'Non-Freight Carrying': [1.896322931, 1.414731039, 1.131194396],
    'Buses': [4.288011435, 3.783495507, 3.326266758],
    'Motorcycles': [0.015113693, 0.076082772, 0.190945201],
    'Total Vehicles': [2.509028465, 1.831748708, 1.789952412]
}

# Years (same as before)
years = [2015, 2019, 2020]

# Plotting
plt.figure(figsize=(12, 8))

# Creating line plots for each vehicle type (same as before)
for vehicle_type, values in data.items():
    plt.plot(years, values, marker='o', label=vehicle_type)

plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Percentage of Other Fuel Registered Vehicles')

# Adjusting legend position outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(True)
plt.xticks(years)  # Set x-axis ticks to be the years

plt.tight_layout()  # Ensures everything fits within the figure


plt.savefig('percent_other_fuels_register.png')
plt.show()






# In[33]:


# Provided data
data = {
    'Passenger vehicles': 14726967,
    'Motor cycles': 893484,
    'Light commercial vehicles': 3412459,
    'Rigid trucks': 521255,
    'Articulated trucks': 104442,
    'Non-freight carrying trucks': 23518,
    'Buses': 86393
}


# Plotting
# plt.figure(figsize=(8, 8))

# Data to plot (same as before)
sizes = list(data.values())

# Plotting the pie chart
wedges, _ = plt.pie(sizes)

# Creating the legend without labels inside the pie chart
plt.legend(wedges, data.keys(), title="Vehicle Types", loc="center left", bbox_to_anchor=(1, 0.5))
plt.title("Distribution of Vehicles in 2020")
plt.axis('equal')


# Adjust the layout to prevent cutoff of the legend
plt.tight_layout()

plt.savefig('2020_vehicle_makeup_pie.png')
plt.show()


# In[42]:


data = {
    'Petrol': 130781.9,
    'Diesel': 27329.6,
    'Electric': 69.1,
    'LPG/hybrid and other': 4802.7
}

# States
states = ['Australia']

# Plotting
plt.figure(figsize=(10, 6))

# Creating a bar chart with a different shade of blue
plt.bar(data.keys(), data.values(), color='#3498db')  # Using a different shade of blue

plt.xlabel('Fuel Type')
plt.ylabel('Total Kilometres Travelled (million)')
plt.title('Total Kilometres Travelled in Australia 2021')

# Adding data labels on the bars
for key, value in data.items():
    plt.text(key, value, f'{value:.1f}', ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('2021_barchart_total_km_travelled.png')
plt.show()








# In[41]:


data = {
    'Petrol': 10.5,
    'Diesel': 13.9,
    'Electric': 11.1,
    'LPG/CNG/dual fuel/hybrid and other': 17.0
}

# States
states = ['Australia']

# Plotting
plt.figure(figsize=(10, 6))

# Creating a bar chart with a different shade of blue
plt.bar(data.keys(), data.values(), color='#3498db')  # Using a different shade of blue

plt.xlabel('Fuel Type')
plt.ylabel('Average Kilometres Travelled (thousands)')
plt.title('Average Kilometres Travelled in Australia in Thousands')

# Adding data labels on the bars
for key, value in data.items():
    plt.text(key, value, f'{value:.1f}', ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('2021_barchart_avg_km_travelled.png')
plt.show()


# In[ ]:




