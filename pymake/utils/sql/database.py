"""
pymake
-------------------------------
 - Eugenio Marinetto
 - nenetto@gmail.com
-------------------------------
Created 10-05-2018
"""

from abc import ABC, abstractmethod
import pandas as pd
from pymake.utils.common.prettymessaging import PrettyMessaging


class DataBase(ABC):

    def __init__(self, host, port, dbname, user, pwd, verbose=True):
        super().__init__()
        self._connection = None
        self._connected = False
        self._verbose = verbose

        self.pm = PrettyMessaging('DataBase')

        # Database connection info
        self._host = host
        self._port = port
        self._dbname = dbname
        self._user = user
        self._pwd = pwd

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    def get_query(self, query, close=True):

        self.connect()

        if self._connected:
            df = pd.read_sql(query, self._connection)
        else:
            raise (Exception('[DataBase]: Data Base not connected'))

        if close:
            self.disconnect()

        return df

    def get_query_from_file(self, sqlfile, parameters=None, save_file=None, close=True):

        # Read the sql file
        with open(sqlfile, 'r') as f:
            query = f.read()

        # Place parameters on query
        if parameters is not None:
            for k, v in parameters.items():
                query = query.replace(k, str(v))

        data = self.get_query(query, close)

        if save_file is not None:
            data.to_csv(save_file, index=False)

        return data