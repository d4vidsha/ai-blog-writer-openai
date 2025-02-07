import json

STORAGE = "private/storage.json"

#===============================================================================
#==================== ZAPIER'S INBUILT VARIABLES AND CLASSES ===================
#===============================================================================
class StoreClient:

    def __init__(self, uuid):
        self.uuid = uuid
        self.fp = open(STORAGE, "r")
        self.storage = json.load(self.fp)
        if uuid not in self.storage:
            self.storage[uuid] = {}

    def get(self, key):
        return self.storage[self.uuid][key]

    def set(self, key, value):
        self.storage[self.uuid][key] = value
        self.__save()

    def delete(self, key):
        self.storage[self.uuid].pop(key)
        self.__save()

    def get_many(self, *args):
        get_dict = {}
        for key in args:
            get_dict[key] = self.storage[self.uuid][key]
        return get_dict

    def set_many(self, **kwargs):
        for key,value in kwargs.items():
            self.storage[self.uuid][key] = value    
        self.__save()

    def delete_many(self, *args):
        for key in args:
            self.storage[self.uuid].pop(key)
        self.__save()

    def clear(self):
        self.storage[self.uuid].clear()
        self.__save()

    def __save(self):
        self.fp.close()
        with open(STORAGE, "w") as fp:
            json.dump(self.storage, fp, indent=4, sort_keys=True)
        self.fp = open(STORAGE, "r")

    def __del__(self):
        self.fp.close()

# leave empty
input_data = {}
output = {}