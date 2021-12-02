def main():
  with open('data.txt','r') as f:
    data = f.read().splitlines()
    data = [int(val) for val in data]

    count = 0
    previous = data[0]
    for value in data:
      if previous < value:
        count += 1
      previous = value

    print(count)
if __name__ == "__main__":
  main()
