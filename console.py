#!/usr/bin/python3
import cmd
from models.base_model import BaseModel 
from models import storage
import os


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        \nusage: $ create BaseModel
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line == "BaseModel":
                instance = BaseModel()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id
        \nUsage: $ show <class name> <id>
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            b = line.split()
            print(len(b))

            if b[0] == "BaseModel":
                if len(b) < 2:
                    print("** instance id missing **")
                else:
                    i = "{}.{}".format(b[0], b[1])
                    objects = storage.all()
                    a = -1

                    for obj_id in objects.keys():
                        obj = objects[obj_id]

                        if obj_id == i:
                            a = 1
                            print(obj)
                            break

                    if a != 1:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        \nUsage: $ destroy <class name> <id>
        """

        if len(line) == 0:
            print("** class name missing **")
        else:
            b = line.split()
            print(len(b))

            if b[0] == "BaseModel":
                if len(b) < 2:
                    print("** instance id missing **")
                else:
                    i = "{}.{}".format(b[0], b[1])
                    objects = storage.all()
                    a = -1

                    for obj_id in objects.keys():
                        obj = objects[obj_id]

                        if obj_id == i:
                            a = 1
                            del(objects[obj_id])
                            break
                        else:
                            pass

                    if a != 1:
                        print("** no instance found **")
                    else:
                        storage.__objects = objects
                        storage.save()

            else:
                print("** class doesn't exist **")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        exit()
    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
