from src.common.flatten_array import flatten_array


def camel_to_underscore(camel: str) -> str:
    nested_list = [['_', x.lower()] if x.upper() == x else [x] for x in camel]
    flattened_list = flatten_array(nested_list)
    joined = "".join(flattened_list)
    return joined[1:]
