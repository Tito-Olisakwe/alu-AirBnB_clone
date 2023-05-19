#!/usr/bin/python3
"Entry point of the command interpreter"
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '  # Set the custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        instances = []

        if not args:
            instances = list(storage.all().values())
        else:
            class_name = args[0]
            if class_name not in storage.all().keys():
                print("** class doesn't exist **")
                return
            instances = [v for k, v in storage.all().items() if class_name in k]

        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        if len(args) < 3 or not args[2]:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3].strip('"')
        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
