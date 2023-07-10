#Exercise 1
#import csv
#
#with open("January.csv") as file:
#  reader = csv.reader(file)
#
#  for row in reader:
#    print(", ".join(row))

#Exercise 2
#import csv
#
#with open("January.csv") as file:
#  reader = csv.DictReader(file)
#
#  total = 0
#  for row in reader:
#    print (row["Net Total"])
#    total += float(row["Net Total"])
#  print(f"\nTotal: {total}")

# Fix My Code
#import csv # Imports the csv library

#with open("January.csv") as file: 
#  reader = csv.DictReader(file) 
#  total = 0
  
#  for row in reader: 
#    print (", ".join(row.values()))
#    total += float(row["Net Total"]) 
    
#print(f"Total: {total}")

#Day 54 Challenge
import csv

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)

  total = 0
  for row in reader:
    revenue = float(row["Cost"])*int(row["Quantity"])
    total += revenue
  total = round(total, 2)

  print(f"{'Shop Tracker':^45}")
  print()
  print(f"Your shop took £{total} today.")