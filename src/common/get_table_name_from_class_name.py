from src.common.camel_to_underscore import camel_to_underscore


def get_table_name_from_class_name(name: str) -> str:
    underscore = camel_to_underscore(name)
    if underscore.endswith('_model'):
        return underscore[:-6]
    return underscore
