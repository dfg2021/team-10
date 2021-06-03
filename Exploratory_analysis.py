import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats


def describe_df(df):
    print(df.head(10))
    print(df.tail(10))
    print(df.dtypes)
    print(df.describe())
    print(df.describe(include="all"))
    print(df.info)


def group_by_usage(df):
    df_all = df[(df['Value'] > 75)]
    print(pd.crosstab(df_all["Sex"], df_all["Type of skill"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_all["GeoAreaName"], df_all["Sex"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_all["Target"], df_all["Sex"]))

    df_test = df[["GeoAreaName", "Type of skill", "Value"]]
    df_grp = df_test.groupby(["GeoAreaName", "Type of skill"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "GeoAreaName", columns = "Type of skill")
    print(df_pivot)


# Completion rate, by sex, location, wealth quantile and education level (%)
def exploratory_df41(df):
    df_41 = df[(df['Target'] == 4.1)]
    print(pd.crosstab(df_41["Sex"], df_41["Quantile"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_41["Location"], df_41["Quantile"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_41["Education level"], df_41["Quantile"]).apply(lambda r: r / r.sum(), axis=1))

    df_test = df_41[["Sex", "Location", "Quantile", "Education level", "Value"]]
    df_grp = df_test.groupby(["Sex", "Location"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "Location", columns = "Sex")
    print(df_pivot)


# Participation rate in organized learning (one year before the official primary entry age), by sex (%)
def exploratory_df42(df):
    df_42 = df[(df['Target'] == 4.2)]
    print(pd.crosstab(df_42["Sex"], df_42["GeoAreaName"]).apply(lambda r: r/r.sum(), axis=1))

    df_test = df_42[["Sex", "GeoAreaName", "Value"]]
    df_grp = df_test.groupby(["Sex", "GeoAreaName"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "GeoAreaName", columns = "Sex")
    print(df_pivot)


# Participation rate in formal and non-formal education and training, by sex (%)
def exploratory_df43(df):
    df_43 = df[(df['Target'] == 4.3)]
    print(pd.crosstab(df_43["Sex"], df_43["GeoAreaName"]).apply(lambda r: r/r.sum(), axis=1))

    df_test = df_43[["Sex", "GeoAreaName", "Value"]]
    df_grp = df_test.groupby(["Sex", "GeoAreaName"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "GeoAreaName", columns = "Sex")
    print(df_pivot)


# Proportion of youth and adults with information and communications technology (ICT) skills,
# by sex and type of skill (%)
def exploratory_df44(df):
    df_44 = df[(df['Target'] == 4.4)]
    print(pd.crosstab(df_44["Sex"], df_44["Type of skill"]).apply(lambda r: r/r.sum(), axis=1))

    df_test = df_44[["Sex", "Type of skill", "Value"]]
    df_grp = df_test.groupby(["Sex", "Type of skill"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "Type of skill", columns = "Sex")
    print(df_pivot)


# Adjusted wealth parity index for completion rate, by sex, location, wealth quantile and education level
def exploratory_df45(df):
    df_45 = df[(df['Target'] == 4.5)]
    print(pd.crosstab(df_45["Sex"], df_45["Location"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_45["Quantile"], df_45["Education level"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_45["Sex"], df_45["Education level"]).apply(lambda r: r/r.sum(), axis=1))

    df_test = df_45[["Sex", "Location", "Quantile", "Education level", "Value"]]
    df_grp = df_test.groupby(["Sex", "Location", "Quantile", "Education level"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "Education level", columns = ["Sex", "Location", "Quantile"])
    print(df_pivot)


# Proportion of population achieving at least a fixed level of proficiency in functional skills,
# by sex, age and type of skill (%)
def exploratory_df46(df):
    df_46 = df[(df['Target'] == '4.6')]
    print(pd.crosstab(df_46["Sex"], df_46["Type of skill"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_46["Age"], df_46["Type of skill"]).apply(lambda r: r/r.sum(), axis=1))

    df_test = df_46[["Sex", "Age", "Type of skill", "Value"]]
    df_grp = df_test.groupby(["Sex", "Age", "Type of skill"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "Type of skill", columns = ["Sex", "Age"])
    print(df_pivot)


# Schools with the facilities, by education level (%) (includes different Series Codes
def exploratory_df4a(df):
    df_4a = df[(df['Target'] == '4.a')]
    print(pd.crosstab(df_4a["Education level"], df_4a["SeriesCode"]).apply(lambda r: r/r.sum(), axis=1))

    df_test = df_4a[["Education level", "SeriesCode", "Value"]]
    df_grp = df_test.groupby(["Education level", "SeriesCode"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "Education level", columns = "SeriesCode")
    print(df_pivot)


# Total official flows for scholarships, by recipient countries (millions of constant 2018 United States dollars)
def exploratory_df4b(df):
    df_4b = df[(df['Target'] == '4.b')]

    df_test = df_4b[["GeoAreaName", "Value"]]
    df_grp = df_test.groupby(["GeoAreaName"], as_index = False).mean()

    df_pivot = df_grp.pivot(columns = "GeoAreaName")
    print(df_pivot)


# Proportion of teachers who have received at least the minimum organized
# teacher training (e.g. pedagogical training) pre-service or in-service required for
# teaching at the relevant level in a given country, by sex and education level (%)
def exploratory_df4c(df):
    df_4c = df[(df['Target'] == '4.c')]
    print(pd.crosstab(df_4c["Sex"], df_4c["GeoAreaName"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_4c["Sex"], df_4c["Education level"]).apply(lambda r: r/r.sum(), axis=1))
    print(pd.crosstab(df_4c["GeoAreaName"], df_4c["Education level"]).apply(lambda r: r/r.sum(), axis=1))

    df_test = df_4c[["Sex", "GeoAreaName", "Education level", "Value"]]
    df_grp = df_test.groupby(["Sex", "GeoAreaName", "Education level"], as_index = False).mean()

    df_pivot = df_grp.pivot(index = "Education level", columns = ["Sex", "GeoAreaName"])
    print(df_pivot)


# Replace the Upper and Lower Bound with the maximum and minimum of
# the values grouped by indication code, country and year
def replace_bound_features(df):
    max_df = df[["Target", "Indicator", "GeoAreaName", "Value", "Time_Detail"]].groupby(["Target", "Indicator", "Time_Detail", "GeoAreaName"]).max()
    max_df = max_df.reset_index()
    max_df = max_df.rename(columns={"Value": "newValue"})
    min_df = df[["Target", "Indicator", "GeoAreaName", "Time_Detail", "Value"]].groupby(["Target", "Indicator", "Time_Detail", "GeoAreaName"]).min()
    min_df = min_df.reset_index()
    min_df = min_df.rename(columns={"Value": "newValue"})

    df["hashIndex"] = df.Indicator.astype(str) + df.GeoAreaName.astype(str) + df.Time_Detail.astype(str)
    min_df["hashIndex"] = min_df.Indicator.astype(str) + min_df.GeoAreaName.astype(str) +  min_df.Time_Detail.astype(str)
    max_df["hashIndex"] = max_df.Indicator.astype(str) + max_df.GeoAreaName.astype(str) + max_df.Time_Detail.astype(str)

    df = df.set_index("hashIndex")
    min_df = min_df.set_index("hashIndex")
    max_df = max_df.set_index("hashIndex")

    df.loc[min_df.index, "LowerBound"] = min_df.newValue
    df.loc[max_df.index, "UpperBound"] = max_df.newValue
    return df.reset_index(drop=True)
