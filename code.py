import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    r'C:\population-analysis-2020\population-dataset\API_SP.POP.TOTL_DS2_en_csv_v2_127006.csv',
    skiprows=4
)


print("Columns are:", data.columns.tolist())

population_data = data[['Country Name', '2022']].dropna()


top_10 = population_data.sort_values(by='2022', ascending=False).head(10)

print(top_10)

plt.figure(figsize=(10, 6))
plt.bar(top_10['Country Name'], top_10['2022'], color='skyblue')
plt.title('Top 10 Countries by Population (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(population_data['2022'], bins=20, color='green', edgecolor='black')
plt.title('Population Distribution of Countries (2022)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()




