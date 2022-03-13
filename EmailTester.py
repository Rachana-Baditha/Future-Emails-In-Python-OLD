import smtplib
from datetime import date
import json

MailFile = "GlobalEmailInfo.json"

def sendEmail(sub,mssg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        email = "rachanaroxx10@gmail.com"
        password = "ijrwcrqamfsrlwpn"
        
        smtp.login(email,password)
        
        subject = sub
        body = mssg

        message = f"Subject:{subject}\n\n{body}"

        smtp.sendmail(email, email, message)

def sendToday(dt):
    if( str(date.today()) == dt):
        return True
    return False

def getEmailData():
    #Open json file and deserialize email data
    with open(MailFile, "r") as gmi:
        emaildata = json.load(gmi)
    
    return emaildata

def updateEmailData(emaildata):
    #Write updated data to json file
    with open(MailFile,"w") as gmi:
        json.dump(emaildata,gmi)



def main():

    #Get data from JSON file
    emaildata = getEmailData()

    deliverydate = emaildata["DateOfDelivery"]

    #Check if email should be delivered today
    if sendToday(deliverydate):

        Sno = emaildata["SerialNo"]
        subj = f"A Message From the Past #{Sno}"
        mssg = emaildata["Message"]

        #Send Email
        sendEmail(subj,mssg)

        #Increment total number of mails
        emaildata["SerialNo"] +=1

        #Update data in JSON file
        updateEmailData(emaildata)
        pass

if __name__ == "__main__":
    main()