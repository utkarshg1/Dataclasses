from dataclasses import dataclass, field

@dataclass
class Account:
    ac_no: int
    name: str
    bal: float = field(default=0.0)

    def __post_init__(self):
        self.validate_ac_no()
        self.validate_name()
        self.validate_bal()

    def validate_ac_no(self):
        if not isinstance(self.ac_no, int):
            raise TypeError("Account number should be an integer")
        
    def validate_name(self):
        if not isinstance(self.name, str):
            raise TypeError("Name should be a string")
        
    def validate_bal(self):
        if not isinstance(self.bal, float):
            raise TypeError("Account Balance should be float")
        if self.bal < 0.0:
            raise ValueError("Account Balance cannot be negative")
        
    def get_balance(self):
        print(f"Current balance for ac_no {self.ac_no} is: {self.bal:.2f} INR")
        
    def deposit(self, amt: float):
        if not isinstance(amt, float):
            raise TypeError("Deposit amount must be a float")
        if amt < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.bal += amt

    def withdraw(self, amt: float):
        if not isinstance(amt, float):
            raise TypeError("Withdrawal amount must be a float")
        if amt < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amt > self.bal:
            raise ValueError("Insufficient Balance")
        self.bal -= amt

    def transfer(self, other, amt: float):
        if not isinstance(amt, float):
            raise TypeError("Transfer amount must be a float")
        if amt < 0:
            raise ValueError("Transfer amount cannot be negative")
        if amt > self.bal:
            raise ValueError("Insufficient Balance")
        self.withdraw(amt)
        other.deposit(amt)
