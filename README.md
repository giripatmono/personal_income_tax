# CALCULATE PERSONAL INCOME TAX 
This is a script that calculates the Personal Income Tax in Indonesia
based on the taxpayer’s annual income and tax reliefs.

### Taxation Scheme
- Annual income from 0 to 50.000.000 IDR - tax rate is 5%
- Annual income from 50.000.000 to 250.000.000 IDR - tax rate is 15%
- Annual income from 250.000.000 to 500.000.000 IDR - tax rate is 25%
- Annual income above 500.000.000 IDR - tax rate is 30%

### Tax Relief
Tax reliefs are based on the person’s profile :
- TK0 - Single : 54.000.000 IDR
- K0 - Married with no dependant : 58.500.000 IDR
- K1 - Married with 1 dependant : 63.000.000 IDR
- K2 - Married with 2 dependants : 67.500.000 IDR
- K3 - Married with 3 dependants : 72.000.000 IDR

### Requirements
This script requires python version 3 
 
### Testing
To run unit testing, run the test.py script
```
$ python test.py
```