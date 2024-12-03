from gradanator import *
from grades import *

def main():
    banner()
    
    generalresult = notasestudiante()
    
    nombreestudiante,examen1resultado,examen2resutlado,examenfinalresultado,result = generalresult
    
    notafinal = round(examen1resultado,1) + round(examen2resutlado,1) + round(examenfinalresultado,1) + round(result,1)
    if notafinal > 100:
        notafinal = 100

    notas(notafinal)
    
    
 
    
main()