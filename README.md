# YDS Project : audio processing 

Impelementation of audio processing related models

**Note**: 
- For those who are interested in this project, please read the Deepmind and PixelRNN posts below first. It describes basic stuff you need to know to do audio processing.

- Then, read the following two papers. 

- Join our discussion [here](https://yds.slack.com/messages/wavenet/)!

- For those who are new to RNN, here are some resources. [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), [How to implement a recurrent neural network Part 1](http://peterroelants.github.io/posts/rnn_implementation_part01/)

paper1 : [Wavenet](https://arxiv.org/pdf/1609.03499.pdf)

Deepmind Blogpost : [Wavenet blogpost](https://deepmind.com/blog/wavenet-generative-model-raw-audio/)

paper2 : [Generating Sequences With Recurrent Neural Networks](https://arxiv.org/pdf/1308.0850v5.pdf)

PixelRNN review : [Magenta Review](https://github.com/tensorflow/magenta/blob/master/magenta/reviews/pixelrnn.md)

### Sound-RNN
- Yutaro Yamada
- Kshitijh Meelu
- Ethan Weinberger

### CharRNN

- Krishnan Srinivasan
- Lincoln Swaine-Moore
- Henry Li

### Log 
Status: [ not started :black_medium_square: | completed :white_check_mark: | in progress :speech_balloon:]

| Task | Status | Deadline | Assigned to |
|------|--------|----------|-------------|
|read paper1 & Deepmind Blogpost|:white_check_mark:|9.30.16|Everyone|
|read PixelRNN review|:white_check_mark:|10.1.16|Everyone|
|preprocess audio data to wavenet data|:white_check_mark:|10.7.16|Krishnan, Sumedh|
|setup an instance on GCP|:speech_balloon:|10.7.16|Kshitijh|
|build ToyModel|:white_check_mark:|10.7.16|Yutaro|
|postprocess wavenet data to audio data|:white_check_mark:|10.7.16|Ethan|
|pipeline preprocessed data into toy model|:speech_balloon:|10.14.16|Krishnan|
|Read/replicate CharRNN, look into text->speech generation|:speech_balloon:|10.14.16|Krishnan, Henry, Lincoln|
