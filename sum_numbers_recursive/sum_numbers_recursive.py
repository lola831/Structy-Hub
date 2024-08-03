def sum_numbers_recursive(numbers):
  # if len(numbers) == 0:
  #   return 0
  # if len(numbers) == 1:
  #   return numbers[0]
  # numbers[len(numbers) - 2] += numbers.pop()
  # print(numbers)
  # sum_numbers_recursive(numbers)


  if len(numbers) == 0:
    return 0
  print(numbers[2:])
  return numbers[0] + sum_numbers_recursive(numbers[1:])
  
  
sum_numbers_recursive([5, 2, 9, 10]);