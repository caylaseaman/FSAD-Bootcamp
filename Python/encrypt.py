file = open('toEncrypt.txt', 'r')
lines = file.readlines()
f = open("Encrypted.txt", "w")


for line in lines:
  for char in line:
    f.write(chr(ord(char) + 1))
  f.write("\n")


f.close()
