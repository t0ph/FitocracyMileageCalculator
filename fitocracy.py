"""
t0ph - 6.10.12
    
Calculates your total distance ran based on Fitocracy data export, since their site doesn't show you that metric yet.
    
To use, download this script and a CSV of you running data from Fitocracy (You ->Performance -> Running -> CSV). Put both in a directory, and run the python script.
    
Loosly based on work http://code.google.com/p/narorumo/source/browse/trunk/fitocracy/fitocracy.py?r=635
"""
    
import csv
import sys

def to_miles(dist, units):
    multiplier_table = { "mi": 1.0,
        "km": 0.621371192,
        "ft": (1 / 5280),
        "m": 0.000621371192,
        "yd": (1 / 1760) }
    asfloat = float(dist)
    multiplier = multiplier_table[units]
    return asfloat * multiplier

def main():
    csvReader = csv.reader(open("runs.csv"))
    headers = next(csvReader)
    useful = headers.index("Combined")
    combinedCSV = []
    for row in csvReader:
        combinedCSV.append(row[useful])
    runData = iter(combinedCSV)
    csvData = csv.reader(runData, delimiter='|')
    total_distance = 0
    for rowz in csvData:
        run = rowz[2]
        run = run.replace(' ', '')
        unit = run[-2:]
        dist = run[:-2]
        miles = to_miles(dist, unit)
        total_distance += miles
    print "You have run this many miles on Fitocracy:", total_distance

if __name__ == "__main__": main()