from abc_implant import implants


class IActiveSlots:

    head:object

    l_arm:object
    r_arm:object

    r_hand:object
    l_hand:object

    legs:object
    boots:object
    torso:object

    implants:implants #TODO: maybe implants:implants here as a part of active slots???

    #TODO: methods to work with active slots? equip/unequip for example