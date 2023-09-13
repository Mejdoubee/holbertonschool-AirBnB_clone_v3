
# Holberton School's AirBnB Clone Project
![UML Diagram](http://www.plantuml.com/plantuml/dpng/ZPA_JiCm4CRtF8N7H2WRCogjX6008IfcwneVhT4bBlQbLGMyEqxFZOAHQBFO_drVxi_Piy3WkM-fQ0X2K7C8-EWCaleiLFok0lkoxwsvhfGrWWmmicrHDHxZrcZWJEYtvfUWTGoZTLcfkDfkdKB33ijAzkoqiGr7nx0KtwcSEqkuPETXZQcWMY8ehT-YfhV06-73Vv6wrJis72Gg4AM8SkvmNqP3zJU_Ht9WukcK-Nx-D5-ujeNEd3AJ3QoEAgRunkcFtd89VXqgjNAEHYwp4MM4OUFs6J8OsBj3He4e8p9IWMEHhm5zgkwXsw2tFBd1qRLaO3nlMrW-d7VTjjXTP7mcQ2x8-e8xY_l_VDCtuEfweatlQ50cpk8uchh-kfduPH0P7DhEMMeonz9I1gM1dCwmCtrBFm00)
## Overview

This project is a simplified clone of AirBnB, focusing on the backend part. It includes a command-line interpreter to manipulate data without a visual interface, perfect for development and debugging. The goal of this project is to deploy a simple copy of the AirBnB website. With the recent updates, we have integrated ORM capabilities, added relationships between models, and provided two types of storage engines - `FileStorage` and `DBStorage`.

## Components

### 1. BaseModel

The `BaseModel` class defines all common attributes/methods for other classes. It includes the following methods:

-   `__init__`: Initializes the base model.
-   `__str__`: Returns the string representation of the object.
-   `save`: Updates the `updated_at` attribute with the current datetime.
-   `to_dict`: Returns a dictionary containing all keys/values of the object.

### 2. FileStorage

The `FileStorage` class serializes instances to a JSON file and deserializes the JSON file to instances. It includes the following methods:

-   `all`: Returns the dictionary `__objects`.
-   `new`: Sets the object in `__objects`.
-   `save`: Serializes `__objects` to a JSON file.
-   `reload`: Deserializes the JSON file to `__objects`.

![UML Diagram](http://www.plantuml.com/plantuml/dpng/ZP9DIyGm48Rl-HKvAkWVy23h1nu4Fx1uNiRsLI9fiYIpNVJNwn1jExL8Rk6Tvnc6p6moK-9zxysE4hlMxIYmlQICkzX1fpVEe-6Ow0qglsqUxgMcmkUCf8A6YJLovVX31HSzmZ9xzDHgxGc3my6OsJZsz7oQsPxPDe4ODhwyesKpLWIRMGAIzpRWSFID7kkEIpJJyDlHShJRRNddXJN-XYX8ZhpxX0YIcn1bh05ftlnaxZG_3h6BmPYnycUU3bDxeQh_mxwcsAygihDgkYoq7fTjrzFb5Eg5SYVrU3cYV_ZrJKtUDRBQr0QXs_V-2m00)


### 3. DBStorage

The newer storage engine which provides interaction with databases. It's built on top of SQLAlchemy, a popular ORM for Python. The main advantages of DBStorage are:

Scalability: Suitable for larger datasets.
Reliability: ACID-compliant, ensures data integrity.
Powerful Query Language: Can leverage SQL for complex queries.
Relationships: Supports complex relationships between classes.


 ```sql
   BaseModel
      ^
      |
  +---+---+---+---+---+---+
  |   |   |   |   |   |   |
State City User Place Review Amenity
  |   |   |   |   |   |
  +---+---+---+---+---+
      |       |       |
      +-------+-------+
              |
          DBStorage

 ```



### 4. Console (Command Interpreter)

The `HBNBCommand` class serves as a command interpreter. Supported commands include:

-   `quit` and `EOF`: Exit the program.
-   `create`: Creates a new instance of a specified class.
-   `show`: Prints the string representation of an instance based on class name and id.
-   `destroy`: Deletes an instance based on class name and id.
-   `all`: Prints all string representations of all instances.
-   `update`: Updates an instance based on class name and id.

### 5. Other Classes

The project also includes specific classes like `User`, `State`, `City`, `Amenity`, `Place`, and `Review`, These models have attributes specific to their functionalities and establish relationships among each other using the ORM's capabilities, such as one-to-many and many-to-many relations.


## Usage

1.  Clone the repository.
2.  Navigate to the project directory.
3.  Run the command-line interpreter using `python3 console.py`.
4.  Use supported commands to interact with the system.

Example usage:

 ```python
 python3./console.py
 (hbnb) create BaseModel
 (hbnb) show BaseModel <id>
 (hbnb) all
 (hbnb) update BaseModel <id> name "John" (hbnb)
 quit
 ```


 ## Testing

Unit tests are provided for different parts of the project. Run the tests using:
```python
python3 -m unittest discover tests
```


