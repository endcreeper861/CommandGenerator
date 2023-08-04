class NBT:
    """Minecraft的NBT标签的类"""

    def __init__(self, **kwargs) -> None:
        """创建一个新的NBT标签"""
        self.dict = kwargs

    def __str__(self) -> str:
        if self.dict == {}:
            return ""
        string = "{"
        for key, item in self.dict.items():
            if type(item) == str:
                string += f'{key}:"{item}",'
            elif type(item) == int or type(item) == float:
                string += f"{key}:{item},"
            elif type(item) == bool:
                if item == True:
                    string += f"{key}:1b,"
                else:
                    string += f"{key}:0b,"
            elif type(item) == list:
                string += f"{key}:"+_list_to_string(item)+","
            elif type(item) == dict:
                string += f"{key}:{NBT(**item)}"
            else:
                string += f"{key}:{item},"
        string = string[:-1] + "}"
        return string
    
def _list_to_string(new_list):
    if new_list == []:
        return "[]"
    string = "["
    for element in new_list: # type: ignore
        if type(element) == dict:
            string += f"{NBT(**element)},"
        elif type(element) == list:
            string += _list_to_string(element)
        elif type(element) == str:
            string += f'"{element}",'
        elif type(element) == int | float:
            string += f"{element},"
        elif type(element) == bool:
            if element == True:
                string += f"1b,"
            else:
                string += f"0b,"
        else:
            string += f"{element},"
    string = string[:-1] + "]"
    return string
