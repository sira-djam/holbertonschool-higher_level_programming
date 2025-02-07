# Define the CountedIterator class which extends the built-in iterator
class CountedIterator:
    def __init__(self, iterable):
        # Initialize with the given iterable and set the counter to 0
        self.iterable = iterable
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0  # Initialize the counter to 0

    # Override the __next__ method to track the number of items iterated over
    def __next__(self):
        try:
            # Fetch the next item from the iterator
            item = next(self.iterator)
            # Increment the count
            self.count += 1
            # Return the item
            return item
        except StopIteration:
            # If iteration is finished, raise StopIteration to indicate the end
            raise StopIteration

    # Optional: method to get the count of items iterated so far
    def get_count(self):
        return self.count


# Test the CountedIterator class
items = [10, 20, 30, 40, 50]

# Create an instance of CountedIterator
counted_iter = CountedIterator(items)

# Iterate over the items and print them along with the count
for item in counted_iter:
    print(f"Item: {item}, Count: {counted_iter.get_count()}")
