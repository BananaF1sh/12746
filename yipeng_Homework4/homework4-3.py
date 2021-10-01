'''
Name: Yi Peng AndrewID: yipeng Homework: 4-3 coursenumber: 12746 
''' 
 
class Kangaroo:
    '''
    Initialize the Kangaroo.
    name: string
    pouch_contents: a list to store some elements.
    '''
    def __init__(self, name):
        self.name = name
        self.pouch_contents = []
    
    '''
    put an element into the pouch
    '''
    def put_in_pouch(self, element):
        self.pouch_contents.append(element)
    
    '''
    show the elements storing by this kangaroo
    '''
    def __str__(self) -> str:
        text = "This kangaroo has "
        for obj in self.pouch_contents:
            text = text + repr(obj) + ' '
        return text

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('baby_kanga')
kanga.put_in_pouch('baby_roo')
kanga.put_in_pouch(roo)
print(kanga)
print(roo)