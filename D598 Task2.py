#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:19:13 2026

@author: Mark Price - WGU SID: 012784323
"""

import pandas as pd
import numpy as np

# Function to remove duplicate data
def remove_duplicates(df):
    return df.drop_duplicates()

# Function for grouping by state and generating descriptive statistics
def descriptive_stats_and_grouping(df):
    # using 'Business State' as the column name for grouping
    target_cols = ['Total Long-term Debt', 'Total Equity', 'Debt to Equity', 'Total Liabilities', 'Total Revenue', 'Profit Margin']
    return df.groupby('Business State')[target_cols].agg(['mean', 'min', 'max', 'median']) 

# Function to calculate Debt-to-Income ratio
def calculate_debt_to_income(df):
    # Calculation: Long Term Debt / Total Revenue 
    df['Debt to Income'] = np.where(
        df['Total Revenue'] != 0,
        df['Total Long-term Debt'] / df['Total Revenue'],
        0
    )
    return df

# Function to filter out negative Debt-to-Equity ratios
def filter_negative_debt_to_equity(df):
    return df[df['Debt to Equity'] >= 0]

# Main execution block
try:
    # 1. Import File (D598 Data Set.xlsx) into data_frame
    df = pd.read_excel('D598 Data Set.xlsx')

    # 2. data_frame_unique = CALL Duplicate Data Removal
    df = remove_duplicates(df)

    # 3. data_frame_by_state_stat = CALL Descriptive Statistics and Grouping
    df2 = descriptive_stats_and_grouping(df)

    # 4. data_frame_unique = CALL Calculate Debt-to-Income
    df = calculate_debt_to_income(df)

    # 5. data_frame_unique = CALL Filter Out Negative Debt-to-Equity
    df = filter_negative_debt_to_equity(df)

    print("Data processing successful.")
    
except FileNotFoundError:
    print("Error: 'D598 Data Set.xlsx' not found. Ensure the file is in the script's directory.")