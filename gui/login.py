class Login:
    def __init__(self, config_file):
        self.config_file = config_file
        self.credenciales = self._leer_configuracion()

    def _leer_configuracion(self):
        credenciales = {}
        with open(self.config_file, 'r', encoding='utf-8') as f:
            for linea in f:
                if ':' in linea:
                    usuario, clave = linea.strip().split(':', 1)
                    credenciales[usuario] = clave
        return credenciales

    def autenticar(self):
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        return self.credenciales.get(usuario) == contrasena

    def autenticar_manual(self, usuario, contrasena):
        return self.credenciales.get(usuario) == contrasena
