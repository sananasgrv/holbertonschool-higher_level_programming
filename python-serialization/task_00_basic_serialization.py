import pickle


def serialize_and_save_to_file(data, filename):
    try:
        with open(filename, "wb") as file:
            return pickle.dump(data, file)
    except Exception as e:
        raise TypeError("Object is not serializable") from e


def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
