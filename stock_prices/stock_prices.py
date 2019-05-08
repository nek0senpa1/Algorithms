#!/usr/bin/python

# import argparse

testy = [200, 1050, 10, 270, 1540, 3800, 650, 17, 27809, 5]


def find_max_profit(prices):
  holder = prices[0]
  low = prices[0]
  diff = 0

  widget = 1

  print(len(prices))
  
  for i in range(0,len(prices)-1):
    print('finding highest:', holder)
    
    if holder < prices[i+1]:
      holder = prices[i+1]
      widget = i+1

    for j in range(0, prices[i]):
      
      if low > prices[i]:
        low = prices[i]

  diff = holder - low

  return diff



# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

print('andsworz', find_max_profit(testy))