
#
def dec_to_bin(number, places=15):
  whole, dec = str(number).split(".")
  whole = int(whole)
  dec = int(dec)
  res = bin(whole).lstrip("0b") + "."
  for x in range(places):
    whole, dec = str((decimal_converter(dec)) * 2).split(".")
    dec = int(dec)
    res += whole
  return float(res)

def decimal_converter(num):
  while(num>1):
    num /= 10
  return num

def bin_to_dec(binary):
  binary = str(binary)
  whole_str, *dec_str = binary.split('.')

  whole_dec = int(whole_str, 2)
  dec_dec = 0.

  if dec_str:
    for k in range(len(dec_str[0])):
      if(dec_str[0][k] == '1'):
        dec_dec = dec_dec + float(2**(-k-1))
  else:
    dec_dec = 0

  return whole_dec + dec_dec


# Call the function as : quicksort(A,0,len(A)-1)
def quicksort(A, lo, hi):
  if lo >= hi or lo < 0:
    return

  p = partition(A, lo, hi)

  quicksort(A, lo, p - 1)
  quicksort(A, p + 1, hi)

def partition(A, lo, hi):
  pivot = A[hi]
  i = lo - 1

  for j in range(lo,hi):
    if A[j]<=pivot:
      i = i + 1
      A[i], A[j] = A[j], A[i]

  i = i + 1
  A[i], A[hi] = A[hi], A[i]
  return i
