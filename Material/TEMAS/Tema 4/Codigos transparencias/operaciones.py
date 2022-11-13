def division(x, y, output): 
    cociente = x // y 
    resto = x % y
    output[0] = cociente; output[1] = resto
    
def intercambia(inoutput):
    aux = inoutput[0]
    inoutput[0] = inoutput[1]
    inoutput[1] = aux 
        