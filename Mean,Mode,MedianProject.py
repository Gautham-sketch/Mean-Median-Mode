import csv
from collections import Counter

with open("SOCR-HeightWeight.csv",newline='') as f:
    reader = csv.reader(f)
    list_data = list(reader)

list_data.pop(0)

whole_data = []
for i in range(len(list_data)):
    full_list = list_data[i][2]
    list_data.append(float(full_list))

#Calculating the mean
length = len(whole_data)
total = 0
for x in whole_data :
    total += x

mean = total/length

print("Mean of weight is -> " + str(mean))

#Calculating the median
whole_data.sort()
if length % 2 == 0:
    median1 = float(whole_data[length//2])
    median2 = float(whole_data[length//2 - 1])
    median = (median1 + median2)/2
else :
    median = whole_data[length//2]

print("Median is -> "+ str(median))

#Calculating the mode
data = Counter(whole_data)
mode_range_of_data = {
    "75-85" : 0,
    "85-95" : 0,
    "95-105" : 0
}
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_range_of_data["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_range_of_data["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_range_of_data["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")