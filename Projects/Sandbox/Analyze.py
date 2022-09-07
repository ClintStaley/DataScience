import sys
import pandas as pd

def main():
   print(f"Reading {sys.argv[1]}");
   frame = pd.read_csv(sys.argv[1], usecols=["product_id", "order_id", "user_id"])

   print(f"Number of products: {len(frame['product_id'].unique())}")
   print(f"Number of orders: {len(frame['order_id'].unique())}")
   print(f"Number of customers: {len(frame['user_id'].unique())}")

   # print("Original", frame)
   # Remove repeated purchases of same product by same user
   frame = frame.drop_duplicates(['user_id', 'product_id'])
   # print("Without duplicate user/product", frame)

   # Remove users who purchased at most one product
   byUsers = frame.groupby('user_id').filter(lambda x: x['product_id'].size > 1)
   # print("Without users with just one product", byUsers)

   # Assemble DF of user-lists, indexed by product
   byUsers = byUsers.groupby('product_id')['user_id'].apply(lambda x: list(x))
   # print("Product -> user list", byUsers)

   byUsers.to_pickle(sys.argv[2])
   # print("Done Writing")
   checkRead = pd.read_pickle(sys.argv[2])
   print("Read/write check", checkRead)

main()
