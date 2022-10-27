#!/usr/bin/python3
"""Defines the entry point of the command interpreter HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models import storage

used_classes = {'BaseModel': BaseModel}

class HBNBCommand(cmd.Cmd):
    """The command interpreter Class """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Catch errors"""
        
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the Program"""
        
        return True

    def do_create(self, arg):
        """Creates a new instance"""
        
        args = arg.split()

        if not validate_classname(args):
            return 

        new_obj = used_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """ 
            Prints the string representation of an instance based on the 
            class name and id 
        """
        args = arg.split()
        if not validate_classname(args, chk_id=True):
            return

        instance_obj = storage.all()
        key = "{}.{}".format(args[0], args[1])
        chk_instance = instance_obj.get(key, None)
        if chk_instance is None:
            print("** no instance found **")
            return
        print(chk_instance)


    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        args = arg.split()

        if not validate_classname(args, chk_id=True):
            return

    def do_all(self, arg):
        """
            Prints all string representation of all instances based or not on
            the class name.
        """
        
        args = arg.split()
        
        if not validate_classname(args):
            return

        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return

        print(["{}".format(str(v)) for _, v in 
            all_objs.items() if type(v).__name__ == args[0]])
        return
        
def validate_classname(args, chk_id=False):
    """Check if class_name exist or checks if it is entered"""

    if len(args) < 1:
        print("** class name missing **")
        return False

    if args[0] not in used_classes.keys():
        print("** class doesn't exist **")
        return False

    if len(args) < 2 and chk_id:
        print("** instance id missing **")
        return False

    return True  
           

if __name__ == '__main__':
    HBNBCommand().cmdloop()
