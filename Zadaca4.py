import re

mail = "(^[a-z]+)[.]([a-z]+)([@]fpmoz[.]sum[.]ba$)"

while 1:
           mail_1 = input("Unesi mail: ")
           jednako = re.match(mail, mail_1)
           if jednako:
                      print("Uspješno ste unijeli vašu e-mail adresu!")
                      grupe = jednako.groups()
                      break
           else:
                      print("Ne'ispravno, pokušajte ponovo!")
psi = grupe[0][0]
p = grupe[1]
eduid_pattern = "^"+psi+p+"(\d*@sum.ba$)"
while 1:
           eduid = input("Unesi eduid: ")
           match = re.match(eduid_pattern, eduid)
           if match:
                      print("Uspješno ste unijeli vaš eduid!")
                      break
           else:
                      print("Ne'ispravno, pokušajte ponovo!")




