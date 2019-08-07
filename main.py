from bs4 import BeautifulSoup
import csv
import requests
import string

def remove_all(substr, str):
  index = 0
  length = len(substr)
  while string.find(str, substr) != -1:
    index = string.find(str, substr)
    str = str[0:index] + str[index+length:]
  return str

csv_file = open('output.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['date', 'pure_gold_24k', 'std_gold_22k'])

# output_rows = []
for year in range(2006, 2020, 1):
  for month in range(1, 13, 1):
    if year == 2019 and month > 6: # get current year and month
      break
    source = requests.get(f'https://www.livechennai.com/get_goldrate_history.asp?monthno={month}&yearno={year}').text
    soup = BeautifulSoup(source, 'lxml')
    goldTable = soup.find('table', class_="table-price")

    # fetch data from the table
    for table_row in goldTable.findAll('tr')[1:]:
      columns = table_row.findAll('td')
      output_row = []
      for column in columns:
        output_row.append(column.text.replace('\r', '').replace('\n', '').replace('\t', ''))
      # output_rows.append(output_row)
      print(output_row)
      csv_writer.writerow(output_row)
    # output_rows = output_rows[1:]
    # print(output_rows)

csv_file.close()
# with open('output.csv', 'w') as csvfile:
#   ffwriter = csv.writer(csvfile)
#   ffwriter.writerows(output_rows)
# csvfile.close()
