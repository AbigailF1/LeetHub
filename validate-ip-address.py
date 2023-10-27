class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ltr = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B' ,'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7' , '8', '9']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7' , '8', '9']
        x = []
        if "." in queryIP:
            x = queryIP.split('.')
        if ":" in queryIP:
            x = queryIP.split(':')
        # print(x)
        if len(x) != 4 and len(x) != 8:
            return "Neither"
        elif len(x) == 4:
            for i in range(4):
                for j in range(len(x[i])):
                    if x[i][j] not in nums:
                        return "Neither"
                if x[i] == "" or  len(str(int(x[i]))) != len(x[i]) or 0 > int(x[i]) or  int(x[i]) >= 256:
                    return "Neither"
            return "IPv4"
        else:
            for i in range(8):
                if len(x[i]) > 4 or x[i] == "": return "Neither"
                for j in range(len(x[i])):
                    if x[i][j] not in ltr:
                        return "Neither"
            return "IPv6"
        
        return "Neither"