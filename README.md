# Crypto Wallet Behavior Analysis

A data science project that analyzes Ethereum wallet transaction behavior using on-chain data. This project uses clustering and feature engineering to uncover patterns in user behavior such as frequent traders, holders, and gas spenders.

## 🔍 Project Goals
- Collect and preprocess Ethereum wallet transaction data
- Engineer features such as transaction frequency, volume, token diversity
- Segment wallets using unsupervised learning (clustering)
- Visualize patterns across different wallet types

## 🧰 Tech Stack
- **Python**, **Jupyter Notebooks**
- **pandas**, **scikit-learn**, **matplotlib**, **seaborn**
- **Etherscan API**, **Plotly**, **Streamlit (optional)**

## 📦 Project Structure
```text 
crypto-wallet-behavior-analysis/
├── 📁 data/ # Raw and processed transaction CSV files
├── 📁 notebooks/ # Jupyter notebooks for exploration and analysis
├── 📁 src/ # Python modules for data processing, clustering, utils
├── app.py # Streamlit dashboard app
├── wallet_behavior_clusters.csv # Output CSV with clustered wallet behaviors
├── requirements.txt # Python package dependencies
├── README.md # Project documentation
└── .gitignore # Files to exclude from Git tracking
```

## 🚀 Setup and Run the Streamlit Dashboard

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KayMan2025/crypto-wallet-behavior-analysis.git
   cd crypto-wallet-behavior-analysis
