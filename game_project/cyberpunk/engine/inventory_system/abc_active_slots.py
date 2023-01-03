from abc_implants import implants


class IActiveSlots:

    head:object
    rhand:object
    lhand:object

    legs:object
    boots:object
    torso:object

    implants:implants #TODO: maybe implants:implants here as a part of active slots???

    #TODO: methods to work with active slots? equip/unequip for example