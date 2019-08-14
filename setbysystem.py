import pandas as pd

file = r'C:\Users\ajezewsk\Downloads\cudo1.xlsx'
file_rb = pd.read_excel(file, sheet_name='Parameter List')
df = pd.DataFrame(file_rb)


def replacement():
    for num in range(len([column for column in df.columns])):
        df.rename(columns={[column for column in df.columns][num]: [name for name in df.loc[1]][num]}, inplace=True)
    return df
replacement()


parse_sbs = (df.loc[:, ["Abbreviated Name", "Required on Creation"]].drop(index=0)).loc[
    df["Required on Creation"] == "Value set by the system"]

parse_ifs =(df.loc[:, ["Abbreviated Name", "Interfaces"]].drop(index=0))
direct_ifs = parse_ifs[~parse_ifs["Interfaces"].str.contains("<")]

def set_by_system(dataframe):
    return dataframe["Abbreviated Name"].values
print(set_by_system(parse_sbs))


def interfaces(dataframe):
    return dataframe["Abbreviated Name"].values
print(interfaces(direct_ifs))


def main():
    pass

if __name__ =='__main__':
    main()