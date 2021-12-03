
def main():
  with open("data.txt",'r') as f:
    data = f.read().splitlines()
    total = [0]*12
    for value in data:
      for i, char in enumerate(value):
        if char == "1":
          total[i] += 1

    total = [1 if val >= len(data)/2 else 0 for val in total] 
    neg_total = [1 if val == 0 else 0 for val in total]
    print(total,neg_total)
    gamma = int(''.join(str(x) for x in total),2)
    epsilon = int(''.join(str(x) for x in neg_total),2)
    print(gamma,epsilon)
    print(gamma*epsilon)

if __name__ == "__main__":
  main()
