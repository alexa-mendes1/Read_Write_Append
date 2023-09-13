# 3) reads the sales.csv file and creates a new file with the customer ID
# and calculated total (as shown in salesreport.csv)

# Import csv module
import csv

# Open and prepare files
read_file = open('sales.csv', 'r')
csv_file = csv.reader(read_file)
write_file = open('salesreport.csv', 'w')

# Write headers for new file
write_file.write(f'Customer ID, Total\n')

#initialize variables
cust_id = '250'
total = 0
next(csv_file)

#write to file 
for rec in csv_file:
    if cust_id == rec[0]:
        total += float(rec[3]) + float(rec[4]) + float(rec[5])
    else:
        write_file.write(f'{cust_id}, {total:.2f}\n')
        cust_id = rec[0]
        total = float(rec[3]) + float(rec[4]) + float(rec[5])
write_file.write(f'{cust_id}, {total:.2f}')

#Close files
read_file.close()
write_file.close()