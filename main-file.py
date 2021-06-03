from Exploratory_analysis import *

def main():
    print("Hello!")
    path = "config_files/Goal4.csv"
    df = pd.read_csv(path)
    describe_df(df)
    group_by_usage(df)
    print("\n\n Exploratory analysis of Target 4.1")
    exploratory_df41(df)
    print("\n\n Exploratory analysis of Target 4.2")
    exploratory_df42(df)
    print("\n\n Exploratory analysis of Target 4.3")
    exploratory_df43(df)
    print("\n\n Exploratory analysis of Target 4.4")
    exploratory_df44(df)
    print("\n\n Exploratory analysis of Target 4.5")
    exploratory_df45(df)
    print("\n\n Exploratory analysis of Target 4.6")
    exploratory_df46(df)
    print("\n\n Exploratory analysis of Target 4.a")
    exploratory_df4a(df)
    print("\n\n Exploratory analysis of Target 4.b")
    exploratory_df4b(df)
    print("\n\n Exploratory analysis of Target 4.c")
    exploratory_df4c(df)

main()