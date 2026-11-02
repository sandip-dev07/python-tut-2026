# file = open("data/example.txt", "r")
# print(file.read())
# file.close()


# mode: w: write, replace existing file:
# file = open("data/example.txt", "w")
# file.write("Hello World")
# file.close()

# mode: a: append, add to existing file:
file = open("data/example.txt", "a")
file.write(", Sandip Rocks!!")
file.close()

# file = open("data/example.txt", "r")
# print(file.read())
# file.close()


# using 'with' statement:
with open("data/example.txt", "a") as file:
    file.write("\nHow are you?")
    
with open("data/example.txt", "r") as file:
    # print(file.read())
    pass
    
    
    
# Creates or overwrites, allowing both read and write
with open("data/example2.txt", "w+") as f:
    f.write("Writing content...\n")
    
    # Move file pointer back to the beginning to read what was just written
    f.seek(0)
    # print(f.read())



# -------------------------------- CSV FILE --------------------------------
import csv

with open("data/example3.csv", "w+") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Raju", 26, "Hyderabad"])
    writer.writerow(["Reddy", 26, "Hyderabad"])
    writer.writerow(["Sandip", 26, "Hyderabad"])
    
with open("data/example3.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        pass
    
    
    
# -------------------------- JSON FILE --------------------------------
import json

data = {"name": "Sandip", "age": 26, "city": "Hyderabad"}

with open("data/example4.json", "w+") as file:
    json.dump(data, file, indent=4) # indent: indentation, 4 spaces
    
with open("data/example4.json", "r") as file:
    data = json.load(file)
    # print(data)
        
        
        
# --------------------------- Exception Handling -----------------------------
try:
    with open("data/example5.json", "r") as file:
        data = json.load(file)
        print(data)
except Exception as e:
    print(e)
    print("File not found")
finally:
    print("File closed")