import signnow_python_sdk

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_SECRET",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"
    document_id = "DOCUMENT_ID"

    # Create access_token for the user
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')

    # Create the signing links for a document.
    signing_link = signnow_python_sdk.Link.create(access_token['access_token'], document_id)

    # Embed signing link to your website or share directly
    '''
    <iframe
      src = 'https://signnow.com/s/ttKssERL?form=true' > 
    </ iframe >
    
    '''