import unittest
from sut import Account


class TestSut(unittest.TestCase):

    def setUp(self):
        # Setting up accounts for tests
        self.fab = Account("Fabian", 3000)
        self.ata = Account("Ata", 2500)

# ---------------Desposit & Balance Check --------
    def test_deposit(self):
        # Testing existing Balance
        self.assertEqual(self.fab.balance(), 3000)
        self.assertEqual(self.ata.balance(), 2500)
        # Making deposit
        self.fab.deposit(3000)
        self.ata.deposit(2500)
        # Asserting change
        self.assertEqual(self.fab.balance(), 6000)
        self.assertEqual(self.ata.balance(), 5000)

# ---------------Withdraw & Balance check --------
    def test_withdraw(self):
        # Testing existing Balance
        self.assertEqual(self.fab.balance(), 3000)
        self.assertEqual(self.ata.balance(), 2500)
        # Making Withdraw
        self.fab.withdraw(1500)
        self.ata.withdraw(1250)
        # Asserting change
        self.assertEqual(self.fab.balance(), 1500)
        self.assertEqual(self.ata.balance(), 1250)

# ---------------Transfers & Balance check -------
    def test_transferTo(self):
        # Testing existing Balance
        self.assertEqual(self.fab.balance(), 3000)
        self.assertEqual(self.ata.balance(), 2500)
        # Making Transfers
        self.ata.transfer_to(self.fab, 1000)
        self.ata.transfer_from(self.fab, 500)
        # Asserting change
        self.assertEqual(self.fab.balance(), 3500)
        self.assertEqual(self.ata.balance(), 2000)

# ---------------Negative Balance -----------------
    def test_negBalanceCheck(self):
        # Testing existing Balance
        self.assertEqual(self.fab.balance(), 3000)
        # Withdraw funds
        self.fab.withdraw(3001)
        # Assert: Validating balance
        self.assertTrue(self.fab.balance() < 0)
        print("\nWarning:", self.fab.name(), "has balance of:", self.fab.balance())


if __name__ == '__main__':
    unittest.main()
