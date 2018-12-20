import unittest
from tax import calculate_tax_income, get_annual_taxable_income


class TestTaxIncomeCalculation(unittest.TestCase):
    tidak_kawin = 'TK0'
    kawin_tanpa_anak = 'K0'
    kawin_anak_1 = 'K1'
    kawin_anak_2 = 'K2'
    kawin_anak_3 = 'K3'
    gaji_1 = 6500000
    gaji_2 = 25000000
    gaji_3 = 3000000
    gaji_4 = 6000000

    def test_gaji_3_single(self):
        print('\nMonthly Salary: {:n}, Profile:{}'.format(self.gaji_3, self.tidak_kawin))
        print('Annual Taxable Income:{:n}'.format(get_annual_taxable_income(self.gaji_3, self.tidak_kawin)))
        print('Income Tax:{:n}'.format(calculate_tax_income(monthly_salary=self.gaji_3, profile=self.tidak_kawin)))
        self.assertEqual(calculate_tax_income(monthly_salary=self.gaji_3, profile=self.tidak_kawin), 0)

    def test_gaji_4_single(self):
        print('\nMonthly Salary: {:n}, Profile:{}'.format(self.gaji_4, self.tidak_kawin))
        print('Annual Taxable Income:{:n}'.format(get_annual_taxable_income(self.gaji_4, self.tidak_kawin)))
        print('Income Tax:{:n}'.format(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.tidak_kawin)))
        self.assertEqual(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.tidak_kawin), 900000)

    def test_gaji_4_anak_1(self):
        print('\nMonthly Salary: {:n}, Profile:{}'.format(self.gaji_4, self.kawin_anak_1))
        print('Annual Taxable Income:{:n}'.format(get_annual_taxable_income(self.gaji_4, self.kawin_anak_1)))
        print('Income Tax:{:n}'.format(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.kawin_anak_1)))
        self.assertEqual(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.kawin_anak_1), 450000)

    def test_gaji_4_anak_2(self):
        print('\nMonthly Salary: {:n}, Profile:{}'.format(self.gaji_4, self.kawin_anak_2))
        print('Annual Taxable Income:{:n}'.format(get_annual_taxable_income(self.gaji_4, self.kawin_anak_2)))
        print('Income Tax:{:n}'.format(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.kawin_anak_2)))
        self.assertEqual(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.kawin_anak_2), 225000)

    def test_gaji_4_anak_3(self):
        print('\nMonthly Salary: {:n}, Profile:{}'.format(self.gaji_4, self.kawin_anak_3))
        print('Annual Taxable Income:{:n}'.format(get_annual_taxable_income(self.gaji_4, self.kawin_anak_3)))
        print('Income Tax:{:n}'.format(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.kawin_anak_3)))
        self.assertEqual(calculate_tax_income(monthly_salary=self.gaji_4, profile=self.kawin_anak_3), 0)

    def test_gaji_1_anak_1(self):
        print('\nMonthly Salary: {:n}, Profile:{}'.format(self.gaji_1, self.kawin_anak_1))
        print('Annual Taxable Income:{:n}'.format(get_annual_taxable_income(self.gaji_1, self.kawin_anak_1)))
        print('Income Tax:{:n}'.format(calculate_tax_income(monthly_salary=self.gaji_1, profile=self.kawin_anak_1)))
        self.assertEqual(calculate_tax_income(monthly_salary=self.gaji_1, profile=self.kawin_anak_1), 750000)


    def test_gaji_2_single(self):
        print('\nMonthly Salary: {:n}, Profile:{}'.format(self.gaji_2, self.tidak_kawin))
        print('Annual Taxable Income:{:n}'.format(get_annual_taxable_income(self.gaji_2, self.tidak_kawin)))
        print('Income Tax:{:n}'.format(calculate_tax_income(monthly_salary=self.gaji_2, profile=self.tidak_kawin)))
        self.assertEqual(calculate_tax_income(monthly_salary=self.gaji_2, profile=self.tidak_kawin), 31900000)


if __name__ == '__main__':
    unittest.main()
