import pandas as pd
import matplotlib.pyplot as plt

def task_1(df):
    print(df.head())
    print(df.info())
    print(df.shape)

def task_2(df):
    print("Population", df["Population"].sum())
    print("Area", df["Area (sq. mi.)"].sum())
    print("GDP", df["GDP ($ per capita)"].mean())

def task_3(df):
    df_population_sorted = df.sort_values("Population", ascending=[False])
    print(df_population_sorted[["Country", "Population"]].head(5))

    df_literacy_phone_sorted = df.sort_values(["Literacy (%)", "Phones (per 1000)"])
    print(df_literacy_phone_sorted[["Country", "Literacy (%)", "Phones (per 1000)"]].head(2))

def task_4(df):
    df_region = df.groupby(["Region"])
    
    print("Površina po regiji")
    print(df_region["Area (sq. mi.)"].sum())

    df_region["Population"].sum().plot.bar()
    plt.xticks(
        rotation=60,
        horizontalalignment='right',
        fontweight='light',
        fontsize='small',
    )
    plt.xlabel('Region')
    plt.ylabel('Population')
    plt.title('Population by region')
    plt.show()

def task_5(df):
    df.to_csv('podaci.csv')


df = pd.read_csv("countries of the world.csv")



