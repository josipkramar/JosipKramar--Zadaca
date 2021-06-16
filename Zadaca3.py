import re

txt = input("Unesi string: ")     

pattern = "^s.*[0-5].*\s.*k$"

pattern2 = "\s"

match = re.search(pattern, txt)

match2 = re.search(pattern2, txt)

if match and match2:
           print("Podudaranje!")

else:
           print("Nije pronađeno podudaranje")
            
