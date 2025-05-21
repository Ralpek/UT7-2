from gui.Login import Login
from gui.MenuPrincipal import MenuPrincipal

def main():
    login = Login("config.txt")

    while True:
        print("\n--- Inicio de sesión ---")
        if login.autenticar():
            print("Login exitoso.")
            config = login.get_config_db()
            MenuPrincipal(config).mostrar()
            break
        else:
            opcion = input("Credenciales incorrectas. Intente de nuevo o escriba 'salir': ").strip().lower()
            if opcion == 'salir':
                print("Saliendo del sistema...")
                break

if __name__ == "__main__":
    main()

