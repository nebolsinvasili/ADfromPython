import pandas as pd

from .color import color


def print_df_describe(df: pd.DataFrame, 
                      name: str,
                      show: bool = False):
    # Get an overview of the data
    if show:
        print(f'{color.BLUE}{name}{color.END} (head of the data is):')
        print(df.head())
        print()

        # Get an describe of the data
        print(f'{color.BLUE}{name}{color.END} (describe of the data is):')
        print(df.describe())
        print()

        #　Checking the shape of the dataframes
        print(f"Shape of {name} : {color.BLUE}{df.shape}{color.END}")
        print('-' * 80)

        # Get an isnull of the data
        print(f'{color.BLUE}{name}{color.END} (is null of the data is):')
        print(df.isnull().sum())
        print()

        # Get an isna of the data
        print(f'{color.BLUE}{name}{color.END} (is nan of the data is):')
        print(df.isna().sum())
        print()

        # Get an isna of the data
        print(f'{color.BLUE}{name}{color.END} (duplicated of the data is):')
        print(df.duplicated().sum())

        # Get info from data
        print(f'{color.BLUE}{name}{color.END} (info of the data is):')
        print(df.info())
        

if __name__ == '__main__':
   pass