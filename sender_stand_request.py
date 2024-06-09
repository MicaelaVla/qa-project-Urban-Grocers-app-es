import configuration
import data
import requests

#Este código crea un nuevo usuario para Urban Grocers app:
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response_post_new_user = post_new_user(data.user_body)
response_post_new_user_json = response_post_new_user.json()
print(response_post_new_user_json)

#Este código obtiene el AuthToken del usuario:
def get_new_user_token ():
    return response_post_new_user_json["authToken"]
#Este codigo le asigna la variable auth_token a la función para extraer el valor del mismo.
auth_token = get_new_user_token()
print(auth_token)

#Este código cambia el formato del authtoken extraido para luego pasarlo como headers en la solicitud de creación del kit para el usuario
authorization = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}"
}
print(authorization)

#Este código obtiene un nuevo kit para el usuario
def post_new_client_kit(name):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=name,
                         headers=authorization
                         )


















