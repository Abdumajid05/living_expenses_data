import json
import get_data
def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    a=list((get_data.get_data(file_path)).values())
    b=list((get_data.get_data(file_path)).keys())
    k=max(a)
    x=a.index(k)
    return b[x]
print(most_expensive(('data.json')))