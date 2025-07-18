import random

headers_create_user = {
    "Content-Type": "application/json"
}

headers_create_kit = {
    "Content-Type": "application/json",
    "Authorization": "",
}

user_body = {
    "firstName": "Camila",
    "phone": "+529983852117",
    "address": "Kusamil",
    "email": "camsmalo@outlook.com",
    "comment": "Hola mundo",
}

create_kit_body = {
    "name": "Mi kit",
    "cardId": random.randint(1, 100),

}
