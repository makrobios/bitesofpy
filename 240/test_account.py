from account import Account

# write your pytest functions below, they need to start with test_
import pytest


@pytest.fixture()
def accountA():
    a = Account('me')
    return a

@pytest.fixture()
def accountB():
    b = Account('You', amount=1000)
    return b

def test_account_repr(accountB):
    assert accountB.__repr__() == "Account('You', 1000)"  

def test_account_str(accountA):
    assert accountA.__str__() == "Account of me with starting amount: 0" 

def test_add_transaction(accountA):
    with pytest.raises(ValueError) as exc:
        accountA.add_transaction(12.4)
    assert str(exc.value) == 'please use int for amount'

def test_balance(accountA):
    accountA.amount = 500
    accountA.add_transaction(200)
    assert accountA.balance == 700
    with pytest.raises(AttributeError):
        accountA.balance = 10000

def test__getitem__(accountB):
    accountB.add_transaction(500)
    accountB.add_transaction(37)
    assert list(accountB)[1] == 37

def test_eq(accountA, accountB):
    assert accountA != accountB
    assert accountA < accountB
    assert accountB > accountA

def test_lt(accountA, accountB):
    accountA.add_transaction(1000)
    assert (accountA < accountB) == False
    
def test_add_accounts(accountA, accountB):
    merged = accountA + accountB
    accountNew = Account('They', amount=0)
    assert merged.owner == "me&You"
    assert merged.amount == accountA.amount + accountB.amount
    accountA.add_transaction(570)
    accountB.add_transaction(1430)
    assert sum((accountA + accountB)._transactions) == sum( [ i for i in  (accountA._transactions + accountB._transactions ) ] )
