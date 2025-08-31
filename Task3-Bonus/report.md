So we cant use the DeepCRNN model (CRNN + CTC) from Task2 here since ctc assumes left to right order.
CTC will try to fit, squish the feature sequence but wont be able to reverse it. Hence may work partially but not acceptable accuracy.

So we need a seq2seq model. or anything that makes use of attention
So im thinking about replacing it with a decoder maybe and definitely resizing the input. Basically CRNN will be the encoder.<br>
***This is where i realise i have re-invented a seq2seq model haha***