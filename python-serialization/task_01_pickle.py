#!/usr/bin/python3
"""Doc"""
import os
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
    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                return pickle.dump(self, file)
        except Exception as e:
            print(f"Object could not be serialized{e}")
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Object could not be serialized{e}")
            return None