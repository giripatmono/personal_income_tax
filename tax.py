import locale
locale.setlocale(locale.LC_ALL, '')


TAX_SCHEME = (
    {
        "min": 0,
        "max": 50000000,
        "tax": 0.05
    },
    {
        "min": 50000000,
        "max": 250000000,
        "tax": 0.15
    },
    {
        "min": 250000000,
        "max": 500000000,
        "tax": 0.15
    },
    {
        "min": 500000000,
        "tax": 0.15
    }
)


# calculate annual taxable income
def get_annual_taxable_income(monthly_salary=None, profile=None):
    return max((monthly_salary*12)-get_tax_relief(profile), 0)


# calculate annual tax income
def calculate_tax_income(monthly_salary=None, profile=None):
    annual_taxable_income = get_annual_taxable_income(monthly_salary, profile)

    # looping untuk setiap tax scheme
    tax_income = 0
    for scheme in TAX_SCHEME:
        if annual_taxable_income > scheme['min']:
            tax_income += scheme['tax'] * min(annual_taxable_income-scheme['min']
                                              , scheme.get('max', annual_taxable_income-scheme['min']))

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
