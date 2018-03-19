__version__ = '1.0'
__author__ = 'Dominik Wiechers'


class OrGate:

    def __init__(self):
        self._input0 = False
        self._input1 = False
        self._output = False 
        self._name = "YaAnd"

    def show(self): 
        print(self._name)
        print(OrGate.__str__(self)) 

    def execute(self):
        if self._input0 == True: 
            self._output = True
        else:
            if self._input1 == True:
                self._output = True
            else:
                self._output = False

    def __str__(self): 
        return str(self._input0)+"+"+str(self._input1)+"="+str(self._output) 

    @property
    def input0(self, value):
        if isinstance(value, bool):
            self._input0 = value
            return self._input0

    @property
    def input1(self, value):
        if isinstance(value, bool):
            self._input1 = value
            return self._input1

    @property
    def output(self, value):
        if isinstance(value, bool):
            self._ouput = value
            return self._ouput

    @property
    def name(self, value):
        self._name = str(value)
        return self._name
