#!/usr/bin/python3
""" Base Class"""


import json
import csv
import os


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base initialization"""
        if id is None:
            base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @statcismethod
    def to_json_string(list_dictionaries):
        """Returning json string representation of the list of dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saving list of objects to file"""
        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list+objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'size', 'x', 'y']
                writer = cvs.DicWriter(f, fieldnames=feilds)
                writer.writeheader()
                writer.writerows(list_objs)

    @staticmethod
    def from_json_string(json_string):
        """return list of objects from json string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instance of class Base"""
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """load list of objects from file"""
        filename = cls.__name__ + ".json"
        m = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    m.append(cls.create(**d))
        return m

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string representation of list_objs to file"""
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """return list of json string represantation json_string"""
        new_len = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeErro("json_string must be a string")
            new_len = json.loads(json_string)
        return new_len

    @ classmethod
    def create(cls, **dictionary):
        """return instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @ classmethod
    def load_from_file(cls):
        """return list of instances"""
        filename = cls.__name__ + '.json'
        new_loader = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    new_loader.append(cls.create(**d))
        return new_loader

    @ classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize list_objs in CSV format and save it to file"""
        if (type(list_objs) != list and list_objs is
           not None or not all(isinstance(x, cls)
           for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @ classmethod
    def load_from_file_cvs(cls):
        """serializes and deserializes list of instances"""
        filename = cls.__name__ + ".csv"
        new_load = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimeter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                satattr(i, fields[j], int(e))
                        new_load.append(i)
        return new_load

    @ staticmethod
    def draw(list_rectangles, list_sqaures):
        """static method that opens window and draws all the instances"""
        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @ staticmethod
    def draw_rect(t, rect):
        """method that draws a rectangle or square"""
        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
