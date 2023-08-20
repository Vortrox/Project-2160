#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
#!pip install openpyxl


# In[2]:


excel_file = "BITRE-Road-Vehicles-Australia-January-2023.xlsx"
working_directory = r"C:\Users\chees\OneDrive - Deakin University\Documents\ComputerScience\Hackathon"
os.chdir(working_directory)

sheet_names = pd.ExcelFile(excel_file).sheet_names


# In[3]:


# Replace "BITRE-Road-Vehicles-Australia-January-2023.xlsx" with the actual file path
excel_file = "BITRE-Road-Vehicles-Australia-January-2023.xlsx"

# Read the Excel file and get a list of sheet names (tables)
sheet_names = pd.ExcelFile(excel_file).sheet_names


# In[4]:


print(sheet_names)


# In[5]:


table_8_data = pd.read_excel(excel_file, sheet_name="Table 8")
print(table_8_data)


# In[6]:


# Drop the "Unnamed: 0" column and reset the index
table_8_data.drop(columns="Unnamed: 0", inplace=True)
table_8_data.reset_index(drop=True, inplace=True)


# In[7]:


# Rename columns
table_8_data.columns = ["Make", "2023", "2022", "2021"]


# In[8]:


print(table_8_data)

"""
Polester
BYD
Tesla are sole electric companies
"""


# In[9]:


table_8_data = table_8_data.drop(range(0, 8))#removing the top 8 lines so that I can utilise the data


# In[10]:


print(table_8_data)


# In[27]:


# Transpose the DataFrame to have years as columns
df_transposed = table_8_data.set_index('Make').T
# Reverse chronological Order
df_transposed = df_transposed[::-1]

# List of distinct colors
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'orange', 'purple', 'brown', 'pink', 'gray', 'lime']


# Plotting the transposed data
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
df_transposed.plot(marker='o', color=colors)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.title('Registered Electric Vehicle Production by Year (2021-2023)')
plt.xticks(rotation=0)  # Keep x-axis labels as years

# Adding legend
plt.legend(title='Make')

# Display the plot
plt.tight_layout()
plt.show()


# In[18]:



# Filter out the "Total" row from the data
filtered_data = table_8_data[table_8_data["Make"] != "Total"]

# Extract the data for each year
years = ["2023", "2022", "2021"]
ev_counts = filtered_data[years]

# Define custom colors for specific categories
category_colors = ["blue", "green", "red", "purple", "orange", "cyan", "magenta", "yellow", "teal", "pink", "gray"]

# Plot a pie chart for each year
for year in years:
    plt.figure(figsize=(8, 8))  # Increase the figure size for better spacing
    plt.pie(ev_counts[year], colors=category_colors, startangle=140)
    plt.title(f"Electric Vehicles Distribution for Year {year}")
    
    # Add a legend
    plt.legend(filtered_data["Make"], loc="upper right")

    # Adjust legend placement to prevent overlap
    plt.tight_layout()

    plt.axis("equal")  # Equal aspect ratio ensures that the pie is drawn as a circle.
    plt.show()


# In[24]:


# Assuming your DataFrame is already loaded as 'table_8_data'

# Select the data for a specific make (e.g., 'Tesla')
make_data = table_8_data[table_8_data['Make'] == 'Tesla']
#Reverse Order

# Set the index as years and convert the values to numeric
make_data = make_data.set_index('Make').T
make_data = make_data.apply(pd.to_numeric, errors='coerce')
make_data = make_data[::-1]

# Fit an ARIMA model
p, d, q = 1, 1, 1  # Example ARIMA order parameters
model = ARIMA(make_data, order=(p, d, q))
model_fit = model.fit()

# Make predictions for future years
future_years = [2024, 2025, 2026]  # Years to predict
forecast = model_fit.forecast(steps=len(future_years))


# Plot historical data
plt.figure(figsize=(10, 6))
plt.plot(make_data.index, make_data.values, label='Historical Data')
plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.title('Vehicle Production History for Tesla')
plt.legend()
plt.tight_layout()

# Show the historical data plot
plt.show()

# Plot forecasted data
plt.figure(figsize=(10, 6))
plt.plot(future_years, forecast, label='Forecast', linestyle='dashed', marker='o', color='orange')
plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.title('Vehicle Production Forecast for Tesla')
plt.legend()
plt.tight_layout()

# Set x-axis to display integers only
plt.xticks(future_years, future_years)
# Show the forecasted data plot
plt.show()


# In[26]:


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Assuming your DataFrame is already loaded as 'table_8_data'
# ... (rest of the code remains the same)

# Select the data for a specific make (e.g., 'Tesla')
make_data = table_8_data[table_8_data['Make'] == 'Tesla']
# Reverse Order

# Select the data for a specific make (e.g., 'Tesla')
make_data = table_8_data[table_8_data['Make'] == 'Tesla']
# Reverse Order

# Set the index as years and convert the values to numeric
make_data = make_data.set_index('Make').T
make_data = make_data.apply(pd.to_numeric, errors='coerce')
make_data = make_data[::-1]

# Fit an ARIMA model
p, d, q = 1, 1, 1  # Example ARIMA order parameters
model = ARIMA(make_data, order=(p, d, q))
model_fit = model.fit()

# Make predictions for future years
future_years = [2024, 2025, 2026]  # Years to predict
forecast = model_fit.forecast(steps=len(future_years))

# Plot historical data and forecasted data
plt.figure(figsize=(10, 6))

# Plot historical data
plt.plot(make_data.index, make_data.values, label='Historical Data')

# Plot forecasted data
plt.plot(list(make_data.index) + future_years, list(make_data.values) + list(forecast), 
         label='Forecast', linestyle='dashed', marker='o', color='orange')

# Set x-axis labels
x_labels = list(make_data.index) + future_years
plt.xticks(range(len(x_labels)), x_labels, rotation=45)

plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.title('Vehicle Production History and Forecast for Tesla')
plt.legend()
plt.tight_layout()

# Show the combined data plot
plt.show()


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Assuming your DataFrame is already loaded as 'table_8_data'
# ... (rest of the code remains the same)

# Select the data for a specific make (e.g., 'BYD')
make_data = table_8_data[table_8_data['Make'] == 'BYD']
# Reverse Order

# Select the data for a specific make (e.g., 'Tesla')
make_data = table_8_data[table_8_data['Make'] == 'BYD']
# Reverse Order

# Set the index as years and convert the values to numeric
make_data = make_data.set_index('Make').T
make_data = make_data.apply(pd.to_numeric, errors='coerce')
make_data = make_data[::-1]

# Fit an ARIMA model
p, d, q = 1, 1, 1  # Example ARIMA order parameters
model = ARIMA(make_data, order=(p, d, q))
model_fit = model.fit()

# Make predictions for future years
future_years = [2024, 2025, 2026]  # Years to predict
forecast = model_fit.forecast(steps=len(future_years))

# Plot historical data and forecasted data
plt.figure(figsize=(10, 6))

# Plot historical data
plt.plot(make_data.index, make_data.values, label='Historical Data')

# Plot forecasted data
plt.plot(list(make_data.index) + future_years, list(make_data.values) + list(forecast), 
         label='Forecast', linestyle='dashed', marker='o', color='orange')

# Set x-axis labels
x_labels = list(make_data.index) + future_years
plt.xticks(range(len(x_labels)), x_labels, rotation=45)

plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.title('Vehicle Production History and Forecast for Tesla')
plt.legend()
plt.tight_layout()

# Show the combined data plot
plt.show()


# In[28]:


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Assuming your DataFrame is already loaded as 'table_8_data'
# ... (rest of the code remains the same)

# Select the data for a specific make (e.g., 'BYD')
make_data = table_8_data[table_8_data['Make'] == 'BYD']
# Reverse Order

# Select the data for a specific make (e.g., 'Tesla')
make_data = table_8_data[table_8_data['Make'] == 'BYD']
# Reverse Order

# Set the index as years and convert the values to numeric
make_data = make_data.set_index('Make').T
make_data = make_data.apply(pd.to_numeric, errors='coerce')
make_data = make_data[::-1]

# Fit an ARIMA model
p, d, q = 1, 1, 1  # Example ARIMA order parameters
model = ARIMA(make_data, order=(p, d, q))
model_fit = model.fit()

# Make predictions for future years
future_years = [2024, 2025, 2026]  # Years to predict
forecast = model_fit.forecast(steps=len(future_years))

# Plot historical data and forecasted data
plt.figure(figsize=(10, 6))

# Plot historical data
plt.plot(make_data.index, make_data.values, label='Historical Data')

# Plot forecasted data
plt.plot(list(make_data.index) + future_years, list(make_data.values) + list(forecast), 
         label='Forecast', linestyle='dashed', marker='o', color='orange')

# Set x-axis labels
x_labels = list(make_data.index) + future_years
plt.xticks(range(len(x_labels)), x_labels, rotation=45)

plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.title('Vehicle Production History and Forecast for Tesla')
plt.legend()
plt.tight_layout()

# Show the combined data plot
plt.show()


# In[ ]:


#Conclusion because the data is limited to 3 points only the data will only give us a linear projection. With more data for the registered EV's a predictive model can be made


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




