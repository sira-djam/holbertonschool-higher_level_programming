# Define a custom class VerboseList that extends the built-in list class
class VerboseList(list):

    # Override the append method to print a message when an item is added
    def append(self, item):
        super().append(item)  # Call the original append method from the list class
        print(f"Item '{item}' has been added to the list.")

    # Override the extend method to print a message when items are added
    def extend(self, iterable):
        super().extend(iterable)  # Call the original extend method from the list class
        print(f"Items {iterable} have been added to the list.")

    # Override the remove method to print a message when an item is removed
    def remove(self, item):
        super().remove(item)  # Call the original remove method from the list class
        print(f"Item '{item}' has been removed from the list.")

    # Override the pop method to print a message when an item is popped
    def pop(self, index=-1):
        item = super().pop(index)  # Call the original pop method from the list class
        print(f"Item '{item}' has been removed from the list (popped).")
        return item

# Test the VerboseList class
verbose_list = VerboseList()

# Adding items using append
verbose_list.append(10)
verbose_list.append(20)

# Adding multiple items using extend
verbose_list.extend([30, 40, 50])

# Removing an item using remove
verbose_list.remove(20)

# Popping an item using pop
verbose_list.pop()
