# Name: Frank Morales    Student ID: 001122005

from PackageHashTable import PackageHashTable
from datetime import datetime, date, time

# Instantiate the Package Hash Table
packages = PackageHashTable()

# This while loop runs the deliver function
# until there are no more packages to deliver
while packages.all_delivered() is not True:
    packages.deliver()

# When all packages have been delivered, print
# out the results. The if statement is for these
# print statements to run just the first time the
# program runs.
print("All the packages have been delivered!")
print("Time: " + str(packages.delivery_time.time()))
print("Total miles traveled: " + str(packages.miles))

# Print out prompt for user to enter time for
# status during that time
hr, minutes = 1, 0
prompt = True
while prompt:
    try:
        correct_time = False
        while not correct_time:
            print("\nPlease enter the time from 8:00-17:00, or enter a string to exit")
            hr = int(input("Hour (8-17): "))
            if not 8 <= hr <= 17:
                print("Please enter valid hour.")
            else:
                minutes = int(input("Minute (0-59): "))
                if not 0 <= minutes <= 59 or (hr == 17 and minutes != 0):
                    print("Please enter valid minute.")
                else:
                    correct_time = True
        packages.print_package_hash_table(datetime.combine(date.today(), time(hr, minutes)))

    # Once the user inputs a string, the program finally
    # ends here in the except statement.
    except ValueError:
        print("\nThank you! Have a great day.")
        prompt = False
