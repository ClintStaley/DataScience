import pandas as pd;

def main():
   frame = pd.read_csv('kz.csv', nrows = 10)
   orders = frame.groupby('order_id')
   print(frame)
   print(orders.groups)


main()