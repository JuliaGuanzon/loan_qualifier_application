# Loan Qualifier Application

The loan qualifier application is a helpful tool for people who are looking to apply for a loan. This application is useful to any user as it is an interactive application that gathers qualifying loans for each user's circumstance. The best feature in this program is the user's ability to save the loans they have qualified for in a spreadsheet. It saves the user time by creating a list of loan where the bank's loan criteria is met (ie. Debt to Income, maximum loan to value,minimum credit score). This enhancement to the application will make it efficient and painless for the user to find a loan.

---

## Technologies

In order for this program to run, this application must be used in either Git Bash or VS Code, as it was written in Python. To run the program, a programmer must have Anaconda/Python installed on their computer. To ensure the code works, please open the file in a dev environment.

**Systems**

conda 4.10.3

python 3.7

**Packages**

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entry-point.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs


---

## Installation Guide

As mentioned above, to ensure that there are no errors when running this application, the user or programmer must use Git Bash or Visual Studio Code to access the application file. The operating systems and program versions are mentioned above and are highly recommended when running the program.

Additional installs are needed before running the program.

```python
  pip install fire
  pip install questionary
```
---

## Examples

This is a modular application, therefore parts of this application are referenced in the main file and are hosted on different files. The code below pulls these outside files that contain the code that helps us run the app.py file. It also includes imports that help in running some of the functions in the file. 

```
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv, save_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value
```
The lines of code seen in the picture below tell us that the user must type in the file they chose to use. By typing the file name correctly, it will find and open the file the user needs. If the file name is not correctly entered or does not exist, then the application will tell the user the file was not found.

![load_bank_data](https://user-images.githubusercontent.com/84649228/125153667-4183a080-e10a-11eb-990d-479986cfe059.PNG)

This portion of code prompts users to fill in their information. By using questionary, we are able to ask open-ended questions and take the data and compare the information against the criteria for loans. The information a user provides must be a numerical value in order for our application to calculate debt-to-income and loan-to-value.

```
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)
```
The next portion of code determines which loans a user is qualify for. It takes the information gathered and it calculates the monthly debt-to-income and loan-to-value ratios. Then it filters the loan list to determine the qualifying loans based on user information.

```
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):

    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")
    
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered

```

The run function runs the application for saving_qualifying_loans, as seen below.

![run_function](https://user-images.githubusercontent.com/84649228/125153673-48aaae80-e10a-11eb-9a08-e7502b2033c0.PNG)

The saving_qualifying_loans function allow for the saving of the qualifying loan list file. It prompts the user to either save the file or to decline saving the loan list.

![save_qualifying_loans](https://user-images.githubusercontent.com/84649228/125153674-4b0d0880-e10a-11eb-9616-89be136651ac.PNG)

The last lines of code, in the image above, allows us to declare the "run" functions and execute it in command-line interface.

---

## Usage

To use the loan qualifier application, the repository will need to be cloned from GitHub and into a local repository.

In the loan_qualifier_application folder, enter into the loan_qualifier_information. Enter into the dev environment by commanding: 

```
 conda activate dev
```
![opening_repo_file](https://user-images.githubusercontent.com/84649228/125153554-56136900-e109-11eb-8da5-0ce748334148.PNG)

Next, use the code:

```
python app.py
```
to run the file.

The file path necessary to use this application is *./data/daily_rate_sheet.csv*

Next, the user will be prompted to fill in the following criteria information. When the user is finished inputting the information, they will be asked "Would you like to save?" This can be answered with a "y" or "n".

![entering_borrower_info](https://user-images.githubusercontent.com/84649228/125153522-2a907e80-e109-11eb-96e5-a9cb23dccd99.PNG)

For a user to see the list of loans they qualified for, the user will need to open the data data file and command the opening of the file in the terminal. The file is saved as qualifying_loans.csv.

```
cd data

explorer qualifying_loans.csv
```

![open_qualifying_loan_list](https://user-images.githubusercontent.com/84649228/125153551-527fe200-e109-11eb-8c65-28d2978d2a0d.PNG)

Below is the list of loans a user has qualified for based on their information and the criteria of the loan.

![qualifying_loan_list](https://user-images.githubusercontent.com/84649228/125153556-590e5980-e109-11eb-84d8-adae7a7eaf23.PNG)


---

## Contributors

[Julia Guanzon](www.linkedin.com/in/julia-guanzon)

## License

MIT License
kjs;lkjsdf;kljd