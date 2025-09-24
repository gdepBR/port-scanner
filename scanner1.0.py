#||==============BIBLIOTÉCAS===============||
import socket, threading, ipaddress, sys
#||========================================||

#||=================CORES==================||
VERDE = "\033[32m" # deu certo.
VERMELHO ="\033[31m" # deu errado.
RESET = "\033[0m" # volta a cor padrão do terminal.
#||========================================||



#||================PORTAS==================||
portas_open = []
portas = [21,22,23,25,53,80,110,443,]
#||========================================||



#||===============TENTATIVAS===============||
tentativas = []
parar = threading.Lock()
TIMEOUT = 1
#||========================================||

def scan(port): # criar o inpuit do ip no final no código!!

    cliente = None # recebe o valor durante o scan.

    try:
        cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM); cliente.settimeout(TIMEOUT)
        resultado = cliente.connect_ex((ip, port))

        if resultado == 0: # porta aberta/aceitando conexão.

            with parar: # permite apenas 1 conexão por porta.
                print(f"{VERDE}{port} -> open{RESET}")
                portas_open.append(port)

    except socket.error as error_connect: # errors de socket.

        with parar:

            print(f"{VERMELHO}{port} error de conexão. {error_connect}{VERMELHO}")

    except Exception as error_geral: # error gerais.

        with parar: 

            print(f"{VERMELHO}error inerperado, tente novamente.{error_geral}{RESET}")
    finally:
        if cliente:
            try:
                cliente.close()
            except:
                pass # "pass" = não faz nada, siplesmente ignora(deixa passar).
    

ip = input('digite o ip alvo: ')

try:

    ipaddress.ip_address(ip) # "ip_addreses" = transfoma uma string e um objeto (nesse caso, um ip real).
    print(f"{VERDE}ip válido: {ip}{RESET}")

except ValueError: # "ValueError" = caso a string (texto) não for ip válido, biblioteca lanca um "ValueError".
    print(f"{VERMELHO}ip inválido, tente novamente.{RESET}")
    sys.exit(1) # "sys.exit(1)" força o programa a se encerrar. o "1" significa encerrar imediantamente.

for port in portas:

    tent = threading.Thread(target=scan, args=(port,))
    tent.start()
    tentativas.append(tent)

for tent in tentativas:

    tent.join() # ".join()" = espera uma tentativa terminar antes de continuar os outros scans.

print('||===Scan-Finalzado========================================||')
print(f"portas scaneadas: {len(portas_open)}") # "len" = pecorrer e mostra a lista de "portas_open".
print(f"{VERDE}portas abertas: {RESET}", sorted(portas_open)) # "sorted" organiza por ordem numéria ou alfabética.

    
        

