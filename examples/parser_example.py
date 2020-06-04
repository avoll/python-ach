from ach.parser import Parser
import pprint
from sys import argv

with open(argv[1]) as fh:
    body = fh.read()

data = Parser(body)

print(pprint.pformat(data.as_dict()))
