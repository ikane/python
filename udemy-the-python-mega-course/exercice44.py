def celcius_to_fahrenheit(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=(9/5)*c+32
        return f


temperatures=[10,-20,-289,100]

for t in temperatures:
    print(celcius_to_fahrenheit(t))
