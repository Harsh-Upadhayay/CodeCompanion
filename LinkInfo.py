import LOCAL_VARS
import sys

class Link :

    def __init__(self, file=LOCAL_VARS.SOURCE_CODE_PATH):    
        
        try : 
            f = open(file, "r")
        except Exception as e :
            sys.exit("\t\t!! Source File not found, check path in LOCAL_VARS !!\n", e)
        
        self.link = f.readline()[2 : -3]
        self.link = self.link.strip()

        if self.link.count("codeforces.com") == 1:
            self.site = "cf"
        elif self.link.count("codechef.com") == 1:
            self.site = 'cc'
        else :
            self.link = "https://codeforces.com/problemset/problem/1702/C"
            print("\t\t !! Problem link not added, add the link in the first line of the source code !!\n") 

l = Link()
