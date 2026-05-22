import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fatal-police-shootings-data.csv')
print()

# create a crosstab to analyze the relationship between race and signs of mental illness
crosstab = pd.crosstab(df['race'], df['signs_of_mental_illness'])
print(crosstab)

# calculate the percentage of cases with signs of mental illness for each race using the apply method on the crosstab
mental_illness_pct = crosstab.apply(lambda row: (row[True] / row.sum() * 100).round(2), axis=1)
print("\nMental illness percentage by race:")
print(mental_illness_pct)

# Add new column to crosstab with mental_illness_pct values for each race
crosstab['Mental_Illness_Pct'] = mental_illness_pct
print("\nCrosstab with Mental_Illness_Pct column:")
print(crosstab)

print(f"\nHighest rate: {mental_illness_pct.idxmax()} with {mental_illness_pct.max()}%")

# Add a column to crosstab indicating the day of the week on which the intervention occurred.
df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()
interventions_by_day = df['day_of_week'].value_counts()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
interventions_by_day = interventions_by_day.reindex(day_order)

print("\nInterventions by day of week:")   
print(interventions_by_day)

crosstab= pd.crosstab(
    df['race'], 
    [df['signs_of_mental_illness'], df['day_of_week']]
)

crosstab_final = crosstab.reindex(
    columns=[(item, day) for item in [False, True] for day in day_order],
    fill_value=0
)

print("\nCrosstab with mental illness and day of week:")
print(crosstab_final)

# create a bar chart to visualize the number of interventions by day of the week
interventions_by_day.plot(kind='bar', figsize=(10, 6))
plt.title('Interventions by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Interventions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('interventions_by_day.png', dpi=300, bbox_inches='tight')


