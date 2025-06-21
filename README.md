# 📊 EDGAR Financials Utils

A lightweight Python utility to fetch and parse financial data for a specific company from the SEC EDGAR API. Easily access key financials like income statements, balance sheets, and cash flows for recent years.

---

## 🚀 Features

- Retrieve company filings using CIK 
- Parse financial statements (10-K)
- Extract key financial data for multiple years
- Lightweight and easy to integrate into existing projects

---

## 🧩 Installation

### Install Python 
https://www.python.org/downloads/

### Clone the repository:

```bash
git clone https://github.com/cern7/edgar-API-utils.git
cd edgar-API-utils/
```
### Install dependencies:

```bash
pip install aiohttp
pip install pandas
```
## 🛠️ Usage

### 1. Find the Company CIK (Central Index Key)
First, obtain the company's **CIK**. You can find this via EDGAR or other public sources (e.g., searching the company on [https://www.sec.gov/edgar/searchedgar/companysearch.html](https://www.sec.gov/edgar/searchedgar/companysearch.html)).

---

### 2. Fetch Company Facts from the SEC API

Use the following endpoint, replacing `{{CIK}}` with the actual company CIK:
https://data.sec.gov/api/xbrl/companyfacts/CIK{{CIK}}.json



In the API response, navigate to the `facts.us-gaap` object to access structured financial data.

⚠️ **Note:** Different companies may use different attribute names for the same financial term. You may need to inspect their most recent **10-K filing** manually to identify the correct `us-gaap` keys based on the reported values.

---

### 3. Map and Extract Key Financial Metrics

After identifying the correct fields, the script extracts the following financial data (typically from the last ~10 years of 10-K reports):

| Metric | Example Attribute(s) |
|--------|----------------------|
| a. Number of Shares Outstanding | `CommonStockSharesOutstanding`, `EntityCommonStockSharesOutstanding`, etc. |
| b. Revenues | `Revenues` |
| c. Cost of Sales | `CostsAndExpenses`, `CostOfGoodsAndServicesSold`, etc. |
| d. Net Income | `ProfitLoss`, etc. |
| e. Operating Cash Flow | `NetCashProvidedByUsedInOperatingActivities` |
| f. Investing Cash Flow | `NetCashProvidedByUsedInInvestingActivities` |
| g. Financing Cash Flow | `NetCashProvidedByUsedInFinancingActivities` |
| h. Earnings Per Share (EPS) | `EarningsPerShareBasic` |
| i. Dividend Per Share | `CommonStockDividendsPerShareCashPaid` |
| j. Capital Expenditures | `PaymentsToAcquirePropertyPlantAndEquipment` |
| k. Paid Cash Dividends | `DividendsCash` |
| l. Retained Earnings | `RetainedEarningsAccumulatedDeficit` |
| m. Total Debt | `LongTermDebtNoncurrent` |
| n. Total Equity | `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` |

---

💡 **Tip:** It’s often helpful to match the numerical values in the API with those reported in the latest 10-K to identify the appropriate `us-gaap` attributes.


> ⚠️ **Important:**  
Once you've identified the correct attribute names from the `us-gaap` section, make sure to update the script accordingly.  
Failing to do so may result in errors or missing data during execution.

![image](https://github.com/user-attachments/assets/7d0ba4b9-448b-4260-ae1c-18d34a953b96)

📝 **Configuration Note:**  
Before running the script, update the **CIK** value in the script on **line 5** to match the company you're analyzing.

```python
# Example: line 5 in your script
central_index_key = 731766  # Unitedhealth Group Inc.
```

Inside your folder ```../edgar-API-utils``` run the script:

```bash
python .\utils.py
```
✅ **Output:**  
After a successful run, the script will display a table of financial data directly in the terminal.

UNH: CIK 731766
![image](https://github.com/user-attachments/assets/e4b2a134-c0d3-41a5-bec0-a398b7295e63)



---

☕ **Support This Project**  
If this tool helped you, consider [buying me a coffee](https://coff.ee/cern).  
Your support keeps the project alive and growing!

[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20me%20a%20coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://coff.ee/cern)


