import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print("\nA conexão falhou!")
        print("\nErro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso!")

    HostAlvo = input("Digite o Host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + "e na Porta: " + PortaAlvo)
        s.shutdown(2)

    except socket.error as e:
         print("\nNão foi possivel conectar no Host: " + HostAlvo + "- e na Porta: " + PortaAlvo)
         print("\nError: {}".format(e))
         sys.exit()


if __name__ == "__main__":
    main()
