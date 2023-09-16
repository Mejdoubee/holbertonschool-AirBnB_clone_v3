#!/usr/bin/python3
"""
Model defines file_storage class that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_mapping = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects.
        If cls is provided, returns a filtered dictionary.
        """
        if not cls:
            return self.__objects
        if issubclass(cls, BaseModel):
            return {
                k: v for k, v in self.__objects.items() if isinstance(v, cls)
            }
        else:
            return {}

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w') as f:
            json_objs = {
                key: obj.to_dict() for key, obj in self.__objects.items()
                }
            json.dump(json_objs, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)

            for value in obj_dict.values():
                class_name = value.pop("__class__", None)
                if class_name:
                    class_instance = class_mapping.get(class_name)
                    if class_instance:
                        obj = class_instance(**value)
                        self.new(obj)

        except (FileNotFoundError, json.JSONDecodeError):
            return

    def delete(self, obj=None):
        """
        Delete obj from __objects if inside;
        if obj is None, the method does nothing.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    @property
    def reviews(self):
        """
        Return list of Review instances with place_id
        equal to the current Place.id
        """
        from models import storage
        all_reviews = storage.all(Review)
        place_reviews = [review for review in all_reviews.values()
                         if review.place_id == self.id]
        return place_reviews

    def close(self):
        """ Deserializes the JSON file to objects """
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class and its ID
        """
        if cls not in class_mapping.values():
            return None
        all_classes = self.all(cls)
        for value in all_classes.values():
            if value.id == id:
                return value
        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        if cls:
            return len(self.all(cls))

        total_count = 0
        for class_name in class_mapping:
            total_count += len(self.all(class_name))
        return total_count
