import signnow_python_sdk

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_ID",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"

    # Create access_token for the user
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')