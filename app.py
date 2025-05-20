from gui.MenuPrincipal import MenuPrincipal
from gui.login import Login

def main():
    while True:
        login = Login("config.txt")
        if login.autenticar():
            print("Login correcto. Bienvenido.")
            MenuPrincipal().mostrar()
            break
        else:
            opcion = input("Login fallido. Intente de nuevo o escriba 'salir' para salir: ")
            if opcion.strip().lower() == 'salir':
                print("Saliendo...")
                break

if __name__ == "__main__":
    main()
