def unscramble(letters):
  file = open('words.txt', 'r')
  lines = file.readlines()
  li = []
  for line in lines:
    line = line.strip()
    if(sorted(letters) == sorted(line)):
      li.append(line)
      
      
  return li

print(unscramble("eilnst"))
     