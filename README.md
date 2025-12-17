
# pyaccounting 📊

A lightweight Python module for automated financial and accounting ratio analysis.

## 🚀 Overview
`pyaccounting` is designed to simplify financial statement analysis by providing standardized, easy-to-use functions for calculating core business ratios. It is ideal for students, accountants, and developers building financial tools.

## 🚀 Quick Start
After installing with `pip install pyaccounting`, you can use the module like this:

```python
import pyaccounting as pya

# Get user input for analysis
a = int(input("Current assets amount: "))
b = int(input("Current liability amount: "))

# Calculate the ratio using pyaccounting
c = pya.currentr(a, b)

print(f"Your Current Ratio is: {c}")

## ✨ Features
- **Liquidity Analysis:** Quickly calculate Current and Quick ratios.
- **Solvency Metrics:** Automated Debt-to-Equity calculations.
- **Clear Documentation:** Every ratio includes the standard accounting formula used.

## 📥 Installation
You can install `pyaccounting` directly from PyPI:
```bash
pip install pyaccounting
