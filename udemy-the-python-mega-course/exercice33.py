def celcius_to_fahrenheit(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=(9/5)*c+32
        return f

print(celcius_to_fahrenheit(-280))
