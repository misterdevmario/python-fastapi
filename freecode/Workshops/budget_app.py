class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        # 1. Header: Centered category name in 30 '*' characters
        title = f"{self.name:*^30}\n"
        
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]  # Slice to max 23 characters
            amount = f"{entry['amount']:.2f}"        # Format to 2 decimal places
            
            # Left-align description (23 chars), Right-align amount (7 chars)
            items += f"{description:<23}{amount:>7}\n"
            
        # 3. Total balance line
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
def create_spend_chart(categories):
    # 1. Calculate total spending for each category (withdrawals only)
    spent_per_category = []
    for cat in categories:
        total_withdrawals = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent_per_category.append(total_withdrawals)

    total_spent = sum(spent_per_category)

    # 2. Calculate percentages rounded down to the nearest 10
    # Formula: (spent / total_spent) * 100
    if total_spent > 0:
        percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spent_per_category]
    else:
        percentages = [0 for _ in categories]

    # 3. Build the chart header and bar grid (y-axis from 100 down to 0)
    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        # Format label right-aligned to width 3
        chart += f"{level:>3}| "
        for pct in percentages:
            if pct >= level:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # 4. Horizontal line: 4 spaces padding + 3 '-' per category + 1 extra '-'
    # Length formula: 4 + len(categories) * 3 + 1
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Vertical Category Names
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "    "  # 4 leading spaces
        for name in names:
            if i < len(name):
                chart += f" {name[i]} "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += " \n"
        else:
            chart += " "  # Last line ending requirement

    return chart    
    
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(105.55, 'groceries')

entertainment = Category('Entertainment')
entertainment.deposit(1000, 'initial deposit')
entertainment.withdraw(33.40, 'movies')

business = Category('Business')
business.deposit(1000, 'initial deposit')
business.withdraw(10.99, 'services')

print(create_spend_chart([food, entertainment, business]))