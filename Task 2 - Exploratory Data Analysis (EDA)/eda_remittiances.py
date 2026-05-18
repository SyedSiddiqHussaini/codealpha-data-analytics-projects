import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv('worldbank_indicators.csv')

# 2. Explore Data Structure
print("--- DATASET SHAPE ---")
print(df.shape)
print("\n--- DATA TYPES & INFO ---")
df.info()

# 3. Detect Data Issues
print("\n--- MISSING VALUES ---")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# 4. Visualizations

# A. Distribution of GDP (Finding Anomalies)
plt.figure(figsize=(10, 6))
sns.histplot(df['gdp_per_capita_usd'].dropna(), bins=50, kde=True, color='skyblue')
plt.title('Distribution of GDP per Capita (USD)')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('gdp_distribution.png')
plt.show()

# B. Testing Hypothesis: Wealth vs. Health
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='gdp_per_capita_usd', y='life_expectancy_years', alpha=0.5, color='coral')
plt.title('GDP per Capita vs Life Expectancy')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Life Expectancy (Years)')
plt.xscale('log') # Log scale handles the outliers
plt.tight_layout()
plt.savefig('gdp_vs_life_expectancy.png')
plt.show()

# C. Trend Analysis: Remittances over time
plt.figure(figsize=(10, 6))
yearly_remittances = df.groupby('year')['remittances_received_usd'].sum() / 1e9
sns.lineplot(x=yearly_remittances.index, y=yearly_remittances.values, marker='o', color='green')
plt.title('Global Remittances Received Over Time')
plt.xlabel('Year')
plt.ylabel('Total Remittances Received (Billion USD)')
plt.tight_layout()
plt.savefig('remittances_trend.png')
plt.show()

# D. Correlation Heatmap
plt.figure(figsize=(10, 8))
cols_for_corr = ['gdp_per_capita_usd', 'inflation_cpi_pct', 'unemployment_pct', 
                 'population_growth_pct', 'urban_population_pct', 'life_expectancy_years']
corr_matrix = df[cols_for_corr].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Key Indicators')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()


