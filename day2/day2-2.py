def main():
  with open('data.txt','r') as f:
    data = f.read().splitlines()
    
    aim = 0
    depth = 0
    position = 0
    for val in data:
      command, value = val.split()
      value = int(value)
      match command:
        case "forward":
          depth += aim*value
          position += value
        case "up":
          aim -= value
        case "down":
          aim += value
      


    print(position*depth)

if __name__ == "__main__":
  main()
