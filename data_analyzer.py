import pandas as pd

def load_data(file):

    data = pd.read_csv(file)

    return data
def generate_insights(data):

    insights = {}

    numeric_columns = data.select_dtypes(include='number').columns

    for column in numeric_columns:

        insights[column] = {
            "mean": data[column].mean(),
            "max": data[column].max(),
            "min": data[column].min()
        }

    return insights