import data
import sender_stand_request


# Pruebas:

# PRUEBA 1: Creación del kit con el número minimo permitido de caracteres (1)

def test_create_kit_1_letter_in_name_get_success_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_1"],auth_token)
    kit_response_json = kit_response.json()
# comprueba que la respuesta sea código 201
    assert kit_response.status_code == 201
# comprueba que el campo "name" del cuerpo de la respuesta coincide con del campo "name" de la solicitud
    assert kit_response_json["name"] == data.kit_body["test_1"]["name"]




#PRUEBA 2: Creación del kit con el número máximo permitido de caracteres (511)

def test_create_kit_511_letter_in_name_get_success_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_2"],auth_token)
    kit_response_json = kit_response.json()
    assert kit_response.status_code == 201 #comprueba que la respuesta sea código 201
    assert kit_response_json["name"] == data.kit_body["test_2"]["name"] #comprueba que el campo "name" del cuerpo de
                                                                            # la respuesta coincide con del campo "name"
                                                                            # de la solicitud

# PRUEBA 3: Creación del kit con el número de caracteres menor que la cantidad permitida (0):

def test_create_kit_0_letter_in_name_get_negative_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_3"],auth_token)
    assert kit_response.status_code == 400  # comprueba que la respuesta sea código 400


# PRUEBA 4: Creación del kit con número de caracteres mayor que la cantidad permitida (512):

def test_create_kit_512_letter_in_name_get_negative_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_4"],auth_token)
    assert kit_response.status_code == 400  # comprueba que la respuesta sea código 400


#PRUEBA 5: Creación de un kit con caracteres especiales:

def test_create_kit_special_character_in_name_get_success_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_5"],auth_token)
    kit_response_json = kit_response.json()
    assert kit_response.status_code == 201  # comprueba que la respuesta sea código 201
    assert kit_response_json["name"] == data.kit_body["test_5"]["name"]  # comprueba que el campo "name" del cuerpo de
    # la respuesta coincide con del campo "name"
    # de la solicitud


#PRUEBA 6: Creación de un kit con un espacio en el nombre:

def test_create_kit_space_in_name_get_success_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_6"],auth_token)
    kit_response_json = kit_response.json()
    assert kit_response.status_code == 201  # comprueba que la respuesta sea código 201
    assert kit_response_json["name"] == data.kit_body["test_6"]["name"]  # comprueba que el campo "name" del cuerpo de
                                                                         # la respuesta coincide con del campo "name"
                                                                         # de la solicitud


#PRUEBA 7: Creación de un kit con números en el nombre:

def test_create_kit_number_in_name_get_success_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_7"],auth_token)
    kit_response_json = kit_response.json()
    assert kit_response.status_code == 201  # comprueba que la respuesta sea código 201
    assert kit_response_json["name"] == data.kit_body["test_7"]["name"]  # comprueba que el campo "name" del cuerpo de
                                                                         # la respuesta coincide con del campo "name"
                                                                         # de la solicitud

#PRUEBA 8: Creación de un kit cuando el parámetro no se pasa en la solicitud:

def test_create_kit_no_parameter_in_name_get_unsuccess_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_8"],auth_token)
    assert kit_response.status_code == 400  # comprueba que la respuesta sea código 400


# PRUEBA 9: Creación de un kit cuando se ha pasado un tipo de parámetro diferente (número):


def test_create_kit_different_type_parameter_in_name_get_unsuccess_response():
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body["test_9"],auth_token)
    assert kit_response.status_code == 400  # comprueba que la respuesta sea código 400



