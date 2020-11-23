import pandas as pd
#Read the transaction File
anon_df = pd.read_csv("D:\Meniga\Anon_transactions_sample.csv")

print('Reg:1>>How many transactions happened at ATG for a particular day?')
#Include only the merchant name = 'ATG'
atg_df = anon_df[anon_df['network_merchant_name'].str.match("ATG")]
#Get the transaction count for ATG Merchant
atg_count_df = atg_df.value_counts(['transaction_date', 'network_merchant_name']).reset_index(name='ATG_count')
#Display the ATG transactions for the day.
print(atg_count_df)

#Read Categories files
cat_df = pd.read_csv("D:\Meniga\categories.csv")
#Merge the category file with the transaction file for mapping category and subcategory names
merged_df = anon_df.merge(cat_df[["subcategory_id","subcategory_name","category_id","category_name"]],
                          on="subcategory_id", how="left")

#Obtain the most transactions for the day with category
print('Reg:2>>Which category had the most transactions for a particular day?')


cat_trans_category_df = merged_df.value_counts(['transaction_date','category_name']).reset_index(name='trans_count')

print('Category having most transaction per day:')
print(cat_trans_category_df)

print('Reg:3>>Which hours during the day were the busiest in total?')
#Change the object to datetime value.
date_anon_df = anon_df['authorization_time'] = pd.to_datetime(anon_df['authorization_time'],errors='coerce')
date_anon_df = anon_df.dropna(subset=['authorization_time'])

#get the most hour count for the day in total
hour_anon_count = date_anon_df.authorization_time.dt.hour.value_counts().reset_index(name='hours_count')
print(hour_anon_count.head(1))

print('Reg:4>>Which days of the week were the busiest in total? For a single merchant?')

anon_df['transaction_date'] = pd.to_datetime(anon_df['transaction_date'],errors='coerce').dt.day_name()

week_df = anon_df.groupby(anon_df.transaction_date).network_merchant_name.value_counts()
print(week_df.head(1))

