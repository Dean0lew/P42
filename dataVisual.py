import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TUData.csv')
df1 = df['VEHICLE_REGISTRATIONYEAR']
plt.hist(df1, bins=32, range=[1990,2022], ec='black')
plt.title('Registration Years of Fleet',fontsize=22)
plt.xlabel('Year')
plt.ylabel('Number of Cars')
plt.show()



df2 = df['VehicleModel'].value_counts()[:10].index.tolist()
counts = df['VehicleMake'].value_counts().to_dict()

# Get the Keys and store them in a list
labels = list(counts.keys())

# Get the Values and store them in a list
values = list(counts.values())

plt.pie(values, autopct='%1.1f%%', labels=labels)
plt.show()

