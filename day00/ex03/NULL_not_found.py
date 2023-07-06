def NULL_not_found(object: any) -> int:
    # print("Object: " + str(object) + " " + str(type(object)))
    if object is None:
        print("Nothing: None "+ str(type(object)))
    elif str(object) == "nan" and type(object) == float:
        print("Cheese: nan " + str(type(object)))
    elif type(object) == int and object == 0:
        print("Zero: 0 " + str(type(object)))
    elif type(object) == str and object == '':
        print("Empty: '' " + str(type(object)))
    elif type(object) == bool and object == False:
        print("Fake: False " + str(type(object)))
    else:
        print("Type not Found")
        return 1
    return 0