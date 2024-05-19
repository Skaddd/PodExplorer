import json


def save_json(dict_to_save: dict, saving_path: str) -> None:
    with open(saving_path, "w") as json_result:
        json_result.dump(dict_to_save)


def load_json(saving_path: str) -> dict:
    with open(saving_path, "r") as json_batch_result:
        result_dict = json.load(json_batch_result)
    return result_dict
