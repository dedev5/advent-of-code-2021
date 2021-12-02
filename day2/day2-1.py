
def main():
  with open('data.txt','r') as f:
    data = f.read().splitlines()
    
    table = {"forward":0,"down":0,"up":0}
    for val in data:
      direction, value = val.split()
      table[direction] += int(value)

    print(table)
    print(table["forward"]*(table["down"]-table["up"]))

if __name__ == "__main__":
  main()
