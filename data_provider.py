class DataProvider:
    def __init__(self):
        self.data = []

    def get_data(self):
        return self.data

    def update_data(self, new_data):
        self.data = new_data

data_provider = DataProvider()
