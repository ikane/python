def celcius_to_fahrenheit(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=(9/5)*c+32
        return f


temperatures=[10,-20,-289,100]

with open("temperatures.txt","w") as f:
    for t in temperatures:
        if t > -273.15:
            f.write(str(celcius_to_fahrenheit(t)) + "\n")
