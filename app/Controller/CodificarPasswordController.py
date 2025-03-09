import bcrypt

class EncriptarPasswordConrtoller:
    def __init__(self, contraseña):
        self.contraseña = contraseña
    def hashear_password(self):
        self.contraseña_encriptada = bcrypt.hashpw(self.contraseña.encode(), bcrypt.gensalt())
        return self.contraseña_encriptada