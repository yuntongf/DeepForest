## Progress:

* Successfully run Deep Tree model on local environment using trained boston-specific model and a single jpeg picture as input

* The image output of the model is encoded in base64. This can be tested by running the deep_tree.py script, and the print statement in the last line of the script will output the base64 encoding of the output picture.

* Set up a Flask app in the api.py file. The app can currently render a plain html page with the text "Hello World"

## Current Issues: 

* Calling deep_forest() in api.py will give an NSException; however, running deep_forest() seperately in deep_tree.py gives the correct output.
    * error log: 
        Terminating app due to uncaught exception 'NSInternalInconsistencyException', reason: 'NSWindow drag regions should only be invalidated on the Main Thread!'

## Features to be implemented:

* Dnamically update the web page based on the input data

* Allow file upload in the web page as input to the model

* Migrate html file to React and connect the backend with React

* Add more stats and display more output of the DeepForest model on the web page

## Question:

* run model on GPU?


