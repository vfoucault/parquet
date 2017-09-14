from parquet.parquet import Parquet
from pprint import pprint

def main():
    parquet = Parquet(width=3500, length=8000)
    parquet.fill_parquet()
    parquet.draw_parquet()
    parquet.show()

if __name__ == '__main__':
    main()