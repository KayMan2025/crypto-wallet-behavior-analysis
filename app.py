import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ethereum Wallet Cluster Explorer", layout="wide")
st.title("Ethereum Wallet Cluster Explorer")


df = pd.read_csv("wallet_behavior_clusters.csv")

cluster_filter = st.selectbox("Select Cluster", sorted(df["cluster"].unique()))
subset = df[df["cluster"] == cluster_filter]

st.write("### Cluster Summary", subset.describe())

st.write("### Behavior Label Counts")
st.bar_chart(subset["behavior_label"].value_counts())

st.write("### ETH Sent vs Received")
fig, ax = plt.subplots()
sns.scatterplot(data=subset, x="total_eth_received", y="total_eth_sent", hue="behavior_label", ax=ax)
st.pyplot(fig)
