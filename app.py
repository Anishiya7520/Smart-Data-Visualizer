import streamlit as st
from data_analyzer import load_data, generate_insights
from chart_generator import create_bar_chart, create_line_chart

st.title("Smart Data Visualization Tool")

uploaded_file = st.file_uploader("Upload CSV File", type="csv")

if uploaded_file:

    data = load_data(uploaded_file)

    st.subheader("Dataset Preview")

    st.write(data.head())

    insights = generate_insights(data)

    st.subheader("Data Insights")

    for column, stats in insights.items():

        st.write(f"Column: {column}")

        st.write(f"Average: {stats['mean']}")

        st.write(f"Max: {stats['max']}")

        st.write(f"Min: {stats['min']}")

    numeric_columns = data.select_dtypes(include='number').columns

    selected_column = st.selectbox("Select column for visualization", numeric_columns)

    st.subheader("Bar Chart")

    bar_chart = create_bar_chart(data, selected_column)

    st.plotly_chart(bar_chart)

    st.subheader("Line Chart")

    line_chart = create_line_chart(data, selected_column)

    st.plotly_chart(line_chart)