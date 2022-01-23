# Write a Python Program to display Floyd's Triangle by using functions 


def floidtri(n):
  number = 1

  print("Floyd's Triangle") 
  for i in range(1, n + 1):
    for j in range(1, i + 1):        
        print(number, end = '  ')
        number = number + 1
    print()


rows = int(input())
floidtri(rows)

