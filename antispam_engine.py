# !python

import win32com.client
import load_mail
import body_check
import internet_header_check
#import attachment_check
#import sending_mails


#Ucitavanje mejla
message = load_mail.load()
#print(message)


#Izdvajanje tela mejla iz mejla i provera s nb algoritmom
body = message.Body
checked_body = body_check.predictions(body)
#print(checked_body)


#Izdvananje internet header-a i provera s blacklistama
internet_header = message.PropertyAccessor.GetProperty("http://schemas.microsoft.com/mapi/proptag/0x007D001F")
checked_internet_header = internet_header_check.find_ips(internet_header)
#print(checked_internet_header)


"""
#Izdvanje priloga i AV provera
attachments = message.Attackments
checked_attachments = attachment_check.check(attachments)


#Odredjivanje da li je mejl spam



#Slanje poruke obavestenja korisniku i administratoru
"""




#Zadaci
"""
Smisli nacin da kad stigne mejl, ona pokrene skriptu ili da
kreira neki dogadjaj koji se pokrenuti skriptu; i tako svaki novi
pristigli mejl
"""
