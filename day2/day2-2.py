
def main():
  with open('data.txt','r') as f:
    data = f.read().splitlines()
    
    for val in data:
      command, value = val.split()
      


    print(table)

if __name__ == "__main__":
  main()
