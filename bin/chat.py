'''train'''
import tensorflow as tf

from chit_chat import (
    ChitChat,
    DataLoader,
    Vocabulary,
    DONE,
    GO,
)

tf.enable_eager_execution()


def main() -> int:
    '''chat main'''
    data_loader = DataLoader()
    vocabulary = Vocabulary(data_loader.raw_text)

    print('Dataset size: {}, Vocabulary size: {}'.format(
        data_loader.size,
        vocabulary.size,
    ))

    chitchat = ChitChat(vocabulary)
    checkpoint = tf.train.Checkpoint(model=chitchat)
    checkpoint.restore(tf.train.latest_checkpoint('./data/save'))
    print('checkpoint restored.')

    return cli(chitchat, vocabulary=vocabulary, data_loader=data_loader)


def cli(chitchat: ChitChat, data_loader: DataLoader, vocabulary: Vocabulary):
    '''command line interface'''
    index_word = vocabulary.tokenizer.index_word
    word_index = vocabulary.tokenizer.word_index

    print('GO: %d, DONE: %d' % (word_index[GO], word_index[DONE]))

    while True:
        query = input('> ').lower()
        if query == 'q' or query == 'quit':
            break
        query = data_loader.preprocess(query)
        query = '{} {} {}'.format(GO, query, DONE)
        # Evaluate sentence
        query_sequence = vocabulary.texts_to_padded_sequences([query])[0]
        response_sequence = chitchat.predict(
            query_sequence,
            # temperature=0.3,
        )

        # Format and print response sentence
        response_word_list = [
            index_word[indice]
            for indice in response_sequence
            if indice != 0 and indice != word_index[DONE]
        ]

        # import pdb; pdb.set_trace()
        print('> {}'.format(' '.join(map(str, query_sequence))))
        print('{} <'.format(' '.join(map(str, response_sequence))))
        print('{} <'.format(' '.join(response_word_list)))
        print('\n')


main()
