import os
import pickle

def create_folder(_path):
    directory = os.path.dirname(_path)
    os.makedirs(directory, exist_ok=True)


class AppendIndexer(object):

    def __init__(self):
        self.__indices = {}
        self.__indices_reverse = {}
        self.__next_idx = 0

    @classmethod
    def load(cls, filename):
        obj = cls()
        with open(filename, 'rb') as fin:
            obj.__indices, obj.__indices_reverse, obj.__next_idx = pickle.load(fin)
        return obj

    def dump(self, filename):

        tmp_filename = filename + '.tmp'
        create_folder(filename)

        with open(tmp_filename, 'wb') as fout:
            pickle.dump((self.__indices, self.__indices_reverse, self.__next_idx), fout)

        os.rename(tmp_filename, filename)

    def is_in(self, item: str) -> bool:
        return item in self.__indices

    def get(self, item: object) -> object:
        return self.__indices[str(item)]

    def reverse_get(self, index: int) -> str:
        return self.__indices_reverse.get(index)

    def remove_index(self, index: int):
        return self.remove_indexes([index])

    def remove_indexes(self, indexes: [int], get_new=0):
        indexes = set(filter(lambda idx: idx < self.size, indexes))

        if len(indexes) == 0:
            return self

        new_indexer = AppendIndexer()
        for i in range(self.size):
            if i not in indexes:
                new_indexer.get_or_create(self.reverse_get(i))

        if get_new:
            return new_indexer

        self.__indices = new_indexer.__indices
        self.__indices_reverse = new_indexer.__indices_reverse
        self.__next_idx = new_indexer.__next_idx

        return self

    def get_or_create(self, item) -> int:
        item = str(item)
        if item not in self.__indices:
            self.__indices[item] = idx = self.__next_idx
            self.__indices_reverse[idx] = item
            self.__next_idx += 1
        else:
            idx = self.__indices[item]
        return idx

    def get_items(self):
        return self.__indices.keys()

    @property
    def size(self) -> int:
        return self.__next_idx