########################
#!/usr/bin/python
########################

# first n terms of AP

a = int(input("enter first number"))
d = int(input("enter common difference"))
n = int(input("enter number of terms"))

for i in range(1, n + 1):
    n_term = a + (i - 1)*d
    print(n_term)