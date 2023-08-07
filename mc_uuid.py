from hashlib import shake_128


class UUID:
    """用于生成一个MC的UUID，并以多种方式表示"""

    def __init__(self, uuid: str) -> None:
        """通过一个32位的十六进制数(有无连字符均可)来指定UUID。"""
        uuid = uuid.replace("-", "")
        self.uuid = uuid

    def hyp_hex(self):
        """
        UUID的一种十六进制表示方式，中间用连字符将其划分为几个部分。通常的一种划分格式
        是将UUID分成8-4-4-4-12格式的数字，其中每个数字代表对应区间内的十六进制字符个数。
        """
        return f"{self.uuid[0:8]}-{self.uuid[8:12]}-{self.uuid[12:16]}-{self.uuid[16:20]}-{self.uuid[20:32]}"

    def hex(self):
        """和有连字符的十六进制表示方法相同，只是每个部分之间没有连字符用来分隔。"""
        return self.uuid

    def int_array(self):
        """用4个32位数字表示。每一部分存储在由高到低的整型数组中。"""
        array = [
            int.from_bytes(bytes.fromhex(self.uuid[i : i + 8]), "big", signed=True)
            for i in range(0, 32, 8)
        ]
        return array
    
    def __str__(self) -> str:
        array = self.int_array()
        return f"[I;{','.join(map(str, array))}]"
    
    def __repr__(self) -> str:
        return f"UUID(\"{self.uuid}\")"


def generate_uuid(data:bytes):
    """从任意的文件对象生成一个UUID"""
    return UUID(shake_128(data).hexdigest(16))