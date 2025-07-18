import configuration
import requests
import data
import random

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers_create_user)  # inserta los encabezados

def post_new_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=data.headers_create_kit)

def create_user_auth_token(firstName="Camila"):
    current_body = data.user_body.copy()
    current_body["firstName"] = firstName
    user = post_new_user(current_body)
    return user.json()["authToken"]

def create_kit(name="Sin nombre"):
    body = data.create_kit_body.copy()
    body["name"] = name
    body["cardId"] = random.randint(1, 1000)
    kit_response = post_new_kit(body)
    return kit_response

def create_kit_with_id(id_body={}):
    name_copy = data.create_kit_body.copy()
    name_copy["name"] = "name_here"
    name_copy["cardId"] = random.randint(1, 1000)
    kit_response = post_new_kit(id_body)
    return kit_response
