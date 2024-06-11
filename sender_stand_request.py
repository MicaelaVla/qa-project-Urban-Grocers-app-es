import configuration
import data
import requests

#Este código crea un nuevo usuario para Urban Grocers app:
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


#Este código obtiene el AuthToken del usuario:
def get_new_user_token ():
    response_post_new_user = post_new_user(data.user_body)
    response_post_new_user_json = response_post_new_user.json()
    auth_token = response_post_new_user_json["authToken"]
    return auth_token

#Este código obtiene un nuevo kit para el usuario
def post_new_client_kit(name, auth_token):
    auth_token = get_new_user_token()
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=name,
                         headers= {"Content-Type": "application/json",
                                   "Authorization": "Bearer {auth_token}"}
                         )
    return response


















