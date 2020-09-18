from twilio.rest import Client 
 
account_sid = 'AC2151c851860c56a0ba31f4639ee0d80c' 
auth_token = '6fce80e55349998b98c2c494018d2887' 
client = Client(account_sid, auth_token) 

def automessaging(): 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Good Morning',      
                              to='whatsapp:+917699322761' 
                          ) 
 
    print(message.sid)