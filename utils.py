from data_fetching import CompanyFacts
import aiohttp
import asyncio

central_index_key = 000000

HEADER = {'User-Agent': 'email@email.com'}
url = "https://data.sec.gov/api/xbrl/companyfacts/CIK{}.json"
base = "CIK{}"
url_concepts = "https://data.sec.gov/api/xbrl/companyconcept/{}/us-gaap/{}.json"
facts = CompanyFacts("your_company_name")
hashMap = {}


async def get_shares_outstanding(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "CommonStockSharesOutstanding")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("shares", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "SharesOutst", short_val)

async def get_revenues(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "Revenues")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "Revenu", short_val)


async def get_cost_of_sales(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "CostsAndExpenses") 
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "CostOfSales", short_val)

async def get_net_income(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "ProfitLoss")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "NetInc", short_val)

async def get_operating_cash_flow(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "NetCashProvidedByUsedInOperatingActivities")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "OpCashFlow", short_val)

async def get_investing_cash_flow(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "NetCashProvidedByUsedInInvestingActivities")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "InvCashFlow", short_val)

async def get_financing_cash_flow(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "NetCashProvidedByUsedInFinancingActivities")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "FinCashFlow", short_val)   


async def get_eps(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "EarningsPerShareBasic")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD/shares", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                facts.add_fact(item.get("fy"), "EPS", item.get("val"))              

async def get_dividends(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "CommonStockDividendsPerShareCashPaid")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD/shares", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                facts.add_fact(item.get("fy"), "Divid", item.get("val"))

async def get_capital_expenditures(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "PaymentsToAcquirePropertyPlantAndEquipment")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "CapExpend", short_val)

async def get_div_cash(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "DividendsCash")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "DivPaid", short_val)

async def get_retained_earnings_balance(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "RetainedEarningsAccumulatedDeficit")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "RetEarnBal", short_val)


async def get_total_debt(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "LongTermDebtNoncurrent")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "Debt", short_val)

async def get_total_equity(cik):
    local_url = url_concepts.format(base.format(str(cik).zfill(10)), "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest")
    data = {}
    async with aiohttp.ClientSession(headers=HEADER) as session:
        async with session.get(local_url) as response:
            data = await response.json()
    
    if "units" in data:
        shares = data.get("units", {}).get("USD", [])
        for item in shares:
            if item.get("form", "").upper() == "10-K":
                short_val = int(str(int( item.get("val")))[:6])
                facts.add_fact(item.get("fy"), "Equity", short_val)

async def main(cik):
    await asyncio.gather(
        get_dividends(cik),
        get_revenues(cik),
        get_cost_of_sales(cik),
        get_net_income(cik),
        get_shares_outstanding(cik),
        get_operating_cash_flow(cik),
        get_investing_cash_flow(cik),
        get_financing_cash_flow(cik),
        get_eps(cik),
        get_capital_expenditures(cik),
        get_div_cash(cik),
        get_retained_earnings_balance(cik),
        get_total_debt(cik),
        get_total_equity(cik)
    )
    df = facts.to_dataFrame()
    print(df)

if __name__ == "__main__":
    asyncio.run(main(central_index_key))
