import csv


customers_read = open('customers.csv', 'r')
csv_file = csv.reader(customers_read)

outfile = open('customer_country.csv', 'w')
outfile.write(f"Full Name, Country\n")

counter = 0
next(csv_file)
for rec in csv_file:
    line = f"{rec[1]} {rec[2]}, {rec[4]}\n"
    outfile.write(line)
    counter += 1

outfile.close()
customers_read.close()

print(f"total number of customers: {counter}")


# next(csv_file)  #Skip a row

# for rec in csv_file:
#     print(rec)
#     print(f"First name: {rec[1]}")
#     print(f"last name: {rec[2]}")
#     input()