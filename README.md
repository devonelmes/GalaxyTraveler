Team: Devon Elmes, Lang Cao, Melissa Cote

This is our final project for COP3530 - Data Structures and Algorithms, Fall 2025.

Our program parses the data and stores it in an unsorted container. Upon running,
it displays the UI window and then prompts the user for input, to find the k 
(specified by user) closest galaxies. It then uses two different search algorithms
(heapsort and quickselect) to find them and displays it to the user.

Installing dependencies:
> pip3 install customtkinter
> pip3 install pillow

Our dataset can be found here: https://ned.ipac.caltech.edu/Library/Distances/

Space image source: https://opengameart.org/content/seamless-space-backgrounds

Instructions: Run the program and navigate to the UI pop-up window. Input a valid integer,
and click Submit.

This will cause the program to run through both search methods and display 
the results (twice, once with each method) and the time each algorithm took. You may scroll 
through the results in the frame where they are displayed. To the right, an animation will 
play, displaying a node for each galaxy found. If you wish to search for a different 
number of galaxies, simply input another valid integer and click Submit. Do this as many 
times as you please. To end the application, simply close the window.
