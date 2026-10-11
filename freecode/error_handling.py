def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(1)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative
    

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    print(process_data(2))
except ValueError:
    print('Handled at higher level')
    
    
def main():
    user_input = input('Enter ISBN and length: ')
    
    if not "," in user_input:
         raise IndexError("Enter comma-separated values.")
       
    values = user_input.split(',')
    
    try:
          length = int(values[1].strip()) 
    except ValueError:
        
            raise ValueError("Length must be a number.") from None
        print(values)
    # isbn = values[0]
    # length = int(values[1])
    print(len())
if __name__ == "__main__":
    try:
        main()
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
