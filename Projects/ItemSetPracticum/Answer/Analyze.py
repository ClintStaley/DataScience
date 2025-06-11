import sys
import pandas as pd

def main():
    frame = pd.read_csv(sys.argv[1], 
    usecols=["product_id", "order_id", "user_id"],
    dtype={'product_id': str, 'order_id': str, 'user_id': str})

    print(f"Number of products: {len(frame['product_id'].unique())}")
    print(f"Number of orders: {len(frame['order_id'].unique())}")
    print(f"Number of customers: {len(frame['user_id'].unique())}")

    # Remove repeated purchases of same product in same order
    noDups = frame.drop_duplicates(['order_id', 'product_id'])

    # If noSingles, remove orders with only one product
    if (len(sys.argv) > 3 and sys.argv[3] == "noSingles"):
        noDups = noDups.groupby('order_id').filter(
        lambda x: x['product_id'].size > 1)
    
    # Assemble Series of order-lists, indexed by product
    byOrders = pd.DataFrame({
        "orderIds": noDups.groupby('product_id')['order_id'].apply(lambda x: list(x))})
    
    byOrders.to_pickle(sys.argv[2])
    checkRead = pd.read_pickle(sys.argv[2])
    print("Read/write check", checkRead)

main()