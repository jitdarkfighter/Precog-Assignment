
#### **Tasks done** 
- **Task 0** - Dataset Generation
  Dataset generation with Pillow and numpy

- **Task 1** - Classifying 100 words
  Used CNN

- **Task 2** - Getting the text in easy and hard images
  Used CRNN

- **Task 3-(Bonus)** - Getting the text in bonus images
  Used CRNN with attention instead of CTC. Implemented attention, **unable to finish implementing decoder.** Will be completed in the future.


```
Precog-Assignment/
├── README.md                          # This file
├── Task0/                             # Dataset generation scripts
│   ├── ai_wordlist.txt               # Word list for generating text
│   ├── easy_imgs.py                  # Generate simple CAPTCHA images
│   ├── hard_imgs.py                  # Generate complex CAPTCHA images
│   └── bonus_imgs.py                 # Generate bonus task images
├── Task1/                            # CNN Classification (Task 1)
│   ├── final_cnn.ipynb              # Main notebook for CNN implementation
│   ├── Report.md                     # Task 1 specific report
│   ├── smolCNN_model.pth           # Trained model weights
│   ├── captcha_images.zip           # Generated dataset
│   ├── captcha_images/              # Extracted dataset
│   │   ├── train/                   # Training images
│   │   │   ├── easy/
│   │   │   └── hard/
│   │   └── test/                    # Test images
│   │       ├── easy/
│   │       └── hard/
│   └── Dataset-Generation/          # Dataset generation scripts
├── Task2/                           # CRNN Implementation (Task 2)
│   ├── smolCRNN.ipynb              # Small CRNN model
│   ├── DeepCRNN.ipynb              # Deep CRNN model
│   ├── report.md                    # Task 2 specific report
│   ├── smolCRNN_model.pth          # Small model weights
│   ├── DeepCRNN_model.pth          # Deep model weights
│   ├── captcha_images.zip          # Dataset for Task 2
│   ├── wordlist_captcha_images/    # Word-based dataset
│   └── Dataset-Generation/         # Generation scripts
├── Task3-Bonus/                    # Attention-based Model (Bonus Task)
│   ├── encoder.py                  # CNN Encoder implementation
│   ├── decoder.py                  # RNN Decoder implementation
│   ├── attention.py                # Attention mechanism
│   ├── report.md                   # Task 3 specific report
│   ├── captcha_images/            # Bonus task dataset
│   ├── wordlist_captcha_images/   # Additional datasets
│   └── Dataset-Generation/        # Generation scripts
└── Notebooks/                     # Development notebooks
    ├── captcha_image_generation.ipynb
    ├── cnn.ipynb
    ├── easy_imgs.ipynb
    ├── hard_imgs.ipynb
    ├── only_hard.ipynb
    └── bonus_imgs.ipynb
```

```bash
pip install -r "requirements.txt"
```

For each ipynb file in the Task Folder, there is an option to load the saved model and execute it.

The DeepCRNN model was too big to upload on gihub, therefore will be uploaded to huggingface.
https://huggingface.co/jitdarkfighter/DeepCRNN/tree/main

