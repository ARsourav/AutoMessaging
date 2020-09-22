from twilio.rest import Client 
 
account_sid = '[ACCOUNT ID]' 
auth_token = '[AUTH TOKEN]' 
client = Client(account_sid, auth_token) 

def automessaging(): 
    message = client.messages.create( 
                              from_='whatsapp:+10123456789',  
                              body='Good Morning',      
                              to='whatsapp:+911234567890' 
                          ) 
 
    print(message.sid)
