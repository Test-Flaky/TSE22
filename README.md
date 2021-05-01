This repository contains the dataset of flaky tests for the "**Test Flakiness Across Programming Languages**" paper.

## Script for data capture

A script is written in Python [here](https://github.com/Test-Flaky/Flakiness/blob/main/src/Script-flakiness.py) was used to connect to the GitHub API, returning issues according to the filters:

1. Issues only for the Go, Python, Java, and JavaScript programming languages.
2. Search for content in issues by keywords "Flaky" and "Test".
3. Only Issues with label "bug".
4. Only Issues with "closed" status.

We configured the results to return a spreadsheet (.csv) with 1200 Issues.

-------------------------------------------------------------------------------------------------------------------------------------------------------

## Anonymized Dataset

The anonymous dataset contains 1.200 issues which were extracted from projects stored on GitHub through the Script.

The data is organized in tabs within the spreadsheet as we will explain below:

**Aba Data**

The "Data" tab contains the Issues data and is organized in columns.

* ID: Unique identifier for each Issue.
* Repository / Project: Name of the repository registered on GitHub for that Issue.
* Language: Language-specific to each Issue.
* Status: Defines whether Flaky is True ("T"), False Positive ("F"), or Not determined ("ND").
* Label: label registered in the Issue.
* Issue status: defines the status found in the Issue.
* Year: Year the Issue was created.

-------------------------------------------------------------------------------------------------------------------------------------------------------

This dataset is categorized into causes and the Flaky test solution is stored [here](https://github.com/Test-Flaky/OOPSLA21/tree/main/data).
These Root Cause involved a total of 325 open source GitHub projects written primarily in four programming languages: Go, Java, JavaScript and Python.

We classify a number of root causes (472) and solutions (389).

#### This dataset contains the following cause classifications for Flaky Tests

![myimage-alt-tag](https://github.com/Test-Flaky/OOPSLA21/blob/main/Image/cause.png)


#### This dataset contains the following fix classifications for Flaky Tests

![myimage-alt-tag](https://github.com/Test-Flaky/OOPSLA21/blob/main/Image/Fix.png)


We believe that the data set will be useful for the research community, not only to conduct research on various aspects of Flaky tests and their root causes but also for a general understanding of behavior and how it is possible to resolve such instability in these tests.
