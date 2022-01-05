from typing import Any, Callable


def FindMatch(list_of_options: list[Any], predicate: Callable[[Any],bool]):
    for index in range(0,list_of_options.__len__() - 1,2):
        if(predicate(list_of_options[index])):
            return list_of_options[index+1]
    raise Exception("Did not find match")
    