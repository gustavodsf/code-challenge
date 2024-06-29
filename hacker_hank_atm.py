from typing import Dict, Tuple, Optional

class State:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class ATM:
    def __init__(self, init_state: State, init_balance: int, password: str, transition_table: Dict):
        self.state = init_state
        self._balance = init_balance
        self._password = password
        self._transition_table = transition_table

    def next(self, action: str, param: Optional[str]) -> Tuple[bool, Optional]:
        try:
            for transition_action, check, next_state in self._transition_table[self.state]:
                if action == transition_action:
                    passed, new_balance, res = check(param, self._password, self._balance)
                    if passed:
                        self._balance = new_balance
                        self.state = next_state
                        return True, res
        except KeyError:
            pass
        return False, None

# Define the states
unauthorized = State("unauthorized")
authorized = State("authorized")

# Define the checkers
def login_checker(param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    return (param == atm_password, atm_current_balance, None)

def logout_checker(param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    return (True, atm_current_balance, None)

def deposit_checker(param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    amount = int(param)
    return (True, atm_current_balance + amount, None)

def withdraw_checker(param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    amount = int(param)
    if atm_current_balance >= amount:
        return (True, atm_current_balance - amount, None)
    return (False, atm_current_balance, None)

def balance_checker(param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    return (True, atm_current_balance, atm_current_balance)

# Define the transition table
transition_table = {
    unauthorized: [
        ("login", login_checker, authorized)
    ],
    authorized: [
        ("logout", logout_checker, unauthorized),
        ("deposit", deposit_checker, authorized),
        ("withdraw", withdraw_checker, authorized),
        ("balance", balance_checker, authorized)
    ]
}

# Example usage
if __name__ == "__main__":
    password = "hacker"
    init_balance = 10
    atm = ATM(unauthorized, init_balance, password, transition_table)

    actions = [
        ("withdraw", "5"),
        ("login", "foo"),
        ("login", "hacker"),
        ("withdraw", "15"),
        ("deposit", "20"),
        ("withdraw", "15"),
        ("balance", None),
        ("logout", None)
    ]

    for action, param in actions:
        success, result = atm.next(action, param)
        print(f"Success={success} {atm.state}", end="")
        if result is not None:
            print(f" {result}")
        else:
            print()
