from PySide6.QtGui import QRegularExpressionValidator, QIntValidator, QDoubleValidator
from PySide6.QtCore import QRegularExpression

class Validaciones:
    def __init__(self):
        self.REGEX_TEXT = QRegularExpression("^[a-zA-ZñÑ ]+$")
        self.REGEX_CURP = QRegularExpression("[A-ZÑ0-9]+")
        self.REGEX_RFC = QRegularExpression("[A-ZÑ0-9]+")
        self.REGEX_EMAIL = QRegularExpression(r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)")
        self.REGEX_NSS = QRegularExpression("[0-9]+")
        self.REGEX_PHONE = QRegularExpression("[0-9]+")
        self.REGEX_PASSWORD = QRegularExpression("^[a-zA-ZñÑ0-9!@#$%^&*()\\-+=\\{\\}\\[\\]:;\"'<>,.?/|~`]+$")
        self.REGEX_WEB = QRegularExpression("^(https?://)?(www\\.)?([a-zA-Z0-9-]+(\\.[a-zA-Z]{2,})+)(/[^\\s]*)?$")
        self.VALIDATOR_INT = QRegularExpression("^[0-9]+")
    @property
    def get_text_validator(self):
        return QRegularExpressionValidator(self.REGEX_TEXT)
    @property
    def get_curp_validator(self):
        return QRegularExpressionValidator(self.REGEX_CURP)
    @property
    def get_rfc_validator(self):
        return QRegularExpressionValidator(self.REGEX_RFC)
    @property
    def get_email_validator(self):
        return QRegularExpressionValidator(self.REGEX_EMAIL)
    @property
    def get_nss_validator(self):
        return QRegularExpressionValidator(self.REGEX_NSS)
    @property
    def get_phone_validator(self):
        return QRegularExpressionValidator(self.REGEX_PHONE)
    @property
    def get_int_validator(self):
        return QRegularExpressionValidator(self.VALIDATOR_INT)
    @property
    def get_password_validator(self):
        return QRegularExpressionValidator(self.REGEX_PASSWORD)
    @property
    def get_web_validator(self):
        return QRegularExpressionValidator(self.REGEX_WEB)
