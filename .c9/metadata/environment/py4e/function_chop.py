{"filter":false,"title":"function_chop.py","tooltip":"/py4e/function_chop.py","undoManager":{"mark":-1,"position":-1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":24,"column":1},"action":"remove","lines":["#!/usr/bin/python3","#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.","","def chop(inp_list):","    del inp_list[0]","    del inp_list[-1]","    return None","    ","def middle(inp_list):","    ret_list=inp_list[1:-1]","    return ret_list    ","","usr_list=list()","","while True:","    element=input(\"Enter an integer/Done when done!: \")","    if element=='Done':","        break","    usr_list.append(element)","    ","new_list=middle(usr_list)","print(new_list)",""," "," "],"id":341}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":13},"end":{"row":17,"column":13},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1706376096005,"hash":"5b1710b0ba223a3a64eb2bf30886954d02e90edf"}