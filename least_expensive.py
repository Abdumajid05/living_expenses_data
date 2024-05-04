import json
import get_data
def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    pass

    a=list((get_data.get_data(file_path)).values())
    b=list((get_data.get_data(file_path)).keys())
    k=min(a)
    x=a.index(k)
    return b[x]
print(least_expensive(('data.json')))