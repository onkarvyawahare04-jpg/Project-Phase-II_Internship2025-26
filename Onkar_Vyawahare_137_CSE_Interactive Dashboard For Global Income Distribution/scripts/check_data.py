import pandas as pd
df = pd.read_excel(r'c:\Users\onkar\Desktop\infosys springboard virtual internship (1)\Mastersheet_Infosys.xlsx')
with open('data_info_master.txt', 'w') as f:
    f.write(f"Total Countries Analyzed: {df['Country_Name'].nunique()}\n")
    f.write(f"Data Timespan: {df['year'].min()} to {df['year'].max()}\n")
    f.write(f"Average Gini Index: {round(df['Gini_Index (0-100)'].mean(), 2)}\n")
    f.write(f"Average Income Share Lowest 20%: {round(df['Income Share_Lowest 20%'].mean(), 2)}%\n")
    f.write(f"Average Income Share Highest 20%: {round(df['Income Share_Highest 20%'].mean(), 2)}%\n")
    f.write(f"Average Unemployment Rate: {round(df['Unemployement_Rate (%)'].mean(), 2)}%\n")
