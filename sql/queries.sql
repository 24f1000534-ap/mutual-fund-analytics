----------------------------------------------------
-- 1. Top 5 Fund Houses by AUM
----------------------------------------------------

SELECT
    fund_house,
    MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

----------------------------------------------------
-- 2. Average NAV by Month
----------------------------------------------------

SELECT
    substr(nav_date,1,7) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

----------------------------------------------------
-- 3. Total Transactions by State
----------------------------------------------------

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

----------------------------------------------------
-- 4. Transaction Amount by Transaction Type
----------------------------------------------------

SELECT
    transaction_type,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

----------------------------------------------------
-- 5. Funds with Expense Ratio Below 1%
----------------------------------------------------

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

----------------------------------------------------
-- 6. Average Return by Category
----------------------------------------------------

SELECT
    category,
    ROUND(AVG(return_3yr_pct),2) AS avg_return_3yr
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
GROUP BY category
ORDER BY avg_return_3yr DESC;

----------------------------------------------------
-- 7. Top 10 Performing Funds (5-Year Return)
----------------------------------------------------

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
ORDER BY return_5yr_pct DESC
LIMIT 10;

----------------------------------------------------
-- 8. Risk Category Distribution
----------------------------------------------------

SELECT
    risk_category,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_category
ORDER BY fund_count DESC;

----------------------------------------------------
-- 9. Average Investment by City Tier
----------------------------------------------------

SELECT
    city_tier,
    ROUND(AVG(amount_inr),2) AS avg_investment
FROM fact_transactions
GROUP BY city_tier;

----------------------------------------------------
-- 10. Highest Sharpe Ratio Funds
----------------------------------------------------

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
ORDER BY sharpe_ratio DESC
LIMIT 10;