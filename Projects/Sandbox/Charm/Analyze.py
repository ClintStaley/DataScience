import sys
import pandas as pd

def main():
   frame = pd.read_csv(sys.argv[1], 
    usecols=["product_id", "order_id", "user_id"],
    dtype={'product_id': str, 'order_id': str, 'user_id': str})

   print(f"Number of products: {len(frame['product_id'].unique())}")
   print(f"Number of orders: {len(frame['order_id'].unique())}")
   print(f"Number of customers: {len(frame['user_id'].unique())}")

   # Remove repeated purchases of same product by same user
   byUsers = frame.drop_duplicates(['user_id', 'product_id'])

   # If noSingles, remove users who purchased at most one product
   if (len(sys.argv) > 3 and sys.argv[3] == "noSingles"):
       byUsers = byUsers.groupby('user_id').filter(
        lambda x: x['product_id'].size > 1)

   # Assemble Series of user-lists, indexed by product
   byUsers = pd.DataFrame({
      "userIds": byUsers.groupby('product_id')['user_id'].apply(lambda x: list(x))
   });

   byUsers.to_pickle(sys.argv[2])
   checkRead = pd.read_pickle(sys.argv[2])
   print("Read/write check", checkRead)

main()