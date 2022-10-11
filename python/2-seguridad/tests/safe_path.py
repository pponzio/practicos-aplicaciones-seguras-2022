import os


def safe_path(path):
    """Verifica que path es una ruta segura. Si no lo es lanza ValueError.
    Si es segura, retorna la ruta absoluta normalizada.
    """
    if path.startswith('/') or path.startswith('..'):
        raise ValueError
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_filepath = os.path.join(base_dir, path)
    norm_abs_filepath = os.path.normpath(abs_filepath)
    return norm_abs_filepath


