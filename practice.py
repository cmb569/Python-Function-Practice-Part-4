def max_num(a,b,c):
    return max([a,b,c])
print(max_num(40,5,10))


#/////////////////////////////

def mult_list(list):
  if len(list) == 0:
    return 0
  prod = list[0]

  if len(list) > 1:
    for i in list[1:]:
      prod = prod * i

  return prod

print(mult_list([15, 4, 5]))

#/////////////////////////////

def rev_string(my_str):
    return my_str[::-1]

print(rev_string("pirates"))

#/////////////////////////////

def num_within(x,a,b):
    return x in range(a,b+1)
print(num_within(6,14,20))     
print(num_within(50,6,50))     
print(num_within(40,10,70))

#////////////////////////////

triangle = [[1],[1,1]]
def pascal(n):

  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2

    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]

      length = len(row_prev)+1
      for i in range(length):

        if i == 0:
          row.append(1)

        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])

        else:
          row.append(1)
      triangle.append(row)
      row_number += 1


    for row in triangle:
      print(row)

pascal(2)
pascal(5)






















#https://replit.com/@cmb569/1024-solutionPython-Function-Practice-Part-4