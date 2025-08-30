## Problem 1
- Tested first with a model with 6m params - overfitted badly. Made the model memorize the images rather than solve the problem
    - Due to low data. 100 classes, 5 images per class for training, 2 per class for testing
    - Too many params for too less data

- Tested with increased data on the 6m parameter model -> again overfitting

- Got a first working version after using 50 images per class for training with 500k params
