import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Smart Data Visualizer",
    page_icon="📊",
    layout="wide"
)

# Header with logo
col1, col2 = st.columns([1,6])

with col1:
    st.image("assets/logo.png", width=70)

with col2:
    st.title("📊 Smart Data Visualizer")
    st.caption("Upload datasets and generate clean visual insights")

# Sidebar
st.sidebar.image("assets/logo.png", width=110)
st.sidebar.title("Smart Data Visualizer")
st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "📁 Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    data = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(data, use_container_width=True)

    # Detect column types
    numeric_columns = data.select_dtypes(include=['int64','float64']).columns.tolist()
    all_columns = data.columns.tolist()

    # Small subtle metric cards
    col1, col2, col3 = st.columns(3)

    card_style = """
    background-color:#1e1e1e;
    padding:12px;
    border-radius:8px;
    border:1px solid #333;
    text-align:center;
    """

    col1.markdown(
        f"""
        <div style="{card_style}">
        <p style="color:#aaa;margin-bottom:5px;">Rows</p>
        <h3 style="color:white;margin:0;">{data.shape[0]}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    col2.markdown(
        f"""
        <div style="{card_style}">
        <p style="color:#aaa;margin-bottom:5px;">Columns</p>
        <h3 style="color:white;margin:0;">{data.shape[1]}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    col3.markdown(
        f"""
        <div style="{card_style}">
        <p style="color:#aaa;margin-bottom:5px;">Missing Values</p>
        <h3 style="color:white;margin:0;">{data.isnull().sum().sum()}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("📊 Visualization Dashboard")

    chart_type = st.selectbox(
        "Choose Chart Type",
        ["Bar Chart", "Line Chart", "Pie Chart", "Histogram"]
    )

    # Histogram logic (numeric only)
    if chart_type == "Histogram":

        x_axis = st.selectbox("Select Numeric Column", numeric_columns)

        if st.button("Generate Chart 🚀"):

            fig = px.histogram(
                data,
                x=x_axis,
                nbins=20,
                template="plotly_dark",
                color_discrete_sequence=["#4CAF50"]
            )

            st.plotly_chart(fig, use_container_width=True)

    else:

        col1, col2 = st.columns(2)

        x_axis = col1.selectbox("Select X-axis", all_columns)
        y_axis = col2.selectbox("Select Y-axis (numeric)", numeric_columns)

        if st.button("Generate Chart 🚀"):

            if chart_type == "Bar Chart":

                fig = px.bar(
                    data,
                    x=x_axis,
                    y=y_axis,
                    color=y_axis,
                    template="plotly_dark"
                )

            elif chart_type == "Line Chart":

                fig = px.line(
                    data,
                    x=x_axis,
                    y=y_axis,
                    markers=True,
                    template="plotly_dark"
                )

            elif chart_type == "Pie Chart":

                fig = px.pie(
                    data,
                    names=x_axis,
                    values=y_axis,
                    template="plotly_dark"
                )

            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("⚙️ Technologies Used")
    st.write("🐍 Python  |  📊 Pandas  |  📈 Plotly  |  🚀 Streamlit")

else:

    st.info("👈 Upload a CSV dataset from the sidebar to begin visualization.")
