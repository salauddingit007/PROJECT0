class phone:
    def __init__(self):
        print ("i am in phone class")
class samsung(phone):
    # pass
    #init
    def __init__(self):
        super().__init__()
        print('i am in samsung class')

        
s = samsung()