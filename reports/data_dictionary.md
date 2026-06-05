# Mutual Fund Analytics Project
## Data Dictionary

---

# 1. fund_master

Source: AMFI Scheme Master

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique scheme identifier |
| fund_house | Text | Asset Management Company |
| scheme_name | Text | Mutual fund scheme name |
| category | Text | Equity/Debt/Hybrid category |
| sub_category | Text | Scheme sub-category |
| plan | Text | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Decimal | Expense ratio percentage |
| exit_load_pct | Decimal | Exit load percentage |
| min_sip_amount | Decimal | Minimum SIP amount |
| min_lumpsum_amount | Decimal | Minimum lump-sum amount |
| fund_manager | Text | Fund manager |
| risk_category | Text | Risk classification |
| sebi_category_code | Text | SEBI category code |

---

# 2. nav_history

Source: Historical NAV Dataset

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme identifier |
| date | Date | NAV date |
| nav | Decimal | Net Asset Value |

---

# 3. scheme_performance

Source: Performance Dataset

| Column | Data Type | Description |
|----------|----------|----------|
| return_1yr_pct | Decimal | 1-year return |
| return_3yr_pct | Decimal | 3-year return |
| return_5yr_pct | Decimal | 5-year return |
| benchmark_3yr_pct | Decimal | Benchmark return |
| alpha | Decimal | Excess return measure |
| beta | Decimal | Volatility measure |
| sharpe_ratio | Decimal | Risk-adjusted return |
| sortino_ratio | Decimal | Downside-risk-adjusted return |
| std_dev_ann_pct | Decimal | Annualized volatility |
| max_drawdown_pct | Decimal | Maximum drawdown |
| expense_ratio_pct | Decimal | Expense ratio |
| morningstar_rating | Integer | Rating score |
| risk_grade | Text | Risk level |

---

# 4. investor_transactions

Source: Investor Activity Dataset

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor identifier |
| transaction_date | Date | Transaction date |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Decimal | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier classification |
| age_group | Text | Investor age segment |
| gender | Text | Investor gender |
| annual_income_lakh | Decimal | Annual income |
| payment_mode | Text | Mode of payment |
| kyc_status | Text | KYC verification status |

---

# 5. portfolio_holdings

Source: Portfolio Holdings Dataset

Contains security-level holdings of mutual fund schemes.

---

# 6. aum_by_fund_house

Source: AUM Dataset

Tracks Assets Under Management by fund house.

---

# 7. benchmark_indices

Source: Benchmark Index Dataset

Historical benchmark index values.

---

# 8. category_inflows

Source: Category Flow Dataset

Tracks category-wise net inflows and outflows.

---

# 9. industry_folio_count

Source: Industry Statistics Dataset

Industry-level folio counts by period.

---

# 10. monthly_sip_inflows

Source: SIP Statistics Dataset

Monthly SIP collections and growth trends.

---