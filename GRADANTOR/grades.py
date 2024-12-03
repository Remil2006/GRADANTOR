

def notas(notafinal,estudiante):
    print(notafinal)
    if notafinal >= 90:
        print(f"Has sacado una A, sigue asi {estudiante} !!")
    elif notafinal <= 89.99 and notafinal >= 80:
        print(f"Has sacado una B, esta muy bien casi sun sobresaliente {estudiante}")
    elif notafinal <= 79.99 and notafinal >= 70:
        print(f"Has sacado una C, Puedes mejorar {estudiante} ")
    elif notafinal <= 69.99 and notafinal >= 60:
        print(f"Has sacado una D, tienes que estudiar un poco mas {estudiante}")
    else:
        print(f"has sacaod una F, has suspendido {estudiante} tienes que estudiar mucho mas para sacar una buena nota")