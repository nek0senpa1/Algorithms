#!/usr/bin/python

import argparse

def find_max_profit(prices):
  holder = 0
  low = 0
  diff = 0

  for i in prices:
    if prices[i] > prices[i]+1
    holder = prices[i]

    if prices[i] < prices[i]+1
    low = prices[i]

  diff = holder - low

  return diff



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))