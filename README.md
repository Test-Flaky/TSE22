## Test Flakiness Across Programming Languages

This repository contains a dataset of flaky tests associated with GitHub projects written in five different programming languages.

This dataset is the basis of the paper<br> 
&nbsp;&nbsp;&nbsp;&nbsp;**Test Flakiness Across Programming Languages**,<br>
which investigates the phenomenon of flakyness across programming languages.

This repository is organized as follows:<br>
/<br>
├── data/&nbsp;&nbsp;&nbsp;&nbsp;<= where the spreadsheet with the data can be found<br>
└── src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<= where the script to extract the issues can be found<br>

## Script (under /src)

We used [a script in Python](https://github.com/Test-Flaky/Flakiness/blob/main/src/Script-flakiness.py) to access issues related to flakiness. We used the GitHub API for that. The script uses the following filters for issues:

1. From projects written in C, Go, Python, Java, or JavaScript;
2. Use keywords "Flaky" *and* "Test";
3. Contain label "bug";
4. Status is "closed".

The script caps results at 300 isues per programming language. The output is a spreadsheet (.csv) with 1500 issues, 300 issues for each programming language.

-------------------------------------------------------------------------------------------------------------------------------------------------------

## Spreadsheet (under /data)

<!---
This dataset is categorized into causes and the Flaky test solution is stored [here](https://github.com/Test-Flaky/ICSE22/tree/main/data).
These Root Cause involved a total of 421 open source GitHub projects written primarily in four programming languages: C, Go, Java, JavaScript and Python.
--->

<!---
The anonymous dataset contains 1.500 issues which were extracted from projects stored on GitHub through the Script.
--->

A flaky test is associated with (1) a **root cause** that explains the reason for flakiness and (2) a **fix strategy** that explains how developers addreessed flakiness. We aimed to classified 100 root causes and fix strategy for each language. We classified a total of **591 root causes** and **500 fix strategies**.

The data is available in [a spreadsheet](https://github.com/Test-Flaky/ICSE22/blob/main/data/DataBase_GitHub.xlsx) with data organied in different tabs:<br>
&nbsp;&nbsp;&nbsp;&nbsp;(1) Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;(2) Problem<br>
&nbsp;&nbsp;&nbsp;&nbsp;(3) Solution<br>
  
We elaborate in the following the structure of each tab.

**Data**

This tab contains the Issues data and is organized in columns.

* ID: Unique identifier for each Issue.
* Repository / Project: Name of the repository registered on GitHub for that Issue.
* Language: Language-specific to each Issue.
* Status: Defines whether Flaky is True ("T"), False Positive ("F"), or Not determined ("ND").
* Label: Label registered in the Issue.
* Issue status: Defines the status found in the Issue.
* Year: Year the Issue was created.
* URL Issue: Save the issues link.
* M1: Number of days until issue is closed.
* M2: Number of comments until issue is closed.
* Domain: Application Domain.

We also divided the spreadsheet into Problem and Solution where each one has:
* Category: Defines which category (either problem or solution).
* Reviewers: This column shows which author has reviewed that issue.
* Description: It is an excerpt from the issue that helps to support the decision to choose the category.

**Problem**

This tab is the reference that supported the authors in making a decision for which category of problems issues should be categorized.
This tab is organized with the columns as follows:
* References: Previous work that reported the problem category.
* Root Cause Category: Name used by previous authors for a given problem category.
* Description: Description found in the works.
* Support: Amount of times this Root Cause Category occurred in the "Data" tab.
* [n]: Number of times that Root Cause Category occurred in reference works [n].

Finally, in line 17 is the sum of each column.

**Solution**

This tab is the reference that supported the authors in making a decision for which category of problems issues should be categorized.
This tab is organized with the columns as follows:

* Support: Number of times the category occurred in the "Date" tab.
* References: What previous work has reported this category of solution.
* Root Cause Category: Problem category belonging to this solution category.
* Fix Strategy Category: Solution category.
* Reported Works: Previous jobs that reported the solution category.
* Killer Description: Excerpts from the works that support the decision.
* Example: Practical example for the solution category.

Line 27 of this tab contains the sum of supports.
Starting on line 29, we have the categories of solutions that we did not find in our data.

-------------------------------------------------------------------------------------------------------------------------------------------------------
## Research Questions

To answer survey questions, you need to refer to the sheet for more details. Where it will be possible to view the RQ's and their tables with the respective results.

-------------------------------------------------------------------------------------------------------------------------------------------------------
**Citation:**
Barbosa, K., Ferreira, R., Pinto, G., d'Amorim, M., & Miranda, B. (2023). *Test Flakiness Across Programming Languages*. IEEE Transactions on Software Engineering, 49(4), 2039–2052. [https://doi.org/10.1109/TSE.2022.3208864](https://doi.org/10.1109/TSE.2022.3208864)

#### BibTeX Entry

```bibtex
@article{10.1109/TSE.2022.3208864,
  author = {Barbosa, Keila and Ferreira, Ronivaldo and Pinto, Gustavo and d'Amorim, Marcelo and Miranda, Breno},
  title = {Test Flakiness Across Programming Languages},
  year = {2023},
  issue_date = {April 2023},
  publisher = {IEEE Press},
  volume = {49},
  number = {4},
  issn = {0098-5589},
  url = {https://doi.org/10.1109/TSE.2022.3208864},
  doi = {10.1109/TSE.2022.3208864},
  journal = {IEEE Trans. Softw. Eng.},
  month = {apr},
  pages = {2039–2052},
  numpages = {14}
}
-------------------------------------------------------------------------------------------------------------------------------------------------------
