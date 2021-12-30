import pandas as pd

def main():
    df = pd.read_csv("works.csv").dropna()

    c_not_same = 0
    for (i, j) in zip(df['jobTitle'], df['qualification']):
        if i.lower().replace('-', ' ') != j.lower().replace('-', ' '):
             c_not_same += 1

    print(c_not_same)
    print(top_five(df, "jobTitle", "qualification", "менеджер"))
    print(top_five(df, "qualification", "jobTitle", "инженер"))

def top_five(data, to_search, to_return, searched_str):
    return data[data[to_search].str.lower().str.contains(searched_str)][to_return].str.lower().value_counts().head(5)

if __name__ == "__main__":
    main()