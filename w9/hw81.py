def convert_temperature(temperature, unit):
    if unit != 'F' and unit != 'C':
        print('Invalid unit')
        return None
    
    if unit == 'F':
        temperature = (temperature - 32) * 5 / 9
    elif unit == 'C':
        temperature = temperature * 9 / 5 + 32
    
    return temperature

def main():
    temperature = float(input('Enter the temperature: '))
    unit = input('Enter the unit (F/C): ').upper()
    temperature = convert_temperature(temperature, unit)
    if temperature is not None:
        print(f'The converted temperature is: {temperature:.2f}')

### Main ###
main()