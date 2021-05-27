# Color Detector
## An awesome OpenCV project

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

In this project I built an application through which we can automatically get the name of the color by double clicking on it. For this, I used a dataset that contains the color name and its RGB values. The method used to find the color name was to calculate the distance from each color and find the shortest one.


![Feedback Classifier Screen Shot][product-screenshot]
![Feedback Classifier Positive Prediction Screenshot][product-positive-screenshot]
![Feedback Classifier Negative Prediction Screenshot][product-negative-screenshot]



Procedure:

* I used a dataset of colors with their name and RGB values.
* Used Argument Parser from argparse to take image from the user in the command line
* Read the image using cv2.imread()
* Read the dataset and indexed it
* Set a mouse callback event on the image window
* Define the draw function to calculate the RGB values of the pixel that was clicked on
* Define the getColorName function to calculate the distance and return the color name
* Display the image on the window and surround the clicked pixel with a rectangle and use text to display the color name and its RGB values


### Built With

This project was built entirely on Python.

* [Python](https://www.python.org)

### Libraries Used

* [scikit-learn](https://scikit-learn.org/stable/)
* [random](https://docs.python.org/3/library/random.html)
* [json](https://docs.python.org/3/library/json.html)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)

### Machine Learning Models Used:

I trained and evaluated the following Machine Learning models for this project:

* [SVM](https://scikit-learn.org/stable/modules/svm.html)
* [DecisionTrees](https://scikit-learn.org/stable/modules/tree.html)
* [NaiveBayes](https://scikit-learn.org/stable/modules/naive_bayes.html)
* [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)



<!-- CONTACT -->
## Contact

Your Name - [@puneet_arora_14](https://twitter.com/puneet_arora_14)

Project Link: [https://github.com/apuneet839/Feedback_Classifier](https://github.com/apuneet839/Feedback_Classifier)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://www.linkedin.com/in/puneet-arora-1401
[product-screenshot]: images/Feedback_classifier_default.png
[product-positive-screenshot]: images/Feedback_classifier_positive.png
[product-negative-screenshot]: images/Feedback_classifier_negative.png
