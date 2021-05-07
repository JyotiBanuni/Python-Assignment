import pandas as pd

def readEmployeesDetails(fileName):
    data = pd.read_csv(fileName, sep='\t')
    df = pd.DataFrame(data)
    fmt = '%H:%M'
    hourly_wage = 100
    df['new_endTime'] = pd.to_datetime(df['DailyEndTime'], format=fmt, errors='coerce').dt.hour
    df['new_startTime'] = pd.to_datetime(df['DailyStartTime'], format=fmt, errors='coerce').dt.hour
    df['Salary'] = (df['new_endTime'] - df['new_startTime'])*hourly_wage
    return df

def getEmployeesSalary(data):
    sumofSalaries = data.groupby(by=['EmployeeId'], as_index=False)['Salary'].sum()
    return sumofSalaries


TotalSalary = getEmployeesSalary(readEmployeesDetails("C:\\Users\dell\\Documents\\EmployeesDetails.tsv"))
df = pd.DataFrame(TotalSalary)
df.to_csv("C:\\Users\dell\\Documents\\EmployeesSalary.tsv",index=False, sep='\t')
print("Salary has been inserted into EmployeesSalary File !!")
