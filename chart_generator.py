import plotly.express as px

def create_bar_chart(data, column):

    fig = px.bar(data, x=data.index, y=column)

    return fig


def create_line_chart(data, column):

    fig = px.line(data, x=data.index, y=column)

    return fig