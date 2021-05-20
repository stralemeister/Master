import win32com.client
import re
#import ip_rep

def find_ips(internet_header):
    check = internet_header
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    ip = re.findall(re_ip,check)
    #ip_rep.check_ips(ips)
    return ip

    

"""
Popravi regex izraz, prolazi za brojeve koji su verzije!!!

Ostaje jos da se lista IP adresa proveri s blacklistama; za to treba
da preuzmes liste ili ih gadjas preko neta i prodjes sve adrese kroz
liste
"""
