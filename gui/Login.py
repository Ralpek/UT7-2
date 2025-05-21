class Login:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self._leer_configuracion()

    def _leer_configuracion(self):
        config = {}
        with open(self.config_file, 'r', encoding='utf-8') as f:
            for linea in f:
                if ':' in linea:
                    clave, valor = linea.strip().split(':', 1)
                    config[clave] = valor
        return config

    def autenticar(self):
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        return self.config.get(usuario) == contrasena

    def autenticar_manual(self, usuario, contrasena):
        return self.config.get(usuario) == contrasena

    def get_config_db(self):
        return {
            'db_host': self.config.get('db_host', '127.0.0.1'),
            'db_user': self.config.get('db_user', 'root'),
            'db_password': self.config.get('db_password', ''),
            'db_name': self.config.get('db_name', 'daw_prog')
        }

