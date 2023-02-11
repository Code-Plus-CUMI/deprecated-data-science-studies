#		**********************
#		* Python For Finance *
#		**********************
#

import numpy_financial as npf

# 0) Future Value (FV)
#
# Assume you invest $1000 for 5 years at an annual return rate of 8%
# and you do not make any deposits later. How much your investment will
# be worth after these 5 years?

investment = 1000
deposits = 0
years = 5
rate = 0.08 # 8%

# - rate: annual rate return
# = nper: number of periods
# - pmt: payments
# - pv: present value invested
investment_worth = npf.fv(
	rate=rate
	, nper=years
	, pmt=deposits
	, pv=investment
)

print(f'Future Value: ${investment_worth}')



# 1) Present Value (PV)
#
# Assume you are willing for an investment that has an annual interest rate
# (annual rate return) of 10% and a future value of $1000 over 8 years.
# How much do you have to invest to achieve it?

rate = 0.10
years = 8
future_value = 1000
payments = 0

# - rate: annual rate return
# - nper: number of periods
# - pmt: payments
# - fv: future value
present_value = npf.pv(
	rate=rate
	, nper=years
	, pmt=payments
	, fv=future_value
)

print(f'Present Value: ${present_value}')


# 2) Monthly Loan Payments
#
# Assume you got a loan of $100000 with an annual rate of 7%. How much you
# have to pay monthly to finish this loan in 5 years?

rate_per_month = 0.07 / 12
months = 5 * 12
present_value = 100000 # loan value
future_value = 0 # loan finished

monthly_payments = npf.pmt(
	rate=rate_per_month
	, nper=months
	, pv=present_value
	, fv=future_value
)

print(f'${monthly_payments} per month')



# 3) Savings
#
# Assume you are willing to make deposits in a bank with a 10% annual rate
# of return. How much you have to deposit for each month in order to get
# $50000 after 5 years

rate_per_month = 0.10 / 12
months = 5 * 12
present_value = 0
future_value = 50000

monthly_deposits = npf.pmt(
	rate=rate_per_month
	, nper=months
	, pv=present_value
	, fv=future_value
)

print(f'${monthly_deposits} per month')



# 4) IRR
#
# Assume you have two investments:
#
# Option 1:
# - Requires 50k in investment
# - Will pay 10k, 25k, 25k, 35k, 42k for each year over 5 years
#
# Option 2:
# - Requires 30k in investment
# - Will pay 10k, 13k, 18k, 25k, 20k for each year over 5 years

cashflow_1 = [-50000, 10000, 25000, 25000, 35000, 42000]
cashflow_2 = [-30000, 10000, 13000, 18000, 25000, 20000]

irr_1 = npf.irr(cashflow_1)
irr_2 = npf.irr(cashflow_2)

print(f'Option 1: {irr_1}')
print(f'Option 2: {irr_2}')
print('The better is the one with the highest IRR')