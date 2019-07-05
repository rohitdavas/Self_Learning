from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'

# triple quote practise
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,                                                                                                                                                                                                                                              
%d bottles of beer on the wall!
'''
bottles_of_beer = 3
while bottles_of_beer > 1:
    print REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1)
    bottles_of_beer -= 1

#3 lasses
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def overdrawn(self):
        return self.balance < 0

my_account = BankAccount(15)
my_account.withdraw(5)
print my_account.balance

