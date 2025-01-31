from termcolor import colored
class Package:

    def __init__(self, package_id, address, city, state, package_zip, deadline, weight,
                 truck_num, delay_time, group, status, time_loaded, time_delivered):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.package_zip = package_zip
        self.deadline = deadline
        self.weight = weight
        self.truck_num = truck_num
        self.delay_time = delay_time
        self.group = group
        self.status = status
        self.time_loaded = time_loaded
        self.time_delivered = time_delivered

    # This method simply prints out the package
    def print_package(self, status):
        if status == "Undelivered":
            print(colored(str(self.package_id) + ': ' + self.address + ', ' + self.city + ", " + self.state + ", " + str(
                self.package_zip) + ".", attrs=['underline']))
            print(colored('   Deadline: ', attrs=['bold']) + str(self.deadline.time()) + ".")
            print(colored('   Status: ', attrs=['bold']) + colored(status + ".\n", 'red', attrs=['bold']))
        elif status == "Loaded on truck 2":
            print(colored(str(self.package_id) + ': ' + self.address + ', ' + self.city + ", " + self.state + ", " + str(
                self.package_zip) + ".", attrs=['underline']))
            print(colored('   Deadline: ', attrs=['bold']) + str(self.deadline.time()) + ".")
            print(colored('   Status: ', attrs=['bold']) + colored(status + ".", 'yellow', attrs=['bold']))
            print(colored('   Time Loaded: ', attrs=['bold']) + str(self.time_loaded.time()) + "\n")
        else:
            print(colored(str(self.package_id) + ': ' + self.address + ', ' + self.city + ", " + self.state + ", " + str(
                self.package_zip) + ".", attrs=['underline']))
            print(colored('   Deadline: ', attrs=['bold']) + str(self.deadline.time()) + ". ")
            print(colored('   Status: ', attrs=['bold']) + colored(status + ". ", 'green', attrs=['bold']))
            print(colored('   Time Delivered: ', attrs=['bold']) + str(self.time_delivered.time()) + "\n")
