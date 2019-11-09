class TagCloud:
    # define a constructor
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        # returns an iterator object which gives us one item at a time in a for loop
        return iter(self.__tags)


cloud = TagCloud()

cloud["python"] = 10
len(cloud)
# we made it private by prefixing with '__'
# print(cloud.__tags)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags)


# operations supported by this custom container type
# cloud = TagCloud()
# len(cloud)
# cloud["python"] = 10 # get an item by its key
# for tag in cloud:
#     print(tag)

"""
    In Python unlike C# or Java we don't really have the concept of private members.  These private members are still accessible from the outside.  Using double underscores is more convention to prevent accidental access of these private members.
"""
