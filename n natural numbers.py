num=int(input("enter a number:"))
if num<0:
  print("enter number")
else:
  sum_numbers=0
  count = 1
  while count <= num:
    sum_numbers += count
    count += 1
  print("the sum of natural numbers is:",sum_numbers)
