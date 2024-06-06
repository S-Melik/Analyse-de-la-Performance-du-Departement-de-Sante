import random
from datetime import datetime
import calendar
import string
import pandas as pd
import numpy as np
from faker import Faker

# Constants
NUM_DECLARATIONS = 30000
DUPLICATE_FRACTION = 0.01
NUM_BLANK_ROWS = 10

# City population data
CITY_POPULATION = {
    "Casablanca": 7000000,
    "Marrakech": 1500000,
    "Fes": 1300000,
    "Agadir": 900000,
    "Tanger": 900000,
    "Khouribga": 400000,
    "Rabat": 2000000
}

def select_city():
    """Selects a city with probabilities based on population."""
    total_population = sum(CITY_POPULATION.values())
    probabilities = [population / total_population for population in CITY_POPULATION.values()]
    return random.choices(list(CITY_POPULATION.keys()), weights=probabilities, k=1)[0]

def simulate_monthly_declarations():
    """Simulates declaration frequency for each month."""
    month_probabilities = {
        1: 1.1,  # January
        2: 1.0,  # February
        3: 0.9,  # March
        4: 1.0,  # April
        5: 1.1,  # May
        6: 1.2,  # June
        7: 1.0,  # July
        8: 0.9,  # August
        9: 1.0,  # September
        10: 1.3, # October
        11: 1.4, # November
        12: 2.0  # December
    }
    return random.choices(range(1, 13), weights=list(month_probabilities.values()), k=NUM_DECLARATIONS)

def generate_random_dates():
    """Generates random dates within the year 2023 based on monthly probabilities."""
    months = simulate_monthly_declarations()
    days_in_months = [calendar.monthrange(2023, month)[1] for month in months]
    random_days = [random.randint(1, days) for days in days_in_months]
    return [datetime(2023, month, day) for month, day in zip(months, random_days)]

# Initialize Faker
fake = Faker()

# Generate unique 7-digit numbers for declarations
declarations = list(range(7548695, 7548695 + NUM_DECLARATIONS))

# Generate random dates
dates_reception = generate_random_dates()

# Policy distribution with exact counts
policies = {
    "2000GPT4587": 5000,
    "2000GPT2564": 3000,
    "2000GPT4118": 7000,
    "2000GPT9898": 2000,
    "065487956": 10000
}

# Create a list for policies ensuring the correct distribution
policies_list = []
for policy, count in policies.items():
    policies_list.extend([policy] * count)

# If there are not enough policies to match NUM_DECLARATIONS, add more randomly chosen policies
if len(policies_list) < NUM_DECLARATIONS:
    additional_policies = random.choices(list(policies.keys()), k=NUM_DECLARATIONS - len(policies_list))
    policies_list.extend(additional_policies)

# Ensure the length of policies_list matches NUM_DECLARATIONS
policies_list = policies_list[:NUM_DECLARATIONS]
random.shuffle(policies_list)  # Shuffle to mix the policies

# Code maladie distribution
codes_maladie_counts = {
    '001': 1000,
    '002': 700,
    '003': 3000,
    '004': 2000,
    '005': 1000,
    '006': 1500,
    '007': 1000,
    '008': 4000,
    '009': 2000,
    '010': 500,
    '011': 800,
    '012': 3000,
    '013': 900,
    '014': 500,
    '015': 600
}
codes_maladie = []
for code, count in codes_maladie_counts.items():
    codes_maladie.extend([code] * count)
random.shuffle(codes_maladie)

# Ensure the length of codes_maladie matches NUM_DECLARATIONS
if len(codes_maladie) < NUM_DECLARATIONS:
    additional_codes = random.choices(list(codes_maladie_counts.keys()), k=NUM_DECLARATIONS - len(codes_maladie))
    codes_maladie.extend(additional_codes)
codes_maladie = codes_maladie[:NUM_DECLARATIONS]

# Frais engages distribution per policy
frais_engages_distribution = {
    '2000GPT4587': (500, 1500),
    '2000GPT2564': (1500, 3000),
    '2000GPT4118': (3000, 5000),
    '2000GPT9898': (5000, 7000),
    '065487956': (7000, 10000)
}

def generate_frais_engages(policy, code_maladie):
    base_low, base_high = frais_engages_distribution[policy]
    code_variation = int(code_maladie)  # Simple variation based on code_maladie
    return np.random.randint(base_low + code_variation * 10, base_high + code_variation * 10)

frais_engages = [generate_frais_engages(policy, code) for policy, code in zip(policies_list, codes_maladie)]

# Ensure the length of frais_engages matches NUM_DECLARATIONS
if len(frais_engages) < NUM_DECLARATIONS:
    additional_frais = frais_engages[:NUM_DECLARATIONS - len(frais_engages)]
    frais_engages.extend(additional_frais)
frais_engages = frais_engages[:NUM_DECLARATIONS]

# Generate Adhérent CIN values with potential duplicates
adherent_cins = ["BE" + ''.join(random.choices(string.digits, k=2)) + ''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(NUM_DECLARATIONS)]

# Create a mapping for Adherent CIN to Adherent ville
adherent_info = {}
for cin in adherent_cins:
    if cin not in adherent_info:
        adherent_info[cin] = {
            'Adherent ville': select_city()
        }

# Ensure that adherent info stays the same for duplicates
adherent_villes = [adherent_info[cin]['Adherent ville'] for cin in adherent_cins]

# Assign policies from the policies_list
polices = policies_list[:NUM_DECLARATIONS]

# Create DataFrame
data = {
    'Declaration': declarations,
    'Date reception': dates_reception,
    'Frais engages': frais_engages,
    'Adherent CIN': adherent_cins,
    'Adherent ville': adherent_villes,
    'Police': polices,
    'Code maladie': codes_maladie
}

df = pd.DataFrame(data)

# Generate duplicate rows (1% of the original dataset)
num_duplicates = int(DUPLICATE_FRACTION * NUM_DECLARATIONS)
duplicate_rows = df.sample(n=num_duplicates, replace=True)
df = pd.concat([df, duplicate_rows], ignore_index=True)

# Add blank rows
blank_rows = pd.DataFrame({}, index=range(NUM_BLANK_ROWS))
df = pd.concat([df, blank_rows], ignore_index=True)

# Shuffle DataFrame
df = df.sample(frac=1).reset_index(drop=True)

# Print policy distribution
policy_distribution = df['Police'].value_counts()
print("Policy Distribution:")
print(policy_distribution)

# Print code maladie distribution
code_maladie_distribution = df['Code maladie'].value_counts()
print("\nCode Maladie Distribution:")
print(code_maladie_distribution)

# Print average frais engages per policy
average_frais_engages = df.groupby('Police')['Frais engages'].mean()
print("\nAverage Frais Engages per Policy:")
print(average_frais_engages)

# Print code maladie distribution for each policy
code_maladie_per_policy = df.groupby('Police')['Code maladie'].value_counts().unstack().fillna(0)
print("\nCode Maladie Distribution per Policy:")
print(code_maladie_per_policy)

# Save the DataFrame to a CSV file in the current directory
df.to_csv('data_table2023.csv', index=False)

print("Data generation completed and saved to 'data_table2023.csv'")
