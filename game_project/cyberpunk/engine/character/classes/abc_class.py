from abc import ABC, abstractmethod
from typing import List

class IClass(ABC):

    __class_name__: object

    perks: List[object]
    skills: List[object]

    # @abstractmethod
    # def method(self, object_under_action, action):
    #     controller.method(self, object_under_action, action)

    # def method(obj_class, object_under_action):
    #     object_under_action.type = door
    #         door_control.method()

