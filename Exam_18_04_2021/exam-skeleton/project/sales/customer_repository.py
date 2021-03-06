from project.sales.customer import Customer


class CustomerRepository:

    def __init__(self):
        self.customers = []

    def add(self, customer: Customer):
        if customer in self.customers:
            raise ValueError(f"Customer {customer.name} already exists.")

        self.customers.append(customer)

    def remove(self, customer_name: str):
        customer = [cust for cust in self.customers if cust.name == customer_name]
        if not customer:
            raise ValueError(f"Customer {customer_name} does not exist.")
        self.customers.remove(customer[0])
        return f'Removed customer: {customer_name}'

    def find(self, customer_name: str):
        customer = [cust for cust in self.customers if cust.name == customer_name]
        if customer:
            return customer[0]
        return 'None'
