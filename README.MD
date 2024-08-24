# Account Class

The `Account` class represents a basic bank account with features for depositing, withdrawing, transferring funds, and viewing the account balance. The class includes validation and error handling to ensure correct operation.

## Features
- **Account Creation**: Initialize an account with an account number, account holder's name, and an optional initial balance (default: 0.0).
- **Deposit Funds**: Safely deposit a positive float amount into the account.
- **Withdraw Funds**: Withdraw funds with validation to ensure sufficient balance and correct input.
- **Transfer Funds**: Transfer funds between accounts with checks for sufficient balance and valid amounts.
- **Balance Inquiry**: Retrieve the current balance of the account.

## Usage

### Creating an Account
To create an account, initialize it with an account number, the account holder's name, and an optional initial balance.

```python
account1 = Account(ac_no=101, name="Alice", bal=1000.0)
```

### Checking Balance
You can check the balance of the account:

```python
account1.get_balance()  # Displays the current balance in the account
```

### Depositing Funds
To deposit funds, call the `deposit()` method with a positive float value:

```python
account1.deposit(500.0)
```

### Withdrawing Funds
To withdraw funds, call the `withdraw()` method with a valid float amount, ensuring it does not exceed the account's balance:

```python
account1.withdraw(200.0)
```

### Transferring Funds
To transfer funds from one account to another, use the `transfer()` method:

```python
account1.transfer(account2, 300.0)
```

## Error Handling
- **Type Checking**: Ensures that the account number, name, and balance are of the correct type.
- **Value Validation**: Ensures that the balance is non-negative and that transactions (deposit, withdrawal, transfer) use valid amounts.
- **Exception Handling**: Raises `TypeError` for incorrect types and `ValueError` for invalid transactions or insufficient balance.