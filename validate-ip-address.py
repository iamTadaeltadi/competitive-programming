class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        iPForFour =queryIP.split(".")

        ipForSix = queryIP.split(":")

        print(iPForFour,ipForSix)



        def checkForValidity(string,iPType):
            if iPType =="IPv4":
                if len(string) !=4:
                    return (False,"Neither")
                for i in string:
                    if not i:
                        return  (False,"Neither")
                    if i.isdigit() and not 0<=int(i)<256:
                            
                        return (False,"Neither")
                    if len(i)>1 and i[0]=="0":
                        return (False,"Neither")
                    for j in i:
                        print(j)

                        if j.isdigit() and not 0<=int(j)<256:
                            
                            return (False,"Neither")
                       

                        if not j.isdigit() :
                            return (False,"Neither")
                return (True,"IPv4")
            else:
                if len(string) !=8:
                    return (False,"Neither")

                for i in string:
    
                    if not i:
                        return  (False,"Neither")
                    if len(i)>4:
                        return (False,"Neither")
                    for j in i:
                        
                        if  not  j.isdigit() and not  ('a' <= j <= 'f') and  not ('A' <= j <= 'F'):
                            return (False,"Neither")
                
            
            return (True,"IPv4")
                    




        if checkForValidity(iPForFour,"IPv4")[0]:
                return "IPv4"
        

        
        if checkForValidity(ipForSix,"IPv6")[0]:
            return "IPv6"
        return "Neither"