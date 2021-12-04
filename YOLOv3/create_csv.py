import csv
import os

data = []

files = os.listdir("C:\\Users\\Kabir\\Desktop\\Images")  #Path to dir with xml files

for i in files:
    string = str(i[-10:-4])
    data.append([string + ".jpg", string + ".txt"])

print(data)

with open('C:\\Users\\Kabir\\Desktop\\train.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the data
    writer.writerows(data)
