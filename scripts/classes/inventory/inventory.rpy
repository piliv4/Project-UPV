init python:
    class Inventory:
        def __init__(self):
            self.items = []

        def addItem(self, item):
            self.items.append(item)

        def removeItem(self, item):
            self.items.remove(item)

        def getItemByIndex(self, index):
            return self.items[index]