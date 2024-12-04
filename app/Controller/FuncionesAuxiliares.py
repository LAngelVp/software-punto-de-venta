import unicodedata, os
def quitar_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def size_validator_image(image):
        if image:
            file_size = os.path.getsize(image)
            if file_size > 1024 * 1024 * 5:
                return False
            else:
                return True
        return False