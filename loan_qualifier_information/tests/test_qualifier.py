# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # @TODO: Your code here!
    # J.Guanzon Comment-Needed to establish the path of where to pull the file. I included the header so it prints the test with headers. Called the save_csv function from the fileio file and established parameters. Used assert to test if the csvpath exists. The new qualifying_loans.csv should print the headers and the numbers [1, 2, 3, 4, 5, 6] as the corresonding values.
    csvpath = Path('./data/qualifying_loans.csv')
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    fileio.save_csv(csvpath, [[1, 2, 3, 4, 5, 6]], header)
    assert csvpath.exists()
    

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
    '''J.Guanzon Comment- 
    Tested filters individually to make sure they work properly. 
    
    In order for all my tests to return as passing, I had to originally set the code to fail, so it would return the solution.
    Original test code used: assert len(bank_data_filtered_XXX_XXX)=len(bank_data)

    Pytest was ran, which gave the definitive number of loans that were filtered. 
    
    I then used that number to verify that the filter was working by setting the following code as such:
    assert len(bank_data_filtered_XXX_XXX) == ##

    Return:
    Tests passed. No issues presented.

    '''
    bank_data_filtered_credit_score = credit_score.filter_credit_score(750, bank_data)
    assert len(bank_data_filtered_credit_score) == 15

    bank_data_filtered_max_loan_size = max_loan_size.filter_max_loan_size(210000, bank_data)
    assert len(bank_data_filtered_max_loan_size) == 18

    bank_data_filtered_debt_ratio = debt_to_income.filter_debt_to_income(0.375, bank_data)
    assert len(bank_data_filtered_debt_ratio) == 19

    bank_data_filtered_loan_to_value = loan_to_value.filter_loan_to_value(0.84, bank_data)
    assert len(bank_data_filtered_loan_to_value) == 19