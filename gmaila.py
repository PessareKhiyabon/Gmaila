import smtplib
import colorama

colorama.init()

def checker(rcpt) :
    gmail = smtplib.SMTP("gmail-smtp-in.l.google.com" , 25)
    try:
        gmail.sendmail("mrpythonblog@gmail.com" , rcpt , "nothing")
    except smtplib.SMTPRecipientsRefused:
        return False
    except smtplib.SMTPDataError:
        return True

print("""[+]Gmaila v1.1 [+]""")
creators = colorama.Fore.BLUE+"Created By Pessare Khiyabon"
print(creators)
gmaillist = input("Enter Gmail Addres > ")
#gmaillist = open(gmaillist)

for gmail in gmaillist:
    gmail = gmaillist #gmail.strip("\n")
    if checker(gmail):
        print(colorama.Fore.GREEN + "[+] {} is Correct ! [+]".format(gmail))
        exit()

    else:
        print(colorama.Fore.RED + "[-] {} is InCorrect ! [-]".format(gmail))
        exit()

input()
