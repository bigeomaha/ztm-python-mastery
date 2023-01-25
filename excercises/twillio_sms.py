from twilio.rest import Client


auth_token = '[auth token]'
acct_sid = 'AC927dceadd501e3013b36c9bcf08ae683'
mess_srv_id='MGfc2aca966265643a2ceb17a5a672cb37'
to_num = '+14025079169'
msg_body = 'Testing SMS from Python File.'


client = Client(acct_sid, auth_token)
message = client.messages.create(
    to=to_num, body=msg_body, messaging_service_sid=mess_srv_id
)
