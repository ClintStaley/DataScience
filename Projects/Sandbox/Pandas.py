import pandas as pd;

def main():
   frame = pd.read_csv('../Datasets/kz.csv')
   # orders = frame.groupby('order_id')
   # print(frame)
   # print(orders.groups)
   print(len(frame['product_id'].unique()))
   print(len(frame['order_id'].unique()))
  

main()