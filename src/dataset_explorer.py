from src.dataset_info import DataSetInfo


class Explorer:
    """

    """
    def __init__(self, dataset):
        self.dataset = dataset
        self.dataset.info = DataSetInfo()
        return

    def understand(self):
        """

        :return:
        """
        self.dataset.info.understand_attributes(self.dataset.data, self.dataset.type)
        return

    def explore_attributes(self):
        """

        :return:
        """
        self.dataset.info.populate_attribute(self.dataset.data, self.dataset.type)
        print('JKHJKKK')
        return

    def explore_metrics(self):
        """

        :return:
        """
        return
