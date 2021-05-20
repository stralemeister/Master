import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

def load():
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    index = len(messages)
    mail = index-1
    message = messages[mail]
    return message
    #print(message)
