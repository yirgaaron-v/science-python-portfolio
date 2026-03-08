import matplotlib.pyplot as plt
import csv
# 1) Where the file is (relative to main.py)
import os

base_path = os.path.dirname(__file__)
filename = os.path.join(base_path, "data", "sample.csv")

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


# Step 1: find the maximum bacteria count
max_bacteria = max(bacteria_count)

# Step 2: find the index where it occurs
max_index = bacteria_count.index(max_bacteria)

# Step 3: use the index to get the time
time_of_max = time_hr[max_index]

# Step 4: print results
print("Maximum bacteria count:", max_bacteria)
print("Occurred at time (hours):", time_of_max)

# Step 1: create a growth list
growth = [0]  # first point has no previous, so 0

# Step 2: loop through the bacteria_count starting from index 1
for i in range(1, len(bacteria_count)):
    diff = bacteria_count[i] - bacteria_count[i-1]  # current - previous
    growth.append(diff)

# Step 3: print results
for t, b, g in zip(time_hr, bacteria_count, growth):
    print(f"Time: {t} hr, Bacteria: {b}, Growth: {g}")

# Plot total bacteria over time
plt.plot(time_hr, bacteria_count, marker='o', color='green', linestyle='-', label="Total bacteria")

# Optional: plot growth per hour on same graph
plt.plot(time_hr, growth, marker='x', color='red', linestyle='--', label="Growth per hour")

# Add titles and labels
plt.title("Bacterial Growth Over Time")
plt.xlabel("Time (hours)")
plt.ylabel("Bacteria count / Growth")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()