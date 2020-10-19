import pandas as pd

# assigns the csv file to sal as a data frame
sal = pd.read_csv(
    '/home/dm3f90/workspace/python/data_science_ml/chapter3/Salaries.csv')
# prints sal (dataframe)
print(sal)
# prints first 5 lines (default)
print(sal.head())
# Use the .info() method to find out how many entries there are.
print(sal.info())
# What is the average BasePay?
print(sal['BasePay'].mean())
# What is the highest amount of OvertimePay in the dataset?
print(sal['OvertimePay'].max())
# What is the job title of JOSEPH DRISCOLL?
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
# How much does JOSEPH DRISCOLL make (including benefits)?
joseph_driscoll = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
# prints dataframe vertically to be able to see all columns
print(joseph_driscoll.transpose())
# totalpaybenefits is the total pay including benefits
joseph_driscoll_totalbenefits = joseph_driscoll['TotalPayBenefits']
print(joseph_driscoll_totalbenefits)
# What is the name of highest paid person (including benefits)?
highest_paid_person = sal[sal['TotalPayBenefits']
                          == sal['TotalPayBenefits'].max()]['EmployeeName']
print(highest_paid_person)
# What is the name of lowest paid person (including benefits)?
lowest_paid_person = sal[sal['TotalPayBenefits']
                         == sal['TotalPayBenefits'].min()]['EmployeeName']
print(lowest_paid_person)
# What was the average (mean) BasePay of all employees per year? (2011-2014)?
print(sal.groupby('Year').mean()['BasePay'])
# How many unique job titles are there?
unique_job_titles = sal.groupby('JobTitle')
print('Unique job titles', len(unique_job_titles))
# What are the top 5 most common jobs?
five_most_common_jobs = sal['JobTitle'].value_counts().head(5)
print(five_most_common_jobs)
# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
job_titles_heldby_one_person = sum(
    sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
print(job_titles_heldby_one_person)
# How many people have the word Chief in their job title?


def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

# Bonus: Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len', 'TotalPayBenefits']].corr())
