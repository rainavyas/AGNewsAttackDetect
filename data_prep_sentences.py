'''
Same as data_prep.py, but instead of preparing tensors, returns
a list of the raw sentences and associated labels
'''
from datasets import load_dataset


class DataRawLoader():
    def __init__(self):
        self.dataset = load_dataset('ag_news')
    
    def _get_data(self, data):
        texts = data['text']
        labels = data['label']

        return texts, labels

    def get_train(self):
        return self._get_data(self.dataset['train'])

    def get_test(self):
        return self._get_data(self.dataset['test'])
