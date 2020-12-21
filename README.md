# Well Log Viewer
This is a package for you to visualize your well log data. This could visualize your log data from LAS file or other ASCII format. If you are new in python and would like to have a good tools to visualize your well log or just simply too lazy to write a code, this might be useful for you. Reads the las files using [lasio](https://lasio.readthedocs.io/en/latest/installation.html) and visualizes using [bokeh](https://bokeh.org/). 

I will keep updating this package day to day, please keep checking. Next update will include the visualization of lithology, formation well top and finally wrap the package at pip so you can easily use this in the future by installing the pip instead of copying or downloading the py file. If any of you want to fork this repository I kindly appreciate that.


![alt text](https://github.com/panjoel4/WellLogViewer/blob/master/Files/image.png?raw=true)


## Requirements
- [lasio](https://lasio.readthedocs.io/en/latest/installation.html) <br/>
- [bokeh](https://bokeh.org/) <br/>
- [numpy](https://numpy.org/) <br/>


## How to use
Copy the LogViewer.py file to your working directory and then import the file to your code.

<pre><code>from LogViewer import *

wells=lasViewer('yourwell.las') #Load las file
</code></pre>

## User Guide
View the [online documentation](https://github.com/panjoel4/WellLogViewer/tree/master/User%20Guide)

## Output Samples
The ipynb files could not load the html produced by the code, however you could see the actual output of the codes at [files](https://github.com/panjoel4/WellLogViewer/tree/master/Files) folder.
