def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
        