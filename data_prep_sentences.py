'''
Same as data_prep.py, but instead of preparing tensors, returns
a list of the raw sentences and associated labels

If datasets package works, use that instead
'''
# from datasets import load_dataset


# class DataRawLoader():
#     def __init__(self):
#         self.dataset = load_dataset('ag_news')
    
#     def _get_data(self, data):
#         texts = data['text']
#         labels = data['label']

#         return texts, labels

#     def get_train(self):
#         return self._get_data(self.dataset['train'])

#     def get_test(self):
#         return self._get_data(self.dataset['test'])

import pickle


class DataRawLoader():
    def __init__(self):
        # self.dataset = load_dataset('ag_news')
        pass
    
    def _get_data(self, base_dir='data/test'):


        with open(f'{base_dir}/texts.pkl', 'rb') as f:
            texts = pickle.load(f)
        with open(f'{base_dir}/labels.pkl', 'rb') as f:
            labels = pickle.load(f)
        print(texts[:2])
        return texts, labels

    # def get_train(self):
    #     return self._get_data(self.dataset['train'])

    def get_test(self):
        # return self._get_data(self.dataset['test'])
        return self._get_data(base_dir='data/test')
