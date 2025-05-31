import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import snowflake.connector

# Snowflake connection (reads from secrets.toml)
def create_snowflake_connection():
    conn = snowflake.connector.connect(
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"]
    )
    return conn

# Query function
def run_query(query):
    conn = create_snowflake_connection()
    
    try:
        cur = conn.cursor()
        cur.execute(query)
        df = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])
        return df
    finally:
        conn.close()

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Select a page", ["Home", "Explore Data", "Visualize", "Snowflake Query", "About"])

if page == "Home":
    st.title("🎨 Art, Culture, and Tourism of India")
    st.markdown("""
    Welcome! This app explores the **rich cultural heritage of India**, showcasing traditional art forms, regional festivals, and their impact on tourism.
    
    🌏 **Objectives:**
    - Promote responsible tourism through data.
    - Highlight government support and regional diversity.
    - Explore seasonal tourist trends and hidden gems.
    
    Dive in and discover India's vibrant art and cultural tapestry! 🌺
    """)

elif page == "Explore Data":
    st.title("📊 Explore Cultural Data")
    st.write("Fetching data from Snowflake...")

    query = "SELECT * FROM cultural_db;"  # Replace with your actual table name
    df = run_query(query)
    st.dataframe(df)

elif page == "Visualize":
    st.title("📈 Visualize Tourism & Culture")

    query = "SELECT * FROM cultural_db;"  # Replace with your actual table name
    df = run_query(query)

    st.subheader("Select Metric to Visualize")
    metric = st.selectbox("Choose a metric", ["TOURIST_VISITS_SUMMER", "TOURIST_VISITS_WINTER", "GOVERNMENT_FUNDING_CRORES"])

    fig, ax = plt.subplots()
    ax.bar(df["STATE"], df[metric], color="teal")
    ax.set_ylabel(metric)
    ax.set_title(f"{metric} by State")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)


elif page == "Snowflake Query":
    st.title("📝 Run Custom SQL Query")
    query = st.text_area("Enter your SQL query here", "SELECT * FROM cultural_db;")
    if st.button("Run Query"):
        try:
            df = run_query(query)
            st.write("Query Results")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Query failed: {e}")

elif page == "About":
    st.title("📚 About This App")
    st.markdown("""
    **Art, Culture & Tourism: Bridging Technology and Tradition**  
    - Built with **Python & Streamlit**.
    - Data sourced from **Snowflake** (uploaded CSV of cultural data).
    - Showcases traditional art forms, festivals, seasonal tourist trends, and government funding.

    ✨ Developed by Maaz Pasha ✨  
    [GitHub Repository](https://github.com/MaazPasha) | [Contact](mailto:maazpasham@gmail.com)
    """)
