class MySet:

    def __init__(self, items):
        """Takes a list of items and builds a set with them, removing
           duplicates if necessary.
        """
        self.my_set = []
        [self.my_set.append(x) for x in items if x not in self.my_set]

    def add_item(self, item):
        """ Adds an item to the set if it is not already present. If the
            item is present, do nothing.
        """
        if(item not in self.my_set):
            self.my_set.append(item)

    def remove_item(self, item):
        """ Removes item from the set.  Does nothing if item is not
            in the set.
        """
        self.my_set.remove(item)

    def is_empty(self):
        """Returns True is the set has no members."""
        return not self.my_set

    def has_item(self, item):
        """returns True if item is in the set, False otherwise."""
        return item in self.my_set

    def intersection(self, otherset):
        """Returns a new set that is the intersection of self
           and otherset.
           """
        return [x for x in otherset if x in self.my_set]

    def union(self, otherset):
        """"Returns a new set that is the union of self and otherset"""
        return self.my_set + [x for x in otherset if x not in self.my_set]

    def is_subset_of(self, otherset):
        """Returns True if self is a subset of otherset."""
        self.sub_set = [x for x in self.my_set if x in otherset]
        return len(self.sub_set) == len(self.my_set)

    def is_equal_to(self, otherset):
        """Returns True if self and otherset are equal, i.e.,
           they have the exact same members.
        """
        return len([x for x in self.my_set if x in otherset]) == len(otherset);
        

    def is_proper_subset_of(self, otherset):
        """Returns True is self is a *proper* subset of otherset."""
        # Fails if set passed in with two identical values that is a
        # subset. Get the subset, if len is same as my_set and less
        # then supplied otherset, true.
        self.sub_set = [x for x in self.my_set if x in otherset]
        return (len(self.sub_set) == len(self.my_set) and 
                len(self.sub_set) < len(otherset))

