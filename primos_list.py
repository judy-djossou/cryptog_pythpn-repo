def primaute(x):
  r=1
  for div in range(2, x):
    r = x%div
    if r == 0:
      return False
      break
  return True
var = int(input(f"Entrez la porté: "))
for a in range(1, var+1):
  if primaute(a):
    if a ==1:
      continue
    print(a, end=", ")
