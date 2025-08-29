# Problem 2
- A CNN can only classify images. If we were to make each word a dictionary into a class, it will be 9m classes. But still isnt enough since there can be random meaningless words of any length.

- So i read this paper on CRNN. https://arxiv.org/abs/1507.05717
    - This paper suited our use case.
    - Like the model used in problem 1, it has a convolution layer to get the spacial features.
    - Then from going from left to right on the feature maps generated, a vector of feature sequences is generated. This means the ith feature vector is the concatenation of the ith column of all maps.
    - This feature sequence is then the input to the Bi-directional LSTM. We need to use an RNN architecture here to get the sequence since the length of the captcha text isnt constant.
    - Then Transcription, it is the process of converting per frame predictions made by the RNN into a label sequence. 
    - Finally loss is calculated using CTC (Conectionist Temporal Classifications), this allows us to calcualate loss for variable length outputs.
        - CTC allows the model to learn alignments between variable-length input sequences and variable-length output sequences without requiring explicit alignment during training
        - It introduces a "blank" token that represents no character, allowing the model to handle repeated characters and variable spacing
        - The CTC loss computes the probability of all possible alignments that could produce the target sequence and sums them up
        - During inference, CTC decoding (like beam search) is used to find the most likely character sequence by removing blanks and consecutive duplicates

- This approach could be made better using architectures like ViT (Vision Transformer) or Swin Transformer. But it is also computationally very expensive and requires too much data. 
    - Note having an attention layer in general could make this much better like additive attention for CNNs. https://arxiv.org/abs/1409.0473 .This was also the paper where the concept of attention was first introduced too :)

- Another intersting approach is to embed word images and text strings in a vector space. So now the OCR problem is converted into a retrieval problem. But then again this isn't feasible since there are infinite number of possibilities of words (words can be meaningless or random).

- How the model can be made better
    - More data
    - More deeper models, that is more parameters.
    - Note: both should be together, one by itself wont work
        - Too much data on a low parameter model will not train well
        - Too less data on a large parameter model will cause it to overfit badly, as experieced before in Task 1.

- Articles Reffered too
    - https://medium.com/@piyushkashyap045/understanding-pytorch-autograd-a-complete-guide-for-deep-learning-practitioners-f5dd1f43b417
    - https://pub.towardsai.net/optical-character-recognition-ocr-with-cnn-lstm-attention-seq2seq-538a57404de3
    - https://medium.com/@anishnama20/understanding-bidirectional-lstm-for-sequential-data-processing-b83d6283befc