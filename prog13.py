Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
employee_details = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})
employee_salaries = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Salary': [50000, 70000, 80000, 55000, 60000]
})
KeyboardInterrupt
sales_region_1 = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Region': ['North', 'North', 'North', 'North', 'North'],
'Sales': [250, 300, 200, 400, 350]
})


sales_region_2 = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Region': ['South', 'South', 'South', 'South', 'South'],
'Sales': [300, 320, 280, 360, 310]
})
print("Employee Details:")
Employee Details:
print(employee_details)
   EmployeeID     Name   Department
0         101    Alice           HR
1         102      Bob  Engineering
2         103  Charlie  Engineering
3         104    David           HR
4         105      Eva    Marketing
print("\nEmployee Salaries:")

Employee Salaries:
print(employee_salaries)
   EmployeeID  Salary
0         101   50000
1         102   70000
2         103   80000
3         104   55000
4         105   60000
KeyboardInterrupt
print("\nSales Region 1:")

Sales Region 1:
print(sales_region_1)
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
print("\nSales Region 2:")

Sales Region 2:
print("\nSales Region 2:")

Sales Region 2:
avg_salary_per_dept = employee_details.merge(employee_salaries,
on='EmployeeID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary_per_dept)
SyntaxError: multiple statements found while compiling a single statement
merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID',
how='inner')
print("\nMerged Employee Data:")
print(merged_data)
Joining:
    
SyntaxError: multiple statements found while compiling a single statement
print("\nSales Region 2:")

Sales Region 2:
print(sales_region_2)
        Date Region  Sales
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310
avg_salary_per_dept = employee_details.merge(employee_salaries,
on='EmployeeID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary_per_dept)
SyntaxError: multiple statements found while compiling a single statement
avg_salary_per_dept = employee_details.merge(employee_salaries,
on='EmployeeID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")

Average Salary per Department:
print(avg_salary_per_dept)
Department
Engineering    75000.0
HR             52500.0
Marketing      60000.0
Name: Salary, dtype: float64
>>> merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID',
... how='inner')
>>> print("\nMerged Employee Data:")

Merged Employee Data:
>>> print(merged_data)
   EmployeeID     Name   Department  Salary
0         101    Alice           HR   50000
1         102      Bob  Engineering   70000
2         103  Charlie  Engineering   80000
3         104    David           HR   55000
4         105      Eva    Marketing   60000
>>> import pandas as pd
>>> KeyboardInterrupt
>>> import pandas as pd
>>> import pandas as pd\
... 
... 
...        
>>> 
>>> import pandas as pd\
... 
... 
...        
