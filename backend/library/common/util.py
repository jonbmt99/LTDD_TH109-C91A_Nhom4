from flask import jsonify


def ConvertModelListToDictList(model_list):
    dict_items = []
    # model_list=filter(lambda model_item: model_item.delete_at is None, model_list)
    for item in model_list:
        # if item.delete_at is None:
        dict_items.append(item.serialize())
    return dict_items


def ConvertModelListToJson(model_list):
    return jsonify(list(map(lambda item: item.serialize(), model_list)))

