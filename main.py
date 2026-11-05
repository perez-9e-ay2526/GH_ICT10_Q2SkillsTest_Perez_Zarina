# Confirm Element Symbol

from pyscript import display, document

def confirm_element(e):
    document.getElementById('output').innerHTML = ''
    input_symbol = str(document.getElementById('symbol').value)

    symbol = input_symbol.title()

    dict_nonmetals   = {
        'H' : ('Symbol: H', 'Element: Hydrogen', 'Atomic Mass: 1.008', 'Atomic Number: 1'),
        'He' : ('Symbol: He', 'Element: Helium', 'Atomic Mass: 4.002602', 'Atomic Number: 2'),
        'C' : ('Symbol: C', 'Element: Carbon', 'Atomic Mass: 12.011', 'Atomic Number: 6'),
        'N' : ('Symbol: N', 'Element: Nitrogen', 'Atomic Mass: 14', 'Atomic Number: 7'),
        'O' : ('Symbol: O', 'Element: Oxygen', 'Atomic Mass: 15.999', 'Atomic Number: 8'),
        'F' : ('Symbol: F', 'Element: Flourine', 'Atomic Mass: 18.998', 'Atomic Number: 9'),
        'Ne' : ('Symbol: Ne', 'Element: Neon', 'Atomic Mass: 20.180', 'Atomic Number: 10'),
        'P' : ('Symbol: P', 'Element: Phosphorus', 'Atomic Mass: 30.974', 'Atomic Number: 15'),
        'S' : ('Symbol: S', 'Element: Sulfur', 'Atomic Mass: 32.06', 'Atomic Number: 16'),
        'Cl' : ('Symbol: Cl', 'Element: Chlorine', 'Atomic Mass: 35.45', 'Atomic Number: 17'),
        'Ar' : ('Symbol: Ar', 'Element: Argon', 'Atomic Mass: 39.948', 'Atomic Number: 18'), 
        'Se' : ('Symbol: Se', 'Element: Selenium', 'Atomic Mass: 78.971', 'Atomic Number: 34'), 
        'Br' : ('Symbol: Br', 'Element: Bromine', 'Atomic Mass: 79.904', 'Atomic Number: 35'), 
        'Kr' : ('Symbol: Kr', 'Element: Krypton', 'Atomic Mass: 83.798', 'Atomic Number: 36'), 
        'I' : ('Symbol: I', 'Element: Iodine', 'Atomic Mass: 126.90', 'Atomic Number: 53'), 
        'Xe' : ('Symbol: Xe', 'Element: Xenon', 'Atomic Mass: 131.29', 'Atomic Number: 54'), 
        'Rn' : ('Symbol: Rn', 'Element: Radon', 'Atomic Mass: 222', 'Atomic Number: 86'),
    }

    nonmetal_checker = symbol in dict_nonmetals

    element_details = display(*dict_nonmetals[symbol], target='output')

    display_message = {
        False: f'Sorry! Your input is not a non-metal. Try again.',
        True: element_details
    }
    display(display_message[nonmetal_checker], target='output')



