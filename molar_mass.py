import re

ATOMIC_MASS = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "S": 32.06,
    "P": 30.974,
    "Cl": 35.45,
    "Na": 22.990,
    "Ca": 40.078
}

def molar_mass(formula):
    tokens = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
    total = 0.0

    for element, count in tokens:
        if element not in ATOMIC_MASS:
            raise ValueError(f"Unknown element: {element}")
        n = int(count) if count else 1
        total += ATOMIC_MASS[element] * n

    return total

formula = input("Enter molecular formula: ").strip()

try:
    mass = molar_mass(formula)
    print(f"Molar mass of {formula}: {mass:.3f} g/mol")
except ValueError as e:
    print("Error:", e)