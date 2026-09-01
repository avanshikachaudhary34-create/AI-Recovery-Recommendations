import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RecoverAI",
    page_icon="💳",
    layout="wide"
)

st.title("💳 RecoverAI")
st.subheader("AI-Powered Revenue Recovery Agent")

st.write(
    "RecoverAI identifies at-risk payments and recommends "
    "the most suitable recovery action."
)

st.divider()

# Sample transaction data
data = {
    "Transaction ID": ["TXN001", "TXN002", "TXN003", "TXN004", "TXN005"],
    "Customer": ["Aarav", "Priya", "Rahul", "Sneha", "Kabir"],
    "Amount (₹)": [2499, 999, 4999, 1499, 2999],
    "Status": ["Failed", "Failed", "Pending", "Failed", "Pending"],
    "Failure Reason": [
        "Card Declined",
        "Insufficient Funds",
        "Bank Timeout",
        "Card Declined",
        "Network Error"
    ]
}

df = pd.DataFrame(data)

st.header("📊 At-Risk Transactions")

st.dataframe(
    df,
    width="stretch",
    hide_index=True
)

st.divider()

total_at_risk = df["Amount (₹)"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total At-Risk Revenue", f"₹{total_at_risk:,}")

with col2:
    st.metric("Transactions Requiring Action", len(df))
st.divider()

st.header("🤖 AI Recovery Recommendations")

def get_recommendation(reason):
    if reason == "Card Declined":
        return "Retry payment with another card"
    elif reason == "Insufficient Funds":
        return "Send payment reminder"
    elif reason == "Bank Timeout":
        return "Retry payment after some time"
    elif reason == "Network Error":
        return "Retry payment"
    else:
        return "Contact customer"

for _, row in df.iterrows():
    recommendation = get_recommendation(row["Failure Reason"])

    st.write(
        f"**{row['Transaction ID']} – {row['Customer']}** "
        f"→ {recommendation}"
    )