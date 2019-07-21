from dateutil.parser import parse
import numpy as np
import pandas as pd
from exception_handling.custom_exception import InvalidDataTypeException
from src.attribute_info import AttributeInfo, DataType


class DataSetInfo:
    """

    """
    DATA_TYPES = ["structured", "semi-structured", "unstructured"]

    def __init__(self):
        """

        """
        self.attributeInfo = list()
        self.metrics = dict()
        return

    def understand_attributes(self, data, type):
        """

        :param data:
        :param type:
        :return:
        """
        if type not in self.DATA_TYPES:
            raise InvalidDataTypeException("Provided Data Type : {} not ""supported".format(type))

        # For structured datatype
        elif type is "structured":
            print('Structured Data')
            self.attributeInfo = list(map(lambda x: AttributeInfo(x), data.columns))
            print(f'AttributeInfo:{self.attributeInfo}')

            for attr in self.attributeInfo:
                attr.dtype = data[attr.name].dtype
                print(f'Attribute Data Type:{attr.dtype}')
                attr.type = self.find_attr_type(data[attr.name], attr.dtype)
                print(f'Attribute Type:{attr.type}')
                if attr.type is DataType.DATE.value:
                    data[attr.name] = data[attr.name].apply(lambda x: x if pd.isna(x) else parse(x))
                    attr.dtype = data[attr.name].dtype

        # For semi-structured data type
        elif type is "semi-structured":
            self.attributeInfo = list()

        # For unstructured data type
        elif type is "unstructured":
            self.attributeInfo = list()

    @staticmethod
    def isdate(date_values):
        """

        :param date_values:
        :return:
        """
        is_date_bool = list()
        for date in date_values.iteritems():
            try:
                parse(date[1])
                is_date_bool.append(True)
            except ValueError:
                is_date_bool.append(False)
        ret = True if sum(is_date_bool) > len(is_date_bool) / 2 else False
        return ret

    # Below method finds the data type of the attributes
    @staticmethod
    def find_attr_type(data, dtype, threshold=5, length_threshold=50):
        """

        :param data:
        :param dtype:
        :param threshold:
        :param length_threshold:
        :return:
        """
        num_rows = float(data.size)
        unique_values = data.unique().tolist()
        unique_proportion = (float(len(unique_values)) / num_rows) * 100
        dtype = str(dtype)

        if DataType.FLOAT.value in dtype or DataType.INT.value in dtype:
            if unique_proportion < threshold:
                type = DataType.NOMILAL.value

            else:
                type = DataType.NUMERIC.value

        elif DataType.OBJECT.value in dtype:
            max_length = data[~data.isna()].map(len).max()
            if DataSetInfo.isdate(data[~data.isna()][0:10]):
                type = DataType.DATE.value

            elif unique_proportion < threshold:
                type = DataType.NOMILAL.value

            elif max_length < length_threshold:
                type = DataType.STRING.value
            else:
                type = DataType.TEXT.value

        elif DataType.BOOL.value in dtype:
            type = DataType.NOMILAL.value

        return type

    def populate_attribute(self, data, type):
        """

        :param data:
        :param type:
        :return:
        """
        if type not in self.DATA_TYPES:
            raise InvalidDataTypeException("Provided Data Type : {} not "
                                           "supported".format(type))

        # For structured datatype
        elif type is "structured":
            for attr in self.attributeInfo:
                print(f'DataSet Info Attr:{attr}')
                print(f'DataSet Info Attr Name:{attr.name}')
                attr.populate(data[attr.name])

        # For semi-structured data type
        elif type is "semi-structured":
            print("Populate method for semi structured")

        # For unstructured data type
        elif type is "unstructured":
            print("Populate method for unstructured")

        else:
            return

    # populates multi variate metric analysis
    def populate_metric(self):
        """

        :return:
        """
        return