from collections import defaultdict
def main():
  with open('data.txt','r') as f:
    data = f.read().splitlines()
    vents = []
    points = defaultdict(int)
    for line in data:
      vent = line.split()
      x1, y1 = vent[0].split(',')
      x2, y2 = vent[2].split(',')
      x1,y1,x2,y2 = int(x1), int(y1),int(x2),int(y2)
      if x1 == x2 or y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
          for y in range(min(y1,y2), max(y1,y2)+1):
            points[x,y] += 1  
      else:
        dir_x = 1 if x2 > x1 else -1
        dir_y = 1 if y2 > y1 else -1
        points[x1,y1] += 1
        while x1 != x2:
          x1 += dir_x
          y1 += dir_y
          points[x1,y1] += 1
    print(sum(1 for point in points.values() if point > 1))

if __name__ == "__main__":
  main()
