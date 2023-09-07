# Bank-management-system
This bank management system project  performs the essential functions of banking software. It lets the user
* See database records.
* Create records
* Delete records
   ## file:///home/joy/Videos/Screencasts/Screencast%20from%2007-09-2023%2003:21:58%20ALASIRI.webm


file:///home/joy/Pictures/Screenshots/Screenshot%20from%202023-09-07%2015-43-45.png


## Table of Contents
- [Technologiesused](#technologiesused)
- [Installation](#installation)
- [Usage](#usage)

- [Author & License](#author--license)

## Technologies used
![python version](https://img.shields.io/badge/python-3.10.12+-blue.svg)
![pytest version](https://img.shields.io/badge/pytest-7.1.3+-cyan.svg)
![sqlalchemy version](https://img.shields.io/badge/sqlalchemy-2.0%2B-blue.svg)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JOY19ANYANGO/Bank-management-system.git
```

### 2. Navigate to the project's directory

```bash
cd Bank-management-system
```

### 3. Install all the required dependencies

The root directory of this repository contains the `Pipfile` with all the required Python libraries for this project and restricts them to this repository.

To install `pytest` and any other required libraries, run:

```python
pipenv install
```

### 4. Enter the pipenv shell

```python
pipenv shell
```


## Usage
* To launch the project follow this commands:
```python
cd lib/dbfolder
```
```python
python3 main.py
```

- Use the following options to navigate through the main menu:

   - Press 'S' to view records.
   - Press 'F' to add new records.
   - Press 'R' to delete a customer and associated data.
   - Press 'Q' to quit the program.

### View Records Menu

#### Customer Records

- Press 'C' to see a list of all customers.

#### Transaction Records

- Press 'T' to see transaction records for a specific customer.

#### Account Records

- Press 'A' to see account records for a specific customer.

#### Back to Main Menu

- Press 'B' to return to the main menu.

### Add Records Menu

#### Add a New Customer

- Press 'C' to add a new customer.
- Enter the first name and last name of the customer when prompted.

#### Add a New Transaction

- Press 'T' to add a new transaction.
- Enter the required details for the transaction, such as the account ID, amount, and description (deposit or withdrawal).

#### Add a New Account

- Press 'A' to add a new account.
- Provide the account type (savings or current), initial deposit, and customer ID.

#### Back to Main Menu

- Press 'B' to return to the main menu.

### Delete Customer

To delete a customer and their associated data:

- Press 'R' in the main menu.
- Enter the customer's ID when prompted.
- Confirm the deletion.

#
## 5. License

This project is licensed under the [license name]. See the [LICENSE](LICENSE) file for details.



## Author & License

Authored by [Joy Anyango](https://github.com/JOY19ANYANGO).

Licensed under the [MIT](https://choosealicense.com/licenses/mit/)

