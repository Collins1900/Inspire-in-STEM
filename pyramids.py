########################
#!/usr/bin/python
########################

# Half pyramids

rows = int(input("enter number of rows:"))
for i in range (rows):
    for j in range (i + 1):
        print("*" , end = "")
print("\n")

row = int(input("enter number of rows"))
for i in range (rows):
    for j in range(i + 1):
        print(j + 1 , end = "9")
    print("\n")