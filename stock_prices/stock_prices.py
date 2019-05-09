#!/usr/bin/python

# import argparse

testy = [100, 90, 80, 50, 20, 10,400,999,350,4,6,7]


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

      for j in range(0, i):
        print('find lowest:', low)
        if low > prices[j]:
          low = prices[j]

          diff = holder - low

  return diff

print('andsworz', find_max_profit(testy))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

