So we cant use the DeepCRNN model (CRNN + CTC) from Task2 here since ctc assumes left to right order.
I tried training it, but then the loss was flatlining.

CTC will try to fit, squish the feature sequence but wont be able to reverse it. Hence may work partially but not acceptable accuracy.

So we need a seq2seq model. or anything that makes use of attention
So im thinking about replacing it with a decoder maybe and definitely resizing the input. Basically CRNN will be the encoder.<br>
***This is where i realise i have re-invented a seq2seq model***

We can follow the
    - Show, Attend and Tell paper : https://arxiv.org/abs/1502.03044
    - Show, Attend and Read paper : https://arxiv.org/abs/1811.00751


### Encoder
    - The encoder will be A CNN which gets the feature maps. This helps get the spacial features of the image.
    - Unlike the mistake in Task2, we scale the image to `32x64` before passing it onto the CNN.
    - The CNN is build following the VGG architecture.

### Additive attention
    - We use additive attention which was introduced by `Dzmitry Bahdanau`.
    - How it works is, using the feature map, we flatten the feature map. (b,c,h,w) -> (w, b, c*h). The width is considered the time index while passing this sequence to an rnn.
    - There is a MLP layer which make.

    **Refer to pdf Task3 report.**

