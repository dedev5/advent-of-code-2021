# x  : A
# x+1: A B
# x+2: A B
# x+3:   B
#
# A = x + x+1 + x+2 
# B = x+1 + x+2 + x+3
# B-A = x - x+3


def main():
  with open('data.txt','r') as f:
    data = f.read().splitlines()
    data = [int(val) for val in data]
    previous = data[0]
    count = 0
    for i in range(3,len(data)):
      if previous < data[i]:
        count += 1
      previous = data[i-2]
      
    print(count)
if __name__ == "__main__":
  main()
