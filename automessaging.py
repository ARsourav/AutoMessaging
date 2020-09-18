from twilio.rest import Client 
 
account_sid = 'AC2151c851860c56a0ba31f4639ee0d80c' 
auth_token = '09e5429c9307644c2742cc218e7e7ad3' 
client = Client(account_sid, auth_token) 

def automessaging():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hii there',      
                              to='whatsapp:+917699322761' 
                          ) 
 
    print(message.sid)