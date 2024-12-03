def banner():#FALTA la instruciones
    print("Bienvenido/a al programa que evalua la qualificacion, instruciones")
    


def notasestudiante():
    notapuntuaciontrabajo = 0
    notafinalpuntuacion = 0
    nombreestudiante = input("Escribe el nombre del estudiante: ")
    #Examen 1
    parcial_1 = int(input("Escribe la puntuacion del parcial 1: "))
    pesparcial_1 = int(input("Escribe el pes del parcial 1: "))
    examen1resultado = (parcial_1/100)*pesparcial_1
    #Examen 2
    parcial_2 = int(input("Escribe la puntuacion del parcial 2: "))
    pesparcial_2 = int(input("Escribe el pes del parcial 2: "))
    examen2resutlado = (parcial_2/100)*pesparcial_2
    #Examen Final
    examen_final = int(input("Enter la puntuacion del examen final: "))
    pesodelexamen = int(input("Escribe el peso del examen: "))
    examenfinalresultado = (examen_final/100)*pesodelexamen
    #TRABAJO ACABADO
    cantidadtrabajos = int(input("Escribe la cantidad de trabajo: "))
    pesodeltrabajo = int(input("Escribe el peso general: "))
    for x in range(cantidadtrabajos):
        pruebapuntuaciontrabajo = int(input("Escribe la puntuacion del trabajo: "))
        notapuntuaciontrabajo = notapuntuaciontrabajo + pruebapuntuaciontrabajo
        notafinal = int(input("Escribe la puntuacion de la nota final: "))
        notafinalpuntuacion = notafinalpuntuacion + notafinal
    if notapuntuaciontrabajo > notafinalpuntuacion:
        notafinalpuntuacion = notafinalpuntuacion
    result = (notapuntuaciontrabajo/notafinalpuntuacion)* pesodeltrabajo
   
        
        


        
        

    
    return [nombreestudiante,examen1resultado,examen2resutlado,examenfinalresultado,result]






