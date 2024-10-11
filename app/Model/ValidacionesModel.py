from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRegExp

class Validaciones:
    def __init__(self):
        self.REGEX_TEXT = QRegExp("[a-zA-ZñÑ ]+")
        self.REGEX_CURP = QRegExp("[A-ZÑ0-9]{18}")
        self.REGEX_RFC = QRegExp("[A-ZÑ0-9]{13}")
        self.REGEX_EMAIL = QRegExp("[a-zA-Z0-9._%+-]+@[a-zA-ZñÑ0-9.-]+\\.[a-zA-Z]{2,4}")
        self.REGEX_NSS = QRegExp("[0-9]{11}")
        self.REGEX_PHONE = QRegExp("[0-9]{10}")
        self.REGEX_PASSWORD = QRegExp("^[a-zA-ZñÑ0-9!@#$%^&*()\\-+=\\{\\}\\[\\]:;\"'<>,.?/|~`]{1,25}$")
        self.REGEX_WEB = QRegExp("^(https?://)?(www\\.)?([a-zA-Z0-9-]+(\\.[a-zA-Z]{2,})+)(/[^\\s]*)?$")
        self.VALIDATOR_INT = QIntValidator(0, 99999)
    @property
    def get_text_validator(self):
        return QRegExpValidator(self.REGEX_TEXT)
    @property
    def get_curp_validator(self):
        return QRegExpValidator(self.REGEX_CURP)
    @property
    def get_rfc_validator(self):
        return QRegExpValidator(self.REGEX_RFC)
    @property
    def get_email_validator(self):
        return QRegExpValidator(self.REGEX_EMAIL)
    @property
    def get_nss_validator(self):
        return QRegExpValidator(self.REGEX_NSS)
    @property
    def get_phone_validator(self):
        return QRegExpValidator(self.REGEX_PHONE)
    @property
    def get_int_validator(self):
        return self.VALIDATOR_INT
    @property
    def get_password_validator(self):
        return QRegExpValidator(self.REGEX_PASSWORD)
    @property
    def get_web_validator(self):
        return QRegExpValidator(self.REGEX_WEB)
