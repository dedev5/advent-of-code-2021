def count(values, high, low):
  for i in range(len(values[0])):
    total = 0
    for x in values:
      if x[i] == "1":
        total += 1
    check = high if total >= len(values)/2 else low

    print(values,total)
    newValues = []
    for val in values:
      if val[i] == check:
        newValues.append(val)
    values = newValues
    if len(values) == 1:
      return int(values[0],2)

def main():
  with open("data.txt",'r') as f:
    data = f.read().splitlines()
    
    oxygen_rating = count(data,"1","0")
    co2_rating = count(data,"0","1")
    print(oxygen_rating * co2_rating)


if __name__ == "__main__":
  main()
