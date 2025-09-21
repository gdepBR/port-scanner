# |---------Meu 1°GITHUB--------------------------------------------------------------------------------|

#          CRIADOR: gdepBR    DIA: 21/09/25

#1- use apenas em ambientes autorizados (seu pc ou VM).

#2- não use isso em redes públicas(eles vão te achar kk).

#3- ser tiver errors, ok, é só eu ir melhorando e aprendendo mais sobre scans.

#4-NÃO! EM IPÓTESE NENHUMA, UTILIZE ESSE SCAN PRA PREJUDICAR PESSOAS(TÚ VAI SE FERRAR SE FAZER ISSO).

# |-----------------------------------------------------------------------------------------------------|


import socket, threading # "bibliotecas", usamos elas para usar comandos expecíficos (REDE ou Threding).

ip = "127.0.0.1" # <--- colooque o seu ip alvo aqui.

TIMEOUT = 1 # tempo de espera entre portas.

#|=================Portas==================|

porta_open = []
porta = [21,22,23,53,80,443]

#|=========================================|



#|===============Tentativas================|

tentativas = []
travar = threading.Lock()

#==========================================|


def scan(p): # sempre usar o "p" para se referir ao loop de portas dos threads, nunca o "porta"(confunde com a tabela).

    try:

        cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM); cliente.settimeout(TIMEOUT)
        resultado = cliente.connect_ex((ip, p))

        if resultado == 0: # deu certo.

            with travar: # # trava as tentativas, escaneia a porta e depois abre a "fechadura" pra continuar os outros scans.
                print (f"{p} -> open")
                porta_open.append(p)

    finally: # ecerra conexão com esse cliente (você).
        
        cliente.close() 

for p in porta: # para cada porta scaneada dentro da tabela das portas("p")...

    t = threading.Thread(target=scan, args=(p,)) # importa a biblioteca do threds + permite criar minhas tentativas.
    t.start() # começa o scan nas portas.
    tentativas.append(t) # a tabela tentativas recebetentativas ("t").

for t in tentativas: # apar cada tentativa dentro do loop...

    t.join() # scaneia a porta e faz as outras tentativas esperarem o resultado da 1°. depois continua...

print ("|------Scan-Terminado------|")
print (f" portas scaneadas: {len(porta_open)}")
print (" abertas:", sorted(porta_open))
