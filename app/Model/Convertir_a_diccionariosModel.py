
from sqlalchemy.orm import class_mapper, ColumnProperty, RelationshipProperty
from datetime import date, datetime

def model_to_dict(obj, deep=False, exclude=None):
    """
    Convierte una instancia de un modelo SQLAlchemy en un diccionario.
    
    Args:
        obj: Instancia del modelo SQLAlchemy.
        deep (bool): Si es True, serializa relaciones también.
        exclude (list): Lista de campos a excluir.
        
    Returns:
        dict: Diccionario con los datos del modelo.
    """
    if exclude is None:
        exclude = []

    data = {}
    for prop in class_mapper(obj.__class__).iterate_properties:
        if isinstance(prop, ColumnProperty):
            key = prop.key
            if key in exclude:
                continue

            value = getattr(obj, key)
            # Convertir fechas a string para evitar errores
            if isinstance(value, (date, datetime)):
                value = value.isoformat()
            data[key] = value

        elif deep and isinstance(prop, RelationshipProperty):
            key = prop.key
            if key in exclude:
                continue

            related_value = getattr(obj, key)

            if related_value is None:
                data[key] = None
            elif isinstance(related_value, list):
                # Lista de objetos relacionados
                data[key] = [model_to_dict(item, deep=False) for item in related_value]
            else:
                # Un solo objeto relacionado
                data[key] = model_to_dict(related_value, deep=False)
    return data

