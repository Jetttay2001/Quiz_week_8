import matplotlib.pyplot as plt
import sqlite3
        
years = []
co2 = []
temp = []

# STart using the DB
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Taking the data from the database
cursor.execute("SELECT year, co2, temperature FROM ClimateData")

# Iterate through the results and populate the lists
for row in cursor.fetchall():
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# End of use for the database
conn.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
