<number><char>


for example, '2c' or '3a'.
uncompress("2c3a1t") # -> 'ccaaat'
uncompress("4s2b") # -> 'ssssbb'
uncompress("2p1o5p") # -> 'ppoppppp'
uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
def uncompress(s):
  nums = "0123456789"
  num = ""
  word = ""
  for char in s:
    if char in nums:
      print("here ", char)
      num += char
      print("num ", num)
    else:
      word += int(num) * char
      num = ""
      print("word ", word)
  return word
      
      
    


uncompress("2c3a1t") # -> 'ccaaat'



