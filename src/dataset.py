import pandas as pd
from src.dataset_explorer import Explorer


class Dataset:
    """

    """

    def __init__(self):
        return

    def constructor(self,name):
        self.name = name
        self.type = "structured"
        self.description = "Sample Test Database"
        self.num_records = len(self.data)
        self.creation_date = ""
        self.creation_by = ""
        self.repo = ""
        self.branch = "master"
        self.version = 1
        self.tag = "1.0.0"

    def Import(self,datasource,localstore,sample =None):
        """

        :param datasource:
        :param localstore:
        :param sample:
        :return:
        """
        self.data = pd.read_csv(datasource)
        self.type = "structured"
        self.info = ""

    def save(self):
        return

    def load(self):
        return

    def diff(self):
        return


if __name__ == "__main__":
    data = Dataset()
    #data.Import("./config/test/data/test.csv", "", "")
    data.Import("Train.csv", "", "")
    #data.Import("../data/names.csv", "", "")
    explorer = Explorer(data)
    print('Data Understanding Starting')
    explorer.understand()
    print('***********************************')
    print('Data Exploration Starting')
    explorer.explore_attributes()
    #for val in data.info.attributeInfo:
        #print("Name : {} , Dtype : {} ,  Type : {} , Metrics : {} \n".format(
            #val.name,
            #val.dtype, val.type, val.metrics))
