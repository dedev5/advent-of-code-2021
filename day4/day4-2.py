
def main():
  with open('data.txt','r') as f:
    data = f.read().splitlines()
    numbers = data[0].split(',')
    bingo_sheets = []
    for row in data[1:]:
      if row == '':
        bingo_sheets.append([])
      else:
        bingo_sheets[-1] += row.split()
    while len(bingo_sheets) > 0:
      call = numbers.pop(0)
      rem = []
      for i, sheet in enumerate(bingo_sheets):
        if call in sheet:
          mark = bingo_sheets[i].index(call)
          bingo_sheets[i][mark] = "x"
          if (all(val == "x" 
            for val in bingo_sheets[i][mark - mark%5: mark - mark%5 + 5])
            or all(val == "x" for val in bingo_sheets[i][mark%5::5])):
              total = sum([int(val) for val in bingo_sheets[i] if not val == "x"])
              print(total * int(call))
              rem.append(i)
      for sheet_id in rem[::-1]:
        bingo_sheets.pop(sheet_id)

      
def print_bingo(boards):
  for board in boards:
    for i in range(0,len(board)):
      print(f"{board[i]:<4}",end='')
      if i % 5 == 4:
        print()
    print()
if __name__ == "__main__":
  main()
