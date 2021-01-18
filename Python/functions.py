def primes(n):
  for x in range(2, n + 1):
    for i in range(2,x):
      if x % i == 0:
        break
    else:
      print(x)
      
def prime_factorization(n):
  #find primes in n
  factors = []
  prime = []
  for x in range(2, n + 1):
    for i in range(2,x):
      if x % i == 0:
        break
    else:
      prime.append(x)
  #go through list and divide
  
  while n > 1:
    for num in prime:
      while n % num == 0:
        factors.append(num)
        n /= num
  return factors
      
def my_sort(li):
  for i in range(len(li)-1):
    for j in range(i+1,len(li)):
      if(li[i] > li[j]):
        temp = li[j]
        li[j] = li[i]
        li[i] = temp
  return li



print(my_sort([3,2,1]))
  
  
