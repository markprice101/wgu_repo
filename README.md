# wgu_repo
WGU Assignments - D598 Task 2

The Python application ‘D598 Task2.py’ represents all original work, there were no citable references made.
The Python application ‘D598 Task2.py’ has four defined functions to complete the required tasks:
1.	remove_duplicates
a.	This function takes the data frame and removes any rows that are not unique.
2.	filter_negative_debt_to_equity
a.	This function removes any rows of the data frame that have a negative value for the ‘Debt to Equity’ column within the data frame
3.	descriptive_stats_and_grouping
a.	This function takes the data frame, groups the rows by State, then calculates the Mean, Min, Max, and Median of the numeric columns within the original data frame and then creates a new data frame with the States and the descriptive statistics
4.	calculate_debt_to_income
a.	This function takes the data frame and returns an indexed calculated value for ‘Debt to Income’
In the Main Execution Block the application imports an excel file (specifically ‘D598 Data Set.xlsx’) into a Data Frame (‘df’), then calls the remove_duplicates function, then calls the filter_nagative_debt_to_equity function, then calls the destriptive_stats_and_grouping function, then calls the calculate_debt_to_income function, then concatenates the newly created column to the original data frame.

