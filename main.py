import pandas
import openpyxl
import datetime

#2022-02-03T03:50:14

def date_convert(str):
    year = int(str[0:4])
    month = int(str[5:7])
    day = int(str[8:10])
    hour = int(str[11:13])
    minute = int(str[14:16])
    second = int(str[17:])
    date = datetime.datetime(year, month, day, hour, minute, second)
    return date

df = pandas.read_csv('venmo_statement.csv', header = 2)
df = df.drop(columns=df.columns[0])
df = df.drop(["ID", "Type", "Status", "Amount (tip)", "Amount (fee)", "Funding Source", "Destination",
              "Beginning Balance", "Ending Balance", "Statement Period Venmo Fees", "Terminal Location",
              "Year to Date Venmo Fees", "Disclaimer"], axis=1)
df = df.drop(0)
df.drop(df.tail(1).index,inplace=True)

#for x in range(len(df)):
 #   date_value = df.iloc[x]["Datetime"]
  #  date_value = date_value[0:10]
   # df.iat[x, 0] = date_value


master_df = pandas.read_excel(open("MasterWKB.xlsx",'rb'),sheet_name="Total Data")
prev_date = master_df["Datetime"][len(master_df)-1]
prev_date = date_convert(prev_date)


for x in range(len(df)):
    x = x+1
    cur_date = df["Datetime"][x]
    cur_date = date_convert(cur_date)
    cur_from = df["From"][x]
    if cur_date <= prev_date:
        df = df.drop(x)

master_df = pandas.concat([master_df, df])
master_df.set_index("Datetime")
master_df.drop(master_df.filter(regex="Unname"),axis=1, inplace=True)
with pandas.ExcelWriter('MasterWKB.xlsx') as writer:
    master_df.to_excel(writer, sheet_name='Total Data')









