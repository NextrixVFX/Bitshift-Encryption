class BitshiftEncryption:
    def __init__(self, shift: int, input: str) -> None:
        self.shift: int = shift
        self.input: str = input

    def Encrypt(self) -> str:
        encrypted: str = ""
        for i in self.input:
            # Shift each char's unicode value {shift} amnt of bits left
            u: int = ord(i) << abs(self.shift) % 14
            # Append the char to a string
            encrypted += chr(u)
        return encrypted
    
    def Decrypt(self) -> str:
        decrypted: str = ""
        for i in self.input:
            # Shift each char's unicode value {shift} amnt of bits right
            u: int = ord(i) >> abs(self.shift) % 14
            # Append the char to a string
            decrypted += chr(u)
        return decrypted

if __name__ == "__main__":
    shift: int = int(input("Amnt to shift:\t"))
    string: str = input("Input String:\t")

    bitshift: BitshiftEncryption = BitshiftEncryption(shift, string)

    encrypted, decrypted = "", ""

    try:
        encrypted += bitshift.Encrypt()
    except Exception as e:
        encrypted += f"Error: {str(e)}"

    try:
        decrypted += bitshift.Decrypt()
    except Exception as e:
        decrypted += f"Error: {str(e)}"

    print(f"Shifted:\t{abs(shift) % 14}\nEncrypted:\t{encrypted}\nDecrypted:\t{decrypted}")