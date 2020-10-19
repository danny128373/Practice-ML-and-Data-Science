import pandas as pd

# Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.
ecom = pd.read_csv(
    '/home/dm3f90/workspace/python/data_science_ml/chapter3/Ecommerce Purchases')
# Check the head of the DataFrame.
print(ecom.head())
# How many rows and columns are there?
print(len(ecom.columns))
print(len(ecom.index))
# What is the average Purchase Price?
print(ecom['Purchase Price'].mean())
# What were the highest and lowest purchase prices?
print(ecom[ecom['Purchase Price'] ==
           ecom['Purchase Price'].max()]['Purchase Price'])
print(ecom[ecom['Purchase Price'] ==
           ecom['Purchase Price'].min()]['Purchase Price'])
# How many people have English 'en' as their Language of choice on the website?
print(ecom[ecom['Language'] == 'en'].count()['Language'])
# How many people have the job title of "Lawyer"?


def contains_lawyer(title):
    if 'lawyer' in title.lower().split():
        return True
    else:
        return False


print(sum(ecom['Job'].apply(lambda x: contains_lawyer(x))))
# How many people made the purchase during the AM and how many people made the purchase during PM?
print(ecom[ecom['AM or PM'] == 'PM']['AM or PM'])
# What are the 5 most common Job Titles?
print(ecom['Job'].value_counts().head())
# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
print('Purchase Price:', ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
# What is the email of the person with the following Credit Card Number: 4926535242672853
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])
# How many people have American Express as their Credit Card Provider and made a purchase above $95?
print(len(ecom[(ecom['CC Provider'] == 'American Express') &
               (ecom['Purchase Price'] > 95)].index))
# Hard: How many people have a credit card that expires in 2025?
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))
# Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
ecom['Email Providers'] = ecom['Email'].apply(lambda x: x.split('@')[1])
print(ecom['Email Providers'].value_counts().head())
