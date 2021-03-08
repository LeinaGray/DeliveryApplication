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
            print(str(self.package_id) + ": " + self.address + ", " + self.city + ", " + self.state + ", " + str(
                self.package_zip) + ". Deadline: " + str(
                self.deadline.time()) + ". Status: " + status + ".")
        elif status == "Loaded on truck 2":
            print(str(self.package_id) + ": " + self.address + ", " + self.city + ", " + self.state + ", " + str(
                self.package_zip) + ". Deadline: " + str(
                self.deadline.time()) + ". Status: " + status + " @ " + str(self.time_loaded.time()))
        else:
            print(str(self.package_id) + ": " + self.address + ", " + self.city + ", " + self.state + ", " + str(
                self.package_zip) + ". Deadline: " + str(
                self.deadline.time()) + ". Status: " + status + " @ " + str(self.time_delivered.time()))
