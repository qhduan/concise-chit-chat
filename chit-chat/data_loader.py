'''
data loader
'''
import re
from typing import (
    # Any,
    List,
    Tuple,
)

import numpy as np

from config import (
    GO,
    DONE,
)

DATASET_URL = 'https://github.com/zixia/concise-chit-chat/releases/download/v0.0.1/dataset.txt.gz'
DATASET_FILE_NAME = 'concise-chit-chat-dataset.txt'


class DataLoader():
    '''data loader'''

    def __init__(self) -> None:
        # path = tf.keras.utils.get_file(DATASET_FILE_NAME, origin=DATASET_URL)

        # XXX
        path = './data/dataset.txt'
        # print('path', path)

        with open(path, encoding='iso-8859-1') as f:
            self.raw_text = f.read().lower()

        # line_list = self.raw_text_to_line_list(self.raw_text)

        # XXX
        # print('raw_text', raw_text.split('\n'))

        self.queries, self.responses \
            = self.parse_raw_text(self.raw_text)

    def get_batch(
            self,
            batch_size=32,
    ) -> Tuple[List[List[str]], List[List[str]]]:
        '''get batch'''
        # print('corpus_list', self.corpus)
        batch_indices = np.random.choice(
            len(self.queries),
            size=batch_size,
        )
        batch_queries = self.queries[batch_indices]
        batch_responses = self.responses[batch_indices]

        return batch_queries.tolist(), batch_responses.tolist()

    def parse_raw_text(
            self,
            raw_text: str
    ) -> Tuple[List[List[str]], List[List[str]]]:
        '''doc'''
        query_list = []
        response_list = []

        for line in raw_text.strip('\n').split('\n'):
            query, response = line.split('\t')
            query_list.append('{} {} {}'.format(GO, query, DONE))
            response_list.append('{} {} {}'.format(GO, response, DONE))

        return np.array(query_list), np.array(response_list)