import locale
locale.setlocale(locale.LC_ALL, '')


# calculate annual taxable income
def get_annual_taxable_income(monthly_salary=None, profile=None):
    return max((monthly_salary*12)-get_tax_relief(profile), 0)


# calculate annual tax income
def calculate_tax_income(monthly_salary=None, profile=None):
    annual_taxable_income = get_annual_taxable_income(monthly_salary, profile)
    tax_income = 0.05 * min(annual_taxable_income, 50000000)
    if annual_taxable_income > 50000000:
        tax_income += 0.15 * min(annual_taxable_income-50000000, 200000000)
    if annual_taxable_income > 250000000:
        tax_income += 0.25 * min(annual_taxable_income-250000000, 250000000)
    if annual_taxable_income > 500000000:
        tax_income += 0.3 * (annual_taxable_income-500000000)
    return int(tax_income)


# tax relief
def get_tax_relief(profile=None):
    tax_profile = {
        'TK0': 54000000,
        'K0': 58500000,
        'K1': 63000000,
        'K2': 67500000,
        'K3': 72000000,
    }
    return tax_profile.get(profile, 0)
