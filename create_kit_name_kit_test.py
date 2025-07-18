import data
import configuration
import sender_stand_request

def positive_assert(kit_name):
    kit_response = sender_stand_request.create_kit(kit_name)
    print(kit_response.json())
    assert kit_response.status_code == 201
    assert kit_response.json().get("name") == kit_name

def test_create_kit_name_kit():
    kit_name = "a"
    print(kit_name)
    positive_assert(kit_name)

def test_create_kit_name_kit_511_characters():
    kit_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    print(kit_name)
    positive_assert(kit_name)

def test_create_kit_name_kit_special_characters():
    kit_name = "№%@"
    print(kit_name)
    positive_assert(kit_name)

def test_create_kit_name_with_spaces():
    kit_name = "A Aaa"
    print(kit_name)
    positive_assert(kit_name)

def test_create_kit_name_with_numbers():
    kit_name = "123"
    print(kit_name)
    positive_assert(kit_name)

def negative_assert(kit_name):
    kit_response = sender_stand_request.create_kit(kit_name)
    print(kit_response.json())
    assert kit_response.status_code == 400
    assert kit_response.json().get("name") == kit_name

def test_create_kit_name_kit_0_characters():
    kit_name = ""
    print(kit_name)
    negative_assert(kit_name)

def test_create_kit_name_kit_512_characters():
    kit_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    print(kit_name)
    negative_assert(kit_name)

def negative_assert_id(name_copy):
    kit_response = sender_stand_request.create_kit_with_id(name_copy)
    print(kit_response.json())
    assert kit_response.status_code == 400
    assert kit_response.json().get("message") == "No se han aprobado todos los parámetros requeridos"

def test_create_kit_with_id_no_params():
    name_copy = {}
    print(name_copy)
    negative_assert_id(name_copy)


def test_create_kit_with_id_different_params_numbers():
    name_copy = {"name": 123}
    print(name_copy)
    negative_assert_id(name_copy)










