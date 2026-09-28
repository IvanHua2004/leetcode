class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        bitPosition = 31
        final = ""
        total = 0
        hexa = ""
        if str(num)[0] == "-":
            total = -(2**bitPosition)
            bitPosition -= 1
            final += "1"
            while bitPosition != -1:
                if total + 2**bitPosition <= num:
                    total += 2**bitPosition
                    final += "1"
                else:
                    final += "0"
                bitPosition -= 1
        else:
            start = False
            while bitPosition != -1:
                if total + 2**bitPosition <= num:
                    if start == False:
                        for _ in range((4-(bitPosition+1)%4)%4):
                            final += "0"
                    total += 2**bitPosition
                    final += "1"
                    start = True
                elif start == True:
                    final += "0"
                bitPosition -= 1
        
        for i in range(0, len(final), 4):
            value = 0
            bitPosition = 3
            for c in final[i:i+4]:
                if c == "1":
                    value += 2**bitPosition
                bitPosition -= 1
            print(value)
            
            match value:
                case 10:
                    hexa += "a"
                case 11:
                    hexa += "b"
                case 12:
                    hexa += "c"
                case 13:
                    hexa += "d"
                case 14:
                    hexa += "e"
                case 15:
                    hexa += "f"
                case _:
                    hexa += str(value)
        return hexa