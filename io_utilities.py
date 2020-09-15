import pandas as pd

def readvanilla():
    # Reads Dataset and stores results in dictionary
    # Only for python3.8
    data = {"sepal_length":[],"sepal_width":[],"petal_length":[],"petal_width":[],"class":[]}
    filepath = "data/iris.data"
    with open(filepath,"r") as f:
        while (line:=f.readline().strip("\n").split(",")) and len(line) == len(data.keys()):
            for idx,key in enumerate(data.keys()):
                try:
                    data[key].append(float(line[idx]))
                except ValueError as e:
                    data[key].append(line[idx])
    return data


def read_pandas(filepath,**kwargs):
    """
    Reads CSV In pandas
    return Pandas DataFrame
    """
    df = pd.read_csv(filepath,**kwargs)
    return df

if __name__ == "__main__":
    filepath = "data/iris.data"
    df = read_pandas(filepath=filepath,names=["sepal_length","sepal_width","petal_length","petal_width","class"])
    print(df.head())
