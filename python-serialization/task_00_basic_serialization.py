import pickle


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "w") as file:
        return pickle.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        return pickle.load(file)