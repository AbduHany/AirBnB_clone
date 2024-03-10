#!/usr/bin/python3
"""This module describes the unittests for base_model

"""
import unittest
import os
import datetime
import io
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel_instantiation(unittest.TestCase):
    """Defines all unittests for testing instantiation of BaseModel class"""

    def test_instantiation(self):
        """This method tests the normal instantiation of BaseModel"""

        a = BaseModel()
        self.assertEqual(str(type(a)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(a, BaseModel)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_instantiation_no_args(self):
        """This method tests the instantiation of BaseModel with no args"""

        with self.assertRaises(TypeError):
            BaseModel.__init__()

    def test_instantiation_None_arg(self):
        """This method tests the instantiation of BaseModel with many args"""

        with self.assertRaises(AttributeError):
            BaseModel.__init__(None)

    def test_instantiation_int_arg(self):
        """This method tests the instantiation of BaseMode with an int arg"""

        with self.assertRaises(AttributeError):
            BaseModel.__init__(1, 1, 2, 4, 5)

    def test_instantiation_bytes_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(b'Bytes', b'Python', b'Simple')

    def test_instantiation_str_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__("Invalid", "Strings", "Mental")

    def test_instantiation_empty_str_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__("")

    def test_instantiation_bool_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(True)

    def test_instantiation_zero_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(0, 0, 0, 0, 0, 0)

    def test_instantiation_float_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(11.1, 12.8, 54.34, 5.009, 32.9)

    def test_instantiation_neg_val_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(-10, -9, -6, -500)

    def test_instantiation_set_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__({1, 2}, {80, 4, 56, 6}, {89, -98})

    def test_instantiation_tupl_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__((1, 2), )

    def test_instantiation_list_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(['string', 3, 6.8])

    def test_instantiation_dict_arg(self):
        with self.assertRaises(AttributeError):
            now = datetime.datetime.now()
            BaseModel.__init__({'id': 'Holberton', 'created_at': now})

    def test_instantiation_inf_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(float('inf'))

    def test_instantiation_nan_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(float('nan'))

    def test_instantiation_kwargs_class_id_other(self):
        now = datetime.datetime.now()
        kwargs = {'__class__': BaseModel,
                  'id': "888800008888",
                  'created_at': str(now),
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_other(self):
        now = datetime.datetime.now()
        kwargs = {'created_at': str(now),
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        BaseModel(**kwargs)
        self.assertRaises(AttributeError)

    def test_instantiation_kwargs_other_no_ca(self):
        now = datetime.datetime.now()
        kwargs = {'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        BaseModel(**kwargs)
        self.assertRaises(AttributeError)

    def test_instantiation_kwargs_other_no_ca_ua(self):
        kwargs = {'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        BaseModel(**kwargs)
        self.assertRaises(AttributeError)

    def test_instantiation_kwargs_other_no_ca_ua_fn(self):
        kwargs = {'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        BaseModel(**kwargs)
        self.assertRaises(AttributeError)

    def test_instantiation_kwargs_other_no_ca_ua_fn_ln(self):
        kwargs = {'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        BaseModel(**kwargs)
        self.assertRaises(AttributeError)

    def test_instantiation_kwargs_other_no_ca_ua_fn_ln_email(self):
        kwargs = {'age': 98,
                  'weight': 100.048
                  }
        BaseModel(**kwargs)
        self.assertRaises(AttributeError)

    def test_instantiation_kwargs_other_no_ca_ua_fn_ln_email_a(self):
        kwargs = {'weight': 100.048
                  }
        BaseModel(**kwargs)
        self.assertRaises(AttributeError)

    def test_instantiation_kwargs_empty(self):
        kwargs = {}
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_None(self):
        kwargs = None
        with self.assertRaises(TypeError) as e:
            BaseModel(**kwargs)
        err = "type object argument after ** must be a mapping, not NoneType"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_kwargs_id_other(self):
        now = datetime.datetime.now()
        kwargs = {'id': "888800008888",
                  'created_at': str(now),
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca(self):
        now = datetime.datetime.now()
        kwargs = {'id': "888800008888",
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua(self):
        kwargs = {'id': "888800008888",
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn(self):
        kwargs = {'id': "888800008888",
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn_ln(self):
        kwargs = {'id': "888800008888",
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn_ln_email(self):
        kwargs = {'id': "888800008888",
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn_ln_email_a(self):
        kwargs = {'id': "888800008888",
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id(self):
        kwargs = {'id': "888800008888"}
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))


class TestBaseModel_str(unittest.TestCase):
    """This class tests the str method of a User
    class instance
    """
    def setUp(self):
        """redirecting stdout to output
        """
        self.output = io.StringIO()
        self.originalstdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """resetting stdout to its original
        value
        """
        sys.stdout = self.originalstdout

    def test_str_method(self):
        a = BaseModel()
        self.assertEqual(a.__str__(),
                         "[BaseModel] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = BaseModel()
        self.assertEqual(str(a),
                         "[BaseModel] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = BaseModel()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[BaseModel] ({}) {}\n".format(a.id, a.__dict__))


class TestBaseModel_save_test(unittest.TestCase):
    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
