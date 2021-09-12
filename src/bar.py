class Bar:

    def __init__(self, till):
        self.till = till
        self.guests = []
        self.items = [
            {
                "name": "Tennents",
                "price": 3.60
            },
            {
                "name": "Red Wine",
                "price": 4.50
            },
            {
                "name": "Kebab",
                "price": 5.60
            }
        ]

    def start_tab(self, guest):
        self.guests.append({
            "object": guest,
            "tab": 0,
            "items_purchased" : []
        })

    def get_tab(self, guest):
        for person in self.guests:
            if person["object"] == guest:
                return person["tab"]

    def get_item_price(self, item):
        for food in self.items:
            if food["name"] == item:
                return food["price"]

    def adjust_till(self, amount):
        self.till += amount

    def sell(self, guest_name, item):
        for guest in self.guests:
            if guest_name == guest["object"].name:
                guest["tab"] += self.get_item_price(item)
                guest["items_purchased"].append(item)

    def close_tab(self, guest):
        for person in self.guests:
            if person["object"].name == guest.name:
                self.adjust_till(person["tab"])
                guest.adjust_wallet(-person["tab"])
                self.guests.remove(person)
