import os
import json


BASE_DIR = 'data'
NAME_OF_MAPPING = 'map.json'
MAP_PATH = os.path.join(BASE_DIR, NAME_OF_MAPPING)


def get_mapping() -> dict:
    if not os.path.exists(MAP_PATH):
        with open(MAP_PATH, 'w', encoding='utf-8') as f:
            json.dump({}, f)
        return {}

    with open(MAP_PATH, "r", encoding='utf-8') as read_file:
        return json.load(read_file)


def add_to_map(data: dict) -> int:
    count_users = len(get_mapping().keys())
    current_map = get_mapping()
    current_map.update({count_users: data})

    try:
        with open(MAP_PATH, "w", encoding='UTF-8') as write_file:
            json.dump(current_map, write_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)

    return count_users


def create_new_user(data: dict):
    if data['user_type'] == 'Добавить ребенка':
        data['user_type'] = 'child'
    else:
        data['user_type'] = 'employee'

    data['timetable'] = []

    add_to_map(data)


def get_firs_user_by_type(user_type: str) -> dict:
    all_map = get_mapping()

    for num in all_map.keys():
        if all_map[num]['user_type'] == user_type:
            return all_map[num]

    return {}


def get_all_users_by_type(user_type: str) -> list:
    all_map = get_mapping()
    users = []

    for num in all_map.keys():
        if all_map[num]['user_type'] == user_type:
            temp_dict = all_map[num]
            temp_dict['num'] = num
            users.append(temp_dict)

    return users
