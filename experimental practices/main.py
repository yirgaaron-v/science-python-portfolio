import csv

# 1) Where the file is (relative to main.py)
filename = "data/sample.csv"

# 2) Create empty lists (these will be filled from the CSV)
time_hr = []
bacteria_count = []

# 3) Open the file and read it as CSV
with open(filename, mode="r", newline="") as b:
    reader = csv.DictReader(b)  # uses the first row (headers) as keys

    # 4) Go through each row (each row is a dictionary)
    for row in reader:
        # row looks like: {"time_hr": "0", "bacteria_count": "100"}

        # 5) Convert text -> numbers, then add to lists
        time_hr.append(float(row["time_hr"]))
        bacteria_count.append(float(row["bacteria_count"]))

# 6) Prove it worked
print("time_hr:", time_hr)
print("bacteria_count:", bacteria_count)
print("rows read:", len(time_hr))



def calculated_growth_mean(bacteria_count):
    totall = 0
    for x in bacteria_count:
        totall += x
    return totall  / len(bacteria_count)
print(calculated_growth_mean(bacteria_count))

def find_above_mean(bacteria_count, mean):
    above_mean= []
    for x in bacteria_count:
        if x > mean :
            above_mean.append(x)
    return above_mean
print(find_above_mean(bacteria_count, calculated_growth_mean(bacteria_count)))