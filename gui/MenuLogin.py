from configuracion import Usuario

class MenuLogin:
    def main(self):
        print("=== LOGIN ===")
        while True:
            user = input("Usuario: ")
            if user.lower() == "salir":
                print("Saliendo...")
                return None
            password = input("Contraseña: ")
            if user == Usuario.User and password == Usuario.Password:
                print("Acceso concedido.")
                return None
            else:
                print("Credenciales incorrectas. Intente de nuevo o escriba 'salir'.")
