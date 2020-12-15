import numpy
import json
import matplotlib.pyplot as plt

class base_class(object):
    def __init__(self, foo: str, bar: int, baz: dict):
        """Does some stuff

            Args:
                foo (int): The foo to bar
                bar (str): Bar to use on foo
                baz (float): Baz to frobn
        """
        self.eingang = [foo, bar, baz]

    def onifiy(self, in_num:int)->None:
        """Always returns one

        Args:
            in_num (int): input number, does not matter

        Returns:
            out(int): out is always one
        """
        if n_num:
            return 1
        else:
            return 1

class not_base_class(base_class):
    def __init__(self, foo:str, bar:int, baz:dict):
        __super__().__init(foo, bar, baz)
        """Does some stuff

           Args:
             foo (int): The foo to bar
             bar (str): Bar to use on foo
             baz (float): Baz to frobn
        """
    def return_nothing(*args,**kwargs)->None:
        """Always returns None

        Args:
            args and kwargs

        Returns:
            None
        """
        return(None)
