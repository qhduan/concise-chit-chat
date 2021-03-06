# CONCISE CHIT CHAT

TO BE FIXED: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zixia/concise-chit-chat/blob/master/Concise_Chit_Chat.ipynb)

Book Chapter: Concise Chit Chat - <https://zixia.github.io/concise-chit-chat/>

## USAGE

```shell
make install    # install python dependencies
make train      # train the model(dataset will be downloaded automatically)
make board      # monitor & analyse train process
make chat       # chat with it!
```

### Use Nvidia Docker

```shell
make docker   # this will get into the tensorflow/tensorflow:latest-py3-gpu docker container
make board &  # open tensorboard at http://localhost:6006
make train
make chat
```

## DEVELOP

### Open VSCode

```shell
make code
```

### Download Original Corpus Dataset and Preprocdess Them

```shell
make download     # download original dataset
make dataset      # generate the formated dataset
```

## TURORIAL

- [简单粗暴TensorFlow | A Concise Handbook of TensorFlow](https://tf.wiki)
- [Quick guide to run TensorBoard in Google Colab](https://www.dlology.com/blog/quick-guide-to-run-tensorboard-in-google-colab/)

## SEE ALSO

- [Understand the Difference Between Return Sequences and Return States for LSTMs in Keras](https://machinelearningmastery.com/return-sequences-and-return-states-for-lstms-in-keras/)
- [Practical Guide of RNN in Tensorflow and Keras Introduction](https://paulx-cn.github.io/blog/4th_Blog/)
- [Sequence Tagging with Tensorflow](https://guillaumegenthial.github.io/sequence-tagging-with-tensorflow.html)
- [Design and build a chatbot using data from the Cornell Movie Dialogues corpus, using Keras](https://github.com/sekharvth/simple-chatbot-keras)
- [PyTorch Chatbot Tutorial](https://pytorch.org/tutorials/beginner/chatbot_tutorial.html)
- [A ten-minute introduction to sequence-to-sequence learning in Keras](https://blog.keras.io/a-ten-minute-introduction-to-sequence-to-sequence-learning-in-keras.html)
- [Use tf.clip_by_global_norm for gradient clipping](https://stackoverflow.com/a/44798131/1123955)
- [Understanding Python's "with" statement](http://effbot.org/zone/python-with-statement.htm)

## AUTHOR

[@zixia](https://github.com/zixia) [Huan LI](https://linkedin.com/in/zixia) \<zixia@zixia.net\>

<a href="http://stackoverflow.com/users/1123955/zixia">
  <img src="http://stackoverflow.com/users/flair/1123955.png" width="208" height="58" alt="profile for zixia at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for zixia at Stack Overflow, Q&amp;A for professional and enthusiast programmers">
</a>

## COPYRIGHT & LICENSE

- Code & Docs © 2018 - now Huan LI \<zixia@zixia.net\>
- Code released under the Apache-2.0 License
- Docs released under Creative Commons
