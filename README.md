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


![Color Detector Blue][color_detector_blue]
![Color Detector Lust][color_detector_lust]
![Color Detector Green][color_detector_green]



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

* [argparse](https://docs.python.org/3/library/argparse.html)
* [OpenCv](https://opencv.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* 

<!-- CONTACT -->
## Contact

Your Name - [@puneet_arora_14](https://twitter.com/puneet_arora_14)

Project Link: [https://github.com/apuneet839/Feedback_Classifier](https://github.com/apuneet839/Feedback_Classifier)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://www.linkedin.com/in/puneet-arora-1401
[color_detector_bluet]: images/color_detector_blue.png
[color_detector_lust]: images/color_detector_lust.png
[color_detector_green]: images/color_detector_green.png
