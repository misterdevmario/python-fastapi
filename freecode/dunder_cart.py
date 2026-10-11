# class Cart:
#    def __init__(self):
#        self.items = []

#    def add(self, item):
#        self.items.append(item)

#    def remove(self, item):
#        if item in self.items:
#            self.items.remove(item)
#        else:
#            print(f'{item} is not in cart')

#    def list_items(self):
#        return self.items

#    def __len__(self):
#        return len(self.items)

#    def __getitem__(self, index):
#        return self.items[index]

#    def __contains__(self, item):
#        return item in self.items

#    def __iter__(self):
#        return iter(self.items)
   

# cart = Cart()
# cart.add('Laptop')
# cart.add('Wireless mouse')
# cart.add('Ergo keyboard')
# cart.add('Monitor')

# for item in cart:
#    print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

# print(len(cart)) # 4
# print(cart[3]) # Monitor

# print('Monitor' in cart) # True
# print('banana' in cart) # False

# cart.remove('Ergo keyboard')

# print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

# cart.remove('banana') # banana is not in cart   


class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)


print(config_obj.server_url)
