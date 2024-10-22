def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    cm_in_inches=n*0.3937007874016
    return round(cm_in_inches, 1)

def ft_inches_to_cm(ft, inches):
    ft_cm=ft*30.48
    in_cm=inches*0.3937007874016
    suma=ft_cm+in_cm
    return round(suma,1)

if __name__ == "__main__":
    # only execute when you run this module
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'198cm is {cm_to_inch(198)}in')
    print(f'10ft 2in is {ft_inches_to_cm(10,2)}cm')
    