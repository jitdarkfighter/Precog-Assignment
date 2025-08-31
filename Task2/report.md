# Problem 2
- A CNN can only classify images. If we were to make each word a dictionary into a class, it will be 9m classes. But still isnt enough since there can be random meaningless words of any length.

- So i read this paper on CRNN. https://arxiv.org/abs/1507.05717
    - This paper suited our use case.
    - Like the model used in problem 1, it has a convolution layer to get the spacial features. The convolution layers here also resemble the VGG architecture.
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
    
    - Input size can be reshaped like the paper before passing it onto the model. Because of this my RNN input size is `512*11` dimensions, whereas in the paper is just 512. And that's also why in the paper the input to the lstm is `512*1*width`. This doesn't have too much issues just that the training wastes too many resources.

- Articles Reffered too
    - https://medium.com/@piyushkashyap045/understanding-pytorch-autograd-a-complete-guide-for-deep-learning-practitioners-f5dd1f43b417
    - https://pub.towardsai.net/optical-character-recognition-ocr-with-cnn-lstm-attention-seq2seq-538a57404de3
    - https://medium.com/@anishnama20/understanding-bidirectional-lstm-for-sequential-data-processing-b83d6283befc


- Observations
    - batch size 32. Tried with 8, not much improvement. Decided to stick to 32 since others took too much time to train
    - after training on random generated words (50k images), now validating with the word list dataset
        - smolCRNN trained on the Wordlist_dataset itself
            - 100% accuracy on train
            - 96% accuracy on test 
            - most likely overfitted. So generated random datasets and tested again.       

        - smolCRNN gets 
                - Accuracy: 93.19% (46595/50000)
                - Accuracy: 84.04% (12606/15000)
                - Wordlist_captcha dataset
                    - Accuracy: 74.17% (6379/8600) - wordlist train
                    - Accuracy: 76.12% (1964/2580) - wordlist train
            -  Increasing epochs from 15 to 30 did nothing.
            - The low accuracy also means the smolCRNN model previously overfitted.
        
        - DeepCRNN gets (19M params)
                - trained for 15 epochs
                    - 90% accuracy on train set
                    - 89% accuracy on test set
                    - Testing on Wordlist_captcha dataset
                        - Accuracy: 91.60% (7880/8600) - wordlist train part
                        - Accuracy: 92.44% (2383/2580) - wordlist test part

                - trained for 30 epochs
                    - Accuracy: 96.12% (48060/50000) - train
                    - Accuracy: 94.39% (14158/15000) - test
                    - Testing on Wordlist_captcha dataset
                        - Accuracy: 95.20% (8187/8600) - wordlist train part
                        - Accuracy: 95.54% (2465/2580) - wordlist test part

    - Initially I noticed the wordlist accuracy was low. This was because I accidently didn't generate captcha's with numbers and the wordlist dataset had words with numbers like "AIword1" to "AIword10". So I saw only 80% accuracy. Removing the numbers increased accuracy to 95%. Didn't retrain as it would take long, but it will surely work on numbers if needed.


- Areas of Improvement:
    - The model can be made more parameter efficient. The DeepCRNN model was implemented as it is from the paper to test accuracy. It has too large parameters. 
    - Accuracy could be made higher by reducing batch_size and training for more epochs.
    - Forgot to add numbers to the train dataset, maybe could try that later. Training takes hours.

    - Solution:
        - If time permits, Implement a model between DeepCRNN and smolCRNN with batch_size 8 or 4 for 100 epochs and then test the accruary.