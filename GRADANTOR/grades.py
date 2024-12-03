

def notas(notafinal):
    print(notafinal)
    if notafinal >= 90:
        print("A")
    elif notafinal <= 89.99 and notafinal >= 80:
        print("B")
    elif notafinal <= 79.99 and notafinal >= 70:
        print("C")
    elif notafinal <= 69.99 and notafinal >= 60:
        print("D")
    else:
        print("F")