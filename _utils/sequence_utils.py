def find_in_list(search_string: str, key: str, list_to_search: list) -> int:
    i = -1
    count = 0
    for item in list_to_search:
        if item[key] == search_string:
            i = count
        count += 1
    return i
