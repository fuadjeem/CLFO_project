# CLFO_project

- instaling Open CV library
- creating functions for image resize, load, transform color, save with aim to better understand problem
- selecting areas that are connected to illness levels
- simulate ml algorithms to check mask importance
- simulate deeep learning to check mask importance
- problem - to much time for creating masks on 6000 images
- selecting equal image sets for each level
- asigning each image to corespodent level
- princips of PyTorch functioning (gradients, forward & backward pass, linear regression, logistic regression, sigmoid functions, ReLU, softmax, cross entreopy, neural networks - nonlinearity)
- 256x256 gray images (one chanel) 1200 for each class
- creating feedForward neural network model on 256x256 gray images
- creating convolutional neural network model on 256x256 gray images
- transfer learning by preaperd RESNET model with last fully connected layer transformation. 
- a) 140 images of right eye per class has been used as a training model that return 40% accuracy on tested data set
- b) left eye images have been mirror inverted, which almost doubled complete data set returning 50% accuracy
 
Proposal for the next steps
- make data set larger by including upside down inverted images which will include croping images with the nocth.
- binarysplit data set by label zero and others (this will enlarge complete data set and make decrese number of classes which will ressult in mich better accuracy)
- images could be filterd to enhance regions where changes caused by illnes occurs (this will take a huge amount of time)
- transfer learning based on different and approprite pretrained NET model



