import streamlit as st

st.title("🚀 Getting Started")

st.markdown("Complete these steps before beginning the lab exercises.")

st.markdown("---")

st.header("Step 1: Log in to Snowflake")

st.info("""
Open your Snowflake URL and log in.
""")

st.markdown("---")

st.header("Step 2: Find your assigned number")

st.markdown("""
Each participant has a pre-assigned number and workspace. Find your name below and note your **number** — 
you'll use it throughout the entire lab.
""")

st.dataframe(
    {
        "#": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
              "21", "22", "23"],
        "Name": [
            "Azer, David",
            "Das, Asesh",
            "Deng, Yuhan",
            "Guo, Charlie",
            "He, Shuntian",
            "Kichler, Aaron",
            "Lakshminarayanan, Prithvi",
            "Liu, Shally S",
            "Malik, Jamshed",
            "Rehal, Manisha",
            "Chellappan, Dinesh",
            "Shaikh, Anaan",
            "Kundu, Sujoy",
            "Villar, Cesar",
            "Lingaratnam, Anojan",
            "Karbasi, Payam",
            "Terlecky, Stephen",
            "Yadav, Sachinkumar",
            "Chen, Yan",
            "Walimbe, Sharwari",
            "Braga, Antony",
            "Mohanan, Sukanya",
            "Wong, Sam",
        ],
        "Role": [
            "HOL_USER_01", "HOL_USER_02", "HOL_USER_03", "HOL_USER_04",
            "HOL_USER_05", "HOL_USER_06", "HOL_USER_07", "HOL_USER_08",
            "HOL_USER_09", "HOL_USER_10", "HOL_USER_11", "HOL_USER_12",
            "HOL_USER_13", "HOL_USER_14", "HOL_USER_15", "HOL_USER_16",
            "HOL_USER_17", "HOL_USER_18", "HOL_USER_19", "HOL_USER_20",
            "HOL_USER_21", "HOL_USER_22", "HOL_USER_23",
        ],
        "Schema": [
            "RETAIL_BANKING_01", "RETAIL_BANKING_02", "RETAIL_BANKING_03",
            "RETAIL_BANKING_04", "RETAIL_BANKING_05", "RETAIL_BANKING_06",
            "RETAIL_BANKING_07", "RETAIL_BANKING_08", "RETAIL_BANKING_09",
            "RETAIL_BANKING_10", "RETAIL_BANKING_11", "RETAIL_BANKING_12",
            "RETAIL_BANKING_13", "RETAIL_BANKING_14", "RETAIL_BANKING_15",
            "RETAIL_BANKING_16", "RETAIL_BANKING_17", "RETAIL_BANKING_18",
            "RETAIL_BANKING_19", "RETAIL_BANKING_20", "RETAIL_BANKING_21",
            "RETAIL_BANKING_22", "RETAIL_BANKING_23",
        ],
    },
    use_container_width=True,
    hide_index=True,
)

st.warning("Use **your assigned number** in every `USE ROLE` and `USE SCHEMA` command throughout the lab.")

st.markdown("---")

st.header("Step 3: Keep this guide open")

st.markdown("""
Keep this browser tab open throughout the lab:

👉 **https://zero-to-sf-hol-rbc-july28.streamlit.app**

Use the sidebar to navigate between sections. Each section has:
- A **concept intro** explaining what you'll learn
- **Numbered exercises** with SQL to copy and run
- A **CoCo Sneak Peek** showing how Cortex Code could do it for you
""")

st.markdown("---")

st.success("""
## ✅ You're ready!

Head to **Section 1: Snowflake UI Tour** to begin the lab.
""")
