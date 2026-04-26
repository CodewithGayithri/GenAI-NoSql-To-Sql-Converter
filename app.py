 # Import required libraries
import streamlit as st          # Streamlit for UI
import json                     # For JSON parsing and validation
from groq import Groq           # Groq client to access LLaMA model


# ------------------ PAGE CONFIG ------------------
# Configure Streamlit page title and layout
st.set_page_config(
    page_title="NoSQL / MongoDB → SQL Converter",
    layout="centered"
)


# ------------------ TITLE ------------------
# Main title displayed on the web UI
st.title("🧠 NoSQL / MongoDB→ SQL Converter")

# Short description under the title
st.caption("Convert NoSQL & MongoDB JSON into SQL using Generative AI")


# ------------------ GROQ API ------------------
# Groq API key (used to access LLaMA 3.1 model)
GROQ_API_KEY = "YOUR_API_KEY"

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


# ------------------ CONVERSION MODE ------------------
# Radio button to select conversion type
conversion_mode = st.radio(
    "",
    ["NoSQL → SQL", "MongoDB → SQL"],
    horizontal=True
)


# ------------------ DEFAULT INPUT ------------------
# Default example JSON for NoSQL → SQL
default_nosql = '''[
  {"id": 1, "name": "Alice", "salary": 50000},
  {"id": 2, "name": "Bob", "salary": 60000}
]'''

# Default example JSON for MongoDB → SQL
default_mongo = '''{
  "_id": "U001",
  "name": "Alice",
  "salary": 50000,
  "address": {
    "city": "Bengaluru",
    "pincode": 560001
  },
  "skills": ["Python", "SQL"]
}'''

# Initialize session state for text area input
if "nosql_input" not in st.session_state:
    st.session_state.nosql_input = default_nosql

# Automatically switch example JSON when MongoDB mode is selected
if conversion_mode == "MongoDB → SQL":
    st.session_state.nosql_input = default_mongo


# ------------------ INPUT SECTION ------------------
st.subheader("📥 Enter JSON")

# File uploader to upload JSON file
uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

# If file is uploaded, read and load it into text area
if uploaded_file:
    st.session_state.nosql_input = uploaded_file.read().decode("utf-8")

# Text area to paste or edit JSON input
nosql_json = st.text_area(
    "Paste JSON here",
    height=320,
    key="nosql_input"
)


# ------------------ SQL DIALECT SELECTION ------------------
# Dropdown to choose SQL database type
sql_dialect = st.selectbox(
    "Select SQL Database",
    ["MySQL", "PostgreSQL", "SQLite"]
)


# ------------------ ACTION BUTTON ------------------
# Button to start conversion
convert_clicked = st.button("▶ Convert")


# ------------------ CONVERSION LOGIC ------------------
if convert_clicked:
    try:
        # Validate JSON input
        data = json.loads(nosql_json)

        # Prompt for NoSQL → SQL conversion
        if conversion_mode == "NoSQL → SQL":
            prompt = f"""
Convert the following NoSQL JSON into SQL for {sql_dialect}.

Rules:
- Assume flat or semi-structured JSON
- Infer table structure
- Generate CREATE TABLE
- Generate INSERT statements
- Output ONLY SQL
- No explanation

JSON:
{json.dumps(data, indent=2)}
"""

        # Prompt for MongoDB → SQL conversion
        else:
            prompt = f"""
You are a database expert.

Convert the following MongoDB JSON document into SQL for {sql_dialect}.

STRICT RULES:
- Treat _id as PRIMARY KEY
- Normalize nested objects into separate tables
- Normalize arrays into child tables
- Add FOREIGN KEYS
- Generate CREATE TABLE statements
- Generate INSERT statements
- Output ONLY SQL
- No explanation

MongoDB JSON:
{json.dumps(data, indent=2)}
"""

        # Call Groq API with LLaMA 3.1 model
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        # Extract generated SQL from response
        sql_output = response.choices[0].message.content.strip()

        # Display success message
        st.success(f"✅ {sql_dialect} Generated Successfully")

        # Display generated SQL with syntax highlighting
        st.subheader("🧾 Generated SQL")
        st.code(sql_output, language="sql")

        # Allow user to download SQL file
        st.download_button(
            label="📥 Download SQL",
            data=sql_output,
            file_name="converted.sql",
            mime="text/sql"
        )

    # Handle invalid JSON errors
    except json.JSONDecodeError:
        st.error("❌ Invalid JSON format")

    # Handle any other runtime errors
    except Exception as e:
        st.error(f"❌ Error: {e}")


# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Groq + LLaMA 3.1 | NoSQL & MongoDB → SQL Converter")
