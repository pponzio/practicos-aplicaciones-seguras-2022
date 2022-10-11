import os


def safe_path(path):
    """Verifica que path es una ruta segura. Si no lo es lanza ValueError.
    Si es segura, retorna la ruta absoluta normalizada.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_filepath = os.path.join(base_dir, path)
    filepath = os.path.normpath(abs_filepath)
    if base_dir != os.path.commonpath([base_dir, filepath]):
        raise ValueError
    return filepath
