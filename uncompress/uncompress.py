def uncompress(s):
  nums = "0123456789"
  num = ""
  word = ""
  for char in s:
    if char in nums:
      num += char
    else:
      word += int(num) * char
      num = ""
  return word
      
      
    


uncompress("2c3a1t") # -> 'ccaaat'



