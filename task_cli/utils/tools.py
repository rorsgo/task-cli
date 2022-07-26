def extract_keys_and_values(dictionary: dict):
    lista = []
    if not bool(dictionary):
        print('Dictionary empty. Finish program.')
        exit(1)
    for key, value in dictionary.items():
        lista.append(key)
        lista.append(value)
    return lista