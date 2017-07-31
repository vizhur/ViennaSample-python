#  ![vienna icon](Images/vienna_icon.png) Getting Started

This project helps get started a Vienna project.  It contains example code showing how to train and score models while taking advantage of the Vienna system in both Python and PySpark.

In general, your Vienna workflow will be:
* Set up your execution environments
* Connect to and wrangle your data sources
* Implement and execute your training experiments
* Determine which experiments result in the best result
* Implement your scoring code
* Operationalize your scoring code and models

## Setting up your Environments

Under Environments you can set up all of your local and remote compute contexts and any required dependencies.  This project already contains environments for executing your experiments locally on your native OS using Python or on a local docker image using PySpark.    Local native and local docker configurations are already set up for you in this project and a template is provided for a remote Data Science Virtual Machine (DSVM).  You will need to provide details in the DSVM template in order to use this context.

A conda file including typical dependencies required when using Vienna is also provided.

## Data
Under Data you will specify your data sources and use Vienna's data preparation tools to wrangle local and remote data sources as necessary for your data science experimentation needs.  You can then use these data sources in your experiment.

## Notebooks
Notebooks allows you to easily get started with your experimentation.  As with all Vienna experimentation, your work is tracked so you can see exactly how your changes impact your results.

## Run History
In Run History you can see all of the runs of the project organized by starting point.  Here you can customize your reports to see the metrics that matter most to you.  You can drill down to individual runs to see the detailed output of your experiments.  When you  and get to the source code that was executed to create that output. You can even revert to the source of any run to continue experimentation from that point.

## Asset Explorer
In Asset Explorer you will see all the objects you have promoted from your Run History.  These objects are now **assets** that you can access from your code and operationalize.  To load an asset use the <insert asset load api here> method.  Click the "register" button next to an asset to learn how to operationalize assets for production.

## Operationalization
TBD

## Files
In the files section you can browse all of the content files of your project.

