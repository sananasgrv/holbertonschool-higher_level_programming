#!/usr/bin/python3
"""Doc"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student
    def display(self):
        print(f"Name: {self.name}",
              f"Age: {self.age}",
              f"is_student: {self.is_student}")
    def  serialize(self, filename):
        with open(filename, "wb") as file:
            return pickle.dumps(self.__dict__)
    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)