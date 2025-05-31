Indian Culture & Tourism App
A Streamlit app that shows Indian cultural and tourism data using Snowflake.

Features:

View cultural data from Snowflake

Visualize tourist visits and funding

Run your own SQL queries

Setup:

Clone the repo:
git clone https://github.com/MaazPasha/indian-culture-tourism-app.git
cd indian-culture-tourism-app

Add your Snowflake credentials in .streamlit/secrets.toml

Install dependencies:
pip install streamlit snowflake-connector-python pandas matplotlib

Run the app:
streamlit run app.py
