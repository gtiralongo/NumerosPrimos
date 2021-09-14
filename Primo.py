def esprimo(numero):

    if numero % 2 == 0:        
        if numero == 2:
            print(numero, "ES PRIMO")
            return True 
        cuenta = numero / 2
        print("----------------") 
        print("NO ES PRIMO PORQUE ES DIVISIBLE POR 2 DA ", cuenta)
        return False
    else:
        if numero % 3 == 0:
            if numero == 3:
                print(numero, "ES PRIMO")
                return True
            cuenta = numero / 3
            print("----------------")
            print("NO ES PRIMO PORQUE ES DIVISIBLE POR 3 DA ", cuenta)
            return False
        else:
            if numero % 5 == 0:
                if numero == 5:
                    print(numero, "ES PRIMO")
                    return True
                cuenta = numero / 5
                print("----------------")
                print("NO ES PRIMO PORQUE ES DIVISIBLE POR 5 DA ", cuenta)
                return False
            else:
                if numero % 7 == 0:
                    if numero == 7:
                        print(numero, "ES PRIMO")
                        return True
                    cuenta = numero / 7
                    print("----------------")
                    print("NO ES PRIMO PORQUE ES DIVISIBLE POR 7 DA ", cuenta)
                    return False
                else:
                    if numero % 11 == 0:
                        if numero == 11:
                            print(numero, "ES PRIMO")
                            return True
                        cuenta = numero / 11
                        print("----------------")
                        print("NO ES PRIMO PORQUE ES DIVISIBLE POR 11 DA ", cuenta)
                        return False
    print("----------------")
    print(numero," ES PRIMO")
    if numero == 73:
        print("SEGUN SHELDON EL MEJOR NUMERO PRIMO")
        respuesta = input("¿QUERES SABER PORQUE? S/N: ").upper()
        if respuesta == 'N':
            print("VOS TE LO PERDES...")
        else:
            print("PORQUE ES EL UNICO QUE CUMPLE LAS SIGUIENTES PROPIEDADES:")
            print("----------------")
            propiedades = (" El 73 es el 21º número primo, \n leído al revés es el 37 que es el \n 12º número primo que leído al revés es \n 21 que es el resultado de multiplicar 7 × 3; \n y en sistema binario 73 es 1001001, \n un numeral capicúa(palindromo), \n que posee siete (7) cifras de las cuales tres (3) son unos. \n En sistema octal 73 es 111 el cual es un capicúa.").upper()        
            print(propiedades)
    return True

def main():

    print("¿EL NUMERO ES PRIMIMO?")
    numero = int(input("INGRESE EL NUMERO: "))
    esprimo(numero)

main()