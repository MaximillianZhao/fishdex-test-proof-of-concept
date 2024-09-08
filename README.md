# fishdex-test-proof-of-concept
Basic CNN-based fish species image classifier. This is a simple proof of concept and not optimized for high accuracy—intended as an initial test for experimenting with CNN architectures and image classification

### Project brief

Develop a basic Convolutional Neural Network (CNN) model to classify images of different fish species. This project serves as a proof of concept to explore the capabilities of CNNs in image classification tasks and to test initial model architectures.

### Motivation

The motivation behind this project arises from the need for casual fishermen to accurately identify the species of fish they catch. This is crucial for adhering to various regulations that differ by species, including bag limits and size restrictions. Proper identification helps fishermen avoid penalties and, more importantly, contributes to the protection of marine populations and biodiversity by ensuring that fishing practices comply with legal and conservation measures.

### Scope

* Preprocessing images and setting up a data pipeline using Keras ImageDataGenerator
* Building a simple CNN architecture from scratch
* Evaluating model performance and identifying areas for improvement

### Usage

The project uses Jupyter Notebooks for experimentation and analysis. The notebooks include code for training, evaluating, and predicting with the CNN model.

1. Open Notebooks: Launch Jupyter Notebook from the command line:
> ```jupyter notebook```
2. Prepare the data: Place your fish images in the ```data``` directory organized by class subdirectories
> e.g.```data/bream/bream_image1.jpeg```, ```data/snapper/snapper_image2.png```
3. Clean the data: Open ```training_data_preprocessing.ipynb``` and run the cells to clean the data. This should create a new ```processed_data``` with the same structure as the ```data``` directory but containing the cleaned images. Cleaning involves ignoring images of incorrect file formats and file sizes, and removing image backgrounds.
> e.g. The cleaned image under path ```data/bream/bream_image1.jpeg``` will be in ```processed_data/processed_bream/processed_bream_image1.jpeg```
5. Train the model: Open ```model_CNN.ipynb``` and run the cells to train the model on the cleaned data

6. Prepare test data: Place your test fish images in the ```test_data``` folder

7. Predict the model: Open ```test_data_preprocessing_and_testing.ipynb``` and run the cells to clean and resize test fish images, and predict their classes (species).

### Limitations

This classifier is a preliminary test and is not optimized for production use. It lacks extensive data, model tuning, and performance optimizations

### Discussion

Correctly classified 4/5 of unseen fish photos

1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 42ms/step
Image: processed_test_data/no_bg_test_yellowtail_amberjack.png - Predicted Class: silver_trevally

1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step
Image: processed_test_data/no_bg_test_snapper.png - Predicted Class: snapper

1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step
Image: processed_test_data/no_bg_test_silver_trevally.png - Predicted Class: silver_trevally

1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step
Image: processed_test_data/no_bg_test_bream.png - Predicted Class: bream

1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 12ms/step
Image: processed_test_data/no_bg_test_dusky_flathead.png - Predicted Class: dusky_flathead

### Future improvements

* Expand the dataset with more diverse images
* Experiment with different model architectures and hyperparameters
* Additional metrics for evaluation and logging
* Optimize background removal process
* Implement other strategies for classification including data augmentation, and feature extraction and engineering
