

def druha_mocnica(cislo):
    if (isinstance(cislo, int)):
        x = cislo
    else:
        raise ValueError("Error, musite zadat cislo")
    return x**2;

x = druha_mocnica
y = x

print(x(3))
print(y(3))


