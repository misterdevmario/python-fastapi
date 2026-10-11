test_settings = {'theme': 'light'}
def add_setting(dictionary, keyvalue):
    key, value = keyvalue[0].lower(), keyvalue[1].lower()
 
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dictionary, keyvalue):
    key, value = keyvalue[0].lower(), keyvalue[1].lower()
    if key in dictionary:
        dictionary[key] = value
       
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."    
def delete_setting(dictionary, key):
    # Treat it directly as a string, no [0] indexing needed!
    key = key.lower()
    
    if key in dictionary:
        dictionary.pop(key) 
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"   

def view_settings(dict_of_settings):
    result = "Current User Settings:\n"
    if not dict_of_settings:
        return "No settings available."
    else:
        for key, value in dict_of_settings.items():
            result += f"{key.capitalize()}: {value}\n" 
    return result




print(add_setting({'theme': 'light'}, ('VOLUME', 'dark')))
#print(delete_setting({'theme': 'light'}, 'VOLUME'))
print(view_settings(test_settings))