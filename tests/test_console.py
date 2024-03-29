#!/usr/bin/python3
"""This module tests the AirBnB Console program
"""
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import unittest
import os


def tearDownModule():
    """This function clears the file.json after testing is done
    """
    try:
        os.remove('file.json')
        storage.all().clear()
        storage.save()
    except Exception:
        pass


class Console_attributes_test(unittest.TestCase):
    """This class tests the attributes of the console program.
    """
    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
        self.assertIsInstance(HBNBCommand.prompt, str)


class Console_emptyline_test(unittest.TestCase):
    """This class tests the emptyline command of the console
    program
    """
    def test_emptyline_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), "")


class Console_quit_test(unittest.TestCase):
    """This class tests the quit command of the console
    program
    """
    def test_quit_only_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), "")

    def test_quit_with_one_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit arg1")
        self.assertEqual(f.getvalue(), "")

    def test_quit_with_more_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit arg1 arg2 arg3")
        self.assertEqual(f.getvalue(), "")


class Console_help_test(unittest.TestCase):
    """This class tests the help command in the console.
    """
    def test_help_no_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertEqual(len(f.getvalue()), 143)

    def test_help_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help \"\"")
        self.assertEqual(f.getvalue(), "*** No help on \"\"\n")

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        self.assertEqual(f.getvalue(), "Quit command to exit the program\n" +
                         "        \n")

    def test_help_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        self.assertEqual(f.getvalue(), "EOF exits the program\n        \n")

    def test_help_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        self.assertEqual(len(f.getvalue()), 100)

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual(len(f.getvalue()), 96)

    def test_help_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        self.assertEqual(len(f.getvalue()), 60)

    def test_help_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        self.assertEqual(len(f.getvalue()), 99)

    def test_help_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        self.assertEqual(len(f.getvalue()), 100)

    def test_help_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        self.assertEqual(len(f.getvalue()), 64)

    def test_help_default(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        self.assertEqual(len(f.getvalue()), 31)

    def test_help_invalid(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help INVALIDcmd")
        self.assertEqual(len(f.getvalue()), 26)


class Console_EOF_test(unittest.TestCase):
    """This class tests the EOF command of the console
    program
    """
    def test_EOF_only_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), "\n")

    def test_EOF_with_one_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF arg1")
        self.assertEqual(f.getvalue(), "\n")

    def test_EOF_with_more_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF arg1 arg2 arg3")
        self.assertEqual(f.getvalue(), "\n")


class Console_create_test(unittest.TestCase):
    """This class tests the create command of the console
    program
    """
    def test_create_only_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_random_arg_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create ROBOT")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_BaseModel_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertEqual(len(f.getvalue()), 37)
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                jsonstr = f.read()
            self.assertTrue('BaseModel' in jsonstr)
        except Exception:
            pass

    def test_create_User_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertEqual(len(f.getvalue()), 37)

    def test_create_City_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        self.assertEqual(len(f.getvalue()), 37)

    def test_create_State_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        self.assertEqual(len(f.getvalue()), 37)

    def test_create_Review_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        self.assertEqual(len(f.getvalue()), 37)

    def test_create_Place_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        self.assertEqual(len(f.getvalue()), 37)

    def test_create_Amenity_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        self.assertEqual(len(f.getvalue()), 37)

    def test_create_more_than_one_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity hello world")
        self.assertEqual(len(f.getvalue()), 37)


class Console_show_test(unittest.TestCase):
    """This class tests the show command of the console
    """
    def test_show_only_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_fake_class_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show ROBOT")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_valid_class_only_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_invalid_id_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review fake-id-2384324")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_review_class_arg(self):
        a = Review()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_place_class_arg(self):
        a = Place()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_BaseModel_class_arg(self):
        a = BaseModel()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_User_class_arg(self):
        a = User()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_Amenity_class_arg(self):
        a = Amenity()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_City_class_arg(self):
        a = City()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_State_class_arg(self):
        a = State()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_lots_of_spaces_arg(self):
        a = City()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("   show           City     {}".format(a.id))
        self.assertEqual(f.getvalue(), "{}\n".format(str(a)))

    def test_more_than_three_args(self):
        a = User()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City {} 4thargument".format(a.id))


class Console_destroy_test(unittest.TestCase):
    """This class tests the destroy command of the console.
    """
    def test_destroy_only_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_fake_class_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy ROBOT")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_valid_class_only_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_invalid_id_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review fake-id-2384324")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_base_model_destroy(self):
        a = BaseModel()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_user_destroy(self):
        a = User()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User {}".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_place_destroy(self):
        a = Place()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Place {}".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_state_destroy(self):
        a = State()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State {}".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_city_destroy(self):
        a = City()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City {}".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_amenity_destroy(self):
        a = Amenity()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity {}".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_review_destroy(self):
        a = Review()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review {}".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_destroy_4_args(self):
        a = Review()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review {} Helloo".format(a.id))
        self.assertEqual(f.getvalue(), "")


class Console_all_test(unittest.TestCase):
    """This class tests the all command of the console program
    """
    def setUp(self):
        """clears the objects dictionary"""
        try:
            os.remove('file.json')
        except Exception:
            pass
        storage.all().clear()
        storage.save()

    def test_all_no_args(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        storage.new(State())
        storage.new(City())
        storage.new(Review())
        storage.new(Amenity())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        string = f.getvalue()
        self.assertTrue("BaseModel" in string)
        self.assertTrue("User" in string)
        self.assertTrue("Place" in string)
        self.assertTrue("State" in string)
        self.assertTrue("City" in string)
        self.assertTrue("Review" in string)
        self.assertTrue("Amenity" in string)

    def test_BaseModel_arg(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        string = f.getvalue()
        self.assertTrue("BaseModel" in string)
        self.assertTrue("User" not in string)
        self.assertTrue("Place" not in string)

    def test_User_arg(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("User" in string)
        self.assertTrue("Place" not in string)

    def test_Place_arg(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("User" not in string)
        self.assertTrue("Place" in string)

    def test_State_arg(self):
        storage.new(BaseModel())
        storage.new(State())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("State" in string)
        self.assertTrue("Place" not in string)

    def test_City_arg(self):
        storage.new(BaseModel())
        storage.new(City())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("City" in string)
        self.assertTrue("Place" not in string)

    def test_Review_arg(self):
        storage.new(BaseModel())
        storage.new(Review())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("Review" in string)
        self.assertTrue("Place" not in string)

    def test_Amenity_arg(self):
        storage.new(BaseModel())
        storage.new(Amenity())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("Amenity" in string)
        self.assertTrue("Place" not in string)

    def test_unkown_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Robots")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")


class Console_update_test(unittest.TestCase):
    """This class tests the update command in the console program.
    """
    def setUp(self):
        """clears the objects dictionary"""
        try:
            os.remove('file.json')
        except Exception:
            pass
        storage.all().clear()
        storage.save()

    def test_no_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update ROBOTCLASS")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_valid_class_only(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_valid_class_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel VERYVALIDID9324-3243")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_valid_obj_no_key_arg(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {}".format(a.id))
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")

    def test_valid_obj_no_value_arg(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} name".format(a.id))
        self.assertEqual(f.getvalue(), "** value missing **\n")

    def test_BaseModel_arg(self):
        a = BaseModel()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} name Holberton".format(
                a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_User_arg(self):
        a = User()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {} name Holberton".format(
                a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_State_arg(self):
        a = State()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State {} name Holberton".format(
                a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_City_arg(self):
        a = City()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City {} name Holberton".format(
                a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_Amenity_arg(self):
        a = Amenity()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity {} name Holberton".format(
                a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_Place_arg(self):
        a = Place()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Place {} name Holberton".format(
                a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_Review_arg(self):
        a = Review()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Review {} name Holberton".format(
                a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_quotedkey_arg(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "update BaseModel {} \"my email\" a@gmail.com".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertTrue("my email" in a.__dict__)

    def test_quotedval_arg(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "update BaseModel {} name \"Abdelrahman Hany\"".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertTrue("Abdelrahman Hany" in a.__dict__.values())

    def test_morethan5_args(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "update BaseModel {} age 29 hello there extra".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertTrue("hello" not in a.__dict__)

    def test_int_val(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "update BaseModel {} age 29".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertIsInstance(a.age, int)

    def test_float_val(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "update BaseModel {} age 29.5453".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertIsInstance(a.age, float)

    def test_written_to_json(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "update BaseModel {} age 29.5453".format(a.id)
            HBNBCommand().onecmd(cmd)
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                jsonstr = f.read()
                assertTrue("age" in jsonstr)
        except Exception:
            pass

    def test_changing_already_existing_attr(self):
        a = BaseModel()
        a.age = 32
        self.assertEqual(a.age, 32)
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "update BaseModel {} age 29.5453".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertEqual(a.age, 29.5453)


class Console_count_test(unittest.TestCase):
    """This class tests the count command in the console program
    """
    def setUp(self):
        """clears the objects dictionary"""
        try:
            os.remove('file.json')
        except Exception:
            pass
        storage.all().clear()
        storage.save()

    def test_no_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
        self.assertEqual(f.getvalue(), "")

    def test_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count ROBOTCLASS")
        self.assertEqual(f.getvalue(), "")

    def test_BaseModel_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
        self.assertEqual(f.getvalue(), "2\n")

    def test_User_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
        self.assertEqual(f.getvalue(), "1\n")

    def test_State_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(State())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
        self.assertEqual(f.getvalue(), "1\n")

    def test_City_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(City())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
        self.assertEqual(f.getvalue(), "1\n")

    def test_Amenity_class(self):
        storage.new(BaseModel())
        storage.new(Amenity())
        storage.new(Amenity())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
        self.assertEqual(f.getvalue(), "2\n")

    def test_Place_class(self):
        storage.new(Place())
        storage.new(Review())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
        self.assertEqual(f.getvalue(), "1\n")

    def test_Review_class(self):
        storage.new(Review())
        storage.new(Review())
        storage.new(Review())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
        self.assertEqual(f.getvalue(), "3\n")

    def test_nonexistent_valid_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
        self.assertEqual(f.getvalue(), "0\n")


class Console_default_test(unittest.TestCase):
    """This class tests the default method of the console.
    """
    def setUp(self):
        """clears the objects dictionary"""
        try:
            os.remove('file.json')
        except Exception:
            pass
        storage.all().clear()
        storage.save()

    def test_unkowncommand(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("ROBOCOMMAND")
        self.assertEqual(f.getvalue(), "*** Unknown syntax: ROBOCOMMAND\n")

    def test_BaseModel_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        self.assertEqual(len(f.getvalue()), 37)

    def test_User_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        self.assertEqual(len(f.getvalue()), 37)

    def test_Place_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        self.assertEqual(len(f.getvalue()), 37)

    def test_State_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        self.assertEqual(len(f.getvalue()), 37)

    def test_City_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        self.assertEqual(len(f.getvalue()), 37)

    def test_Amenity_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        self.assertEqual(len(f.getvalue()), 37)

    def test_Review_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        self.assertEqual(len(f.getvalue()), 37)

    def test_unkown_dot_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("ROBOT.create()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_dot_no_id_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_unknown_dot_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("ROBOT.show()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_dot_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show()")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_BaseModel_dot_show(self):
        a = BaseModel()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), str(a)+'\n')

    def test_no_instance_found_dot_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(\"7238437284723847\")")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_User_dot_show(self):
        a = User()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), str(a)+'\n')

    def test_Place_dot_show(self):
        a = Place()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), str(a)+'\n')

    def test_State_dot_show(self):
        a = State()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), str(a)+'\n')

    def test_City_dot_show(self):
        a = City()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), str(a)+'\n')

    def test_Amenity_dot_show(self):
        a = Amenity()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), str(a)+'\n')

    def test_Review_dot_show(self):
        a = Review()
        storage.new(a)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), str(a)+'\n')

    def test_None_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show(None)")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_dot_no_id_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_dot_no_class_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".destroy(\"3424234234\")")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_dot_unknown_class_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Hello.destroy(\"3424234234\")")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_BaseModel_dot_destroy(self):
        a = BaseModel()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_User_dot_destroy(self):
        a = User()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_Place_dot_destroy(self):
        a = Place()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_State_dot_destroy(self):
        a = State()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_City_dot_destroy(self):
        a = City()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_Amenity_dot_destroy(self):
        a = Amenity()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_Review_dot_destroy(self):
        a = Review()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_dot_destroy_4args(self):
        a = Review()
        storage.new(a)
        self.assertTrue(a in storage.all().values())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy(\"{}\", Hello!)".format(a.id))
        self.assertEqual(f.getvalue(), "")
        self.assertTrue(a not in storage.all().values())

    def test_dot_all_no_class(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        storage.new(State())
        storage.new(City())
        storage.new(Review())
        storage.new(Amenity())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" in string)
        self.assertTrue("User" in string)
        self.assertTrue("Place" in string)
        self.assertTrue("State" in string)
        self.assertTrue("City" in string)
        self.assertTrue("Review" in string)
        self.assertTrue("Amenity" in string)

    def test_dot_all_BaseModel_arg(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" in string)
        self.assertTrue("User" not in string)
        self.assertTrue("Place" not in string)

    def test_dot_all_User_arg(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("User" in string)
        self.assertTrue("Place" not in string)

    def test_dot_all_Place_arg(self):
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("User" not in string)
        self.assertTrue("Place" in string)

    def test_dot_all_State_arg(self):
        storage.new(BaseModel())
        storage.new(State())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("State" in string)
        self.assertTrue("Place" not in string)

    def test_dot_all_City_arg(self):
        storage.new(BaseModel())
        storage.new(City())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("City" in string)
        self.assertTrue("Place" not in string)

    def test_dot_all_Review_arg(self):
        storage.new(BaseModel())
        storage.new(Review())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("Review" in string)
        self.assertTrue("Place" not in string)

    def test_dot_all_Amenity_arg(self):
        storage.new(BaseModel())
        storage.new(Amenity())
        storage.new(Place())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        string = f.getvalue()
        self.assertTrue("BaseModel" not in string)
        self.assertTrue("Amenity" in string)
        self.assertTrue("Place" not in string)

    def test_dot_all_unkown_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Robots.all()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_dot_update_no_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update()")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_dot_update_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("ROBOTCLASS.update()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_dot_update_valid_class_only(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_dot_update_valid_class_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(\"VERYVALIDID9324-3243\")")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_dot_update_valid_obj_no_key_arg(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(\"{}\")".format(a.id))
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")

    def test_dot_update_valid_obj_no_value_arg(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(\"{}\", name".format(a.id))
        self.assertEqual(f.getvalue(), "** value missing **\n")

    def test_update_BaseModel_arg(self):
        a = BaseModel()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                ("BaseModel.update(\"{}\", " +
                 "\"name\", \"Holberton\"").format(a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_update_User_arg(self):
        a = User()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "User.update(\"{}\", \"name\", \"Holberton\"".format(a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_update_State_arg(self):
        a = State()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "State.update(\"{}\", \"name\", \"Holberton\"".format(a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_update_City_arg(self):
        a = City()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "City.update(\"{}\", \"name\", \"Holberton\"".format(a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_update_Amenity_arg(self):
        a = Amenity()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Amenity.update(\"{}\", \"name\", \"Holberton\"".format(a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_update_Place_arg(self):
        a = Place()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Place.update(\"{}\", \"name\", \"Holberton\"".format(a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_update_Review_arg(self):
        a = Review()
        time1 = a.updated_at
        a.name = "Betty"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Review.update(\"{}\", \"name\", \"Holberton\"".format(a.id))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertNotEqual(time1, time2)

    def test_update_quotedkey_arg(self):
        a = BaseModel()
        cmd = ("BaseModel.update(\"{}\", " +
               "\"my email\", \"a@mail.com\")").format(a.id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        self.assertTrue("my email" in a.__dict__)

    def test_update_quotedval_arg(self):
        a = BaseModel()
        cmd = "BaseModel.update(\"{}\", \"name\", \"abdu hany\")".format(a.id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        self.assertTrue("abdu hany" in a.__dict__.values())

    def test_update_morethan5_args(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = ('BaseModel.update(\"{}\", \"name\", ' +
                   '\"abdu\", \"hello\", \"bye\")').format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertTrue("hello" in a.__dict__)

    def test_update_int_val(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "BaseModel.update(\"{}\", \"age\", 29)".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertIsInstance(a.age, int)

    def test_update_float_val(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "BaseModel.update(\"{}\", \"age\", 29.4342)".format(a.id)
            HBNBCommand().onecmd(cmd)
        self.assertIsInstance(a.age, float)

    def test_update_written_to_json(self):
        a = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "BaseModel.update(\"{}\", \"age\", 29.4342)".format(a.id)
            HBNBCommand().onecmd(cmd)
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                jsonstr = f.read()
                assertTrue("age" in jsonstr)
        except Exception:
            pass

    def test_update_fromdict_BaseModel(self):
        a = BaseModel()
        time1 = a.updated_at
        a.name = "betty"
        cmd = ("BaseModel.update(\"{}\", "
               "{})").format(a.id, str(dict(name="abdu")))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        time2 = a.updated_at
        self.assertEqual(a.name, "abdu")
        self.assertNotEqual(time1, time2)

    def test_update_fromdict_User(self):
        a = User()
        time1 = a.updated_at
        a.name = "betty"
        cmd = "User.update(\"{}\", {})".format(a.id, str(dict(name="abdu")))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        time2 = a.updated_at
        self.assertEqual(a.name, "abdu")
        self.assertNotEqual(time1, time2)

    def test_update_fromdict_State(self):
        a = State()
        time1 = a.updated_at
        a.name = "betty"
        cmd = ("State.update(\"{}\", "
               "{})").format(a.id, str(dict(name="abdu")))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        time2 = a.updated_at
        self.assertEqual(a.name, "abdu")
        self.assertNotEqual(time1, time2)

    def test_update_fromdict_City(self):
        a = City()
        time1 = a.updated_at
        a.name = "betty"
        cmd = ("City.update(\"{}\", "
               "{})").format(a.id, str(dict(name="abdu")))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        time2 = a.updated_at
        self.assertEqual(a.name, "abdu")
        self.assertNotEqual(time1, time2)

    def test_update_fromdict_Amenity(self):
        a = Amenity()
        time1 = a.updated_at
        a.name = "betty"
        cmd = ("Amenity.update(\"{}\", "
               "{})").format(a.id, str(dict(name="abdu")))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        time2 = a.updated_at
        self.assertEqual(a.name, "abdu")
        self.assertNotEqual(time1, time2)

    def test_update_fromdict_Place(self):
        a = Place()
        time1 = a.updated_at
        a.name = "betty"
        cmd = ("Place.update(\"{}\", "
               "{})").format(a.id, str(dict(name="abdu")))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        time2 = a.updated_at
        self.assertEqual(a.name, "abdu")
        self.assertNotEqual(time1, time2)

    def test_update_fromdict_Review(self):
        a = Review()
        time1 = a.updated_at
        a.name = "betty"
        cmd = ("Review.update(\"{}\", "
               "{})").format(a.id, str(dict(name="abdu")))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        time2 = a.updated_at
        self.assertEqual(a.name, "abdu")
        self.assertNotEqual(time1, time2)

    def test_update_from_long_dict(self):
        a = User()
        time1 = a.updated_at
        a.name = "Betty"
        changedict = str(dict(name="Holberton", age=28, height=1.75))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(\"{}\", {})".format(a.id,
                                                                  changedict))
        time2 = a.updated_at
        self.assertEqual(a.name, "Holberton")
        self.assertIsInstance(a.name, str)
        self.assertEqual(a.age, 28)
        self.assertIsInstance(a.age, int)
        self.assertEqual(a.height, 1.75)
        self.assertIsInstance(a.height, float)
        self.assertNotEqual(time1, time2)

    def test_count_noargs(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".count()")
        self.assertEqual(f.getvalue(), "")

    def test_count_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("ROBOTCLASS.count()")
        self.assertEqual(f.getvalue(), "")

    def test_BaseModel_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "2\n")

    def test_User_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertEqual(f.getvalue(), "1\n")

    def test_State_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(State())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertEqual(f.getvalue(), "1\n")

    def test_City_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(City())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertEqual(f.getvalue(), "1\n")

    def test_Amenity_class(self):
        storage.new(BaseModel())
        storage.new(Amenity())
        storage.new(Amenity())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertEqual(f.getvalue(), "2\n")

    def test_Place_class(self):
        storage.new(Place())
        storage.new(Review())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertEqual(f.getvalue(), "1\n")

    def test_Review_class(self):
        storage.new(Review())
        storage.new(Review())
        storage.new(Review())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertEqual(f.getvalue(), "3\n")

    def test_nonexistent_valid_class(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(User())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertEqual(f.getvalue(), "0\n")


if __name__ == "__main__":
    unittest.main()
