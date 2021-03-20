import signnow_python_sdk
import json

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_ID",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"

    # Create access_token for the user
    print ("Creating access token:")
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')
    print (username + "'s access token: " + access_token['access_token'])
    print ("The access token's scope: " + access_token['scope'])
    print ("\n")

    # Get the users root folder
    print ("Getting users root folder:")
    root_folder = signnow_python_sdk.Folder.root_folder(access_token['access_token'])
    print ('Folder name:', root_folder['name'])
    print ('Folder id:', root_folder['id'])
    print ('Number of documents in the folder:', root_folder['total_documents'])
    print ("\n")

    # Get the documents folder with its first 50 documents, that are signed, and in descending order by created date.
    print ("Getting \"Documents\" folder:")
    documents_folder_id = [document for document in root_folder['folders'] if document['name'] == 'Documents'][0]['id']
    filter_object= {
        "filters": "signing-status",
        "filter-values": "signed"
    }
    sort_object = {
        "sortby": "created",
        "order": "desc"
    }
    documents_folder = signnow_python_sdk.Folder.get(access_token['access_token'], documents_folder_id, 50, 0,
                                                     filter_object, sort_object)
    print ('Folder name:', documents_folder['name'])
    print ('Folder id:', documents_folder['id'])
    print ('Total documents that meet criteria:', documents_folder['total_documents'])
    print ('Number of documents returned:', len(documents_folder['documents']))
    print ("\n")

    # Obtain all documents from Documents folder in groups of 20
    print ("Getting all documents in \"Documents\" folder:")
    offset = 0
    documents_folder = signnow_python_sdk.Folder.get(access_token['access_token'], documents_folder_id, 20, offset)
    print ('Folder name:', documents_folder['name'])
    total_documents = documents_folder['total_documents']
    print ('Total number of documents:', total_documents)
    documents_list = documents_folder['documents']
    while len(documents_list) < total_documents:
        offset += 20
        documents_folder = signnow_python_sdk.Folder.get(access_token['access_token'], documents_folder_id, 20, offset)
        documents_list.extend(documents_folder['documents'])
    print ("The number of documents in my compiled list is equal to total documents:", len(documents_list) == total_documents)
