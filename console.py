#!/usr/bin/python3
import cmd
from models.base_model import BaseModel 
from models import storage
import os
import json


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        \nusage: $ create BaseModel
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line == "BaseModel" or line == "User":
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

            if b[0] == "BaseModel" or b[0] == "User":
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

            if b[0] == "BaseModel" or "User":
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

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name
        \n Usage: $ all <Class name>
        """
        if len(line) < 2:
            objects = storage.all()

            for i in objects.keys():
                print(objects[i])
        else:
            b = line.split()

            if b[0] == "BaseModel" or b[0] == "User":

                objects = storage.all()

                for i in objects.keys():
                    print(objects[i])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute
        \nUsage: $ update <class name> <id> <attribute name> <attribute value>
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            b = line.split()

            if b[0] == "BaseModel" or b[0] == "User":
                if len(b) < 2:
                    print("** instance id missing **")
                elif len(b) < 3:
                    print("** attribute name missing **")
                elif len(b) < 4:
                    print("** value missing **")
                else:
                    id_key = "{}.{}".format(b[0], b[1])

                    objects = storage.all()

                    for obj_id in objects.keys():

                        obj = objects[obj_id]
                        if obj_id == id_key:
                            del(objects[obj_id])
                            obj = str(obj)
                            string = "{" + obj.split(" {")[1]

                            string = string.strip("{}")
                            ls_t = string.split(", \'")
                            dic_t = {}

                            for l in ls_t:

                                l1 = l.split(": ")
                                key = l1[0]
                                value = l1[1]

                                dic_t[key.replace("\'", "")] = value.replace("\'", "")
                            
                            if b[2] != "id" or b[2] != "created_at" or b[2] != "updated_at":
                                dic_t[b[2]] = b[3]

                            obj = "[{}] ({}) {}".format(b[0], dic_t["id"], dic_t)
                            objects[obj_id] = obj

                            storage.__objects = obj
                            storage.save()
                            break

    def do_clear(self, line):

        os.system('cls' if os.name == "nt" else "clear")
    def do_EOF(self, line):
        """EOF command to exit the program"""
        exit()
    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
