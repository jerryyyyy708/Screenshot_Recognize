# Screenshot_Recognize
## Dataset Information & datasource
This dataset consists of 964 photos, with 500 photos from screenshots (including screenshots from games, animate, message application…etc), and 464 photos from camera. 

To make it easier to be used in model, the photos are resized into 64x64. 
(for your own picture, you can use img_resizer.py to transform it)

The mission is to classify whether the given picture is screenshot or from camera.
#### sample pictures
![](https://i.imgur.com/gVHDet3.jpg)
## Algorithm
**Logistic Regression:** 
Raising the epoch round appropriately can rise the accuracy. If lower epoch rounds are used, we can raise the learning rate to get a better performance

**CNN:**
It already has a great performance with 5 epochs. Using 20 epochs can raise its accuracy to 98.6%, with 100% accuracy predicting camera photos!

## Result
Using KFold cross validation (mean of four folds)
Train size:723  Test size:240  LR: Logistic Regression a: Learning Rate
![](https://i.imgur.com/7xyBbq0.png)

![](https://i.imgur.com/aLISVks.png)



