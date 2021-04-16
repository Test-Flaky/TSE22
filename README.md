This repository contains the dataset of flaky tests for the "[A Study of Test Flakiness Across Programming Languages](http:/.../A Study of Test Flakiness Across Programming Languages.pdf)"" paper.

## Anonymized Dataset

The anonymous dataset contains 1,291 Issues which were extracted from GitHub through the Script that is stored [here](https://github.com/Test-Flaky/Flakiness/blob/main/src/Script-flakiness.py).

This dataset is categorized into causes and the Flaky test solution is stored [here](https://github.com/Test-Flaky/Flakiness/blob/main/data/IssuesGH_Flaky.xlsx).
These problems involved a total of 325 open source GitHub projects written primarily in four programming languages: Go, Java, JavaScript and Python.

We classify a number of root causes (473) and solutions (390).

### This dataset contains the following cause classifications for Flaky Tests:

| Problem | Initials|
| --- | --- |
| Async Wait | AC |
| Concurrency | C |
| Platform Dependency | PD |
| Network | N |
| Test Order Dependency | TOD |
| Resource Leak | RL |
| Unordered Collections | UC |
| Time | T |
| Test Case Timeout | TCT |
| Randomness | R |
| Floating Point Operations | FPO |
| Too Restrictive Range | TRR |
| Test Suite Timeout | TST |


### And the following classifications of solution strategies:

| Solution |
| --- |
| PD - Correct Directories |
| AW - Add/modify waitFor |
| AW - Add/modify sleep |
| N - Add/modify waitFor |
| TOD - Setup/cleanup state |
| UC - Not Specific Ordering |
| TCT - Increase Timeout |
| RL - Release resource |
| C - Other |
| C - Add/modify waitFor |
| T - Avoid Time Imprecision |
| C - Protect regions |
| C - Change condition |
| FPO - Revise assertions |
| AW - Reorder execution |
| N - Add/modify Mocks |
| R - Control the Seed |
| R - No Math.Random |
| TST - Split Test Suite |
| PD - Add/modify tests |
| TOD - Remove Dependency |
| TST - Skip Non-Initialized Part |
| TRR - Calibrate assertion |
| Hard to Classify |
| N - Disable Test |
| C - Disable Test |
| PD - Disable Test |
| AW - Disable Test |
| UC - Disable Test |
| RL - Disable Test |


We believe that the data set will be useful for the research community, not only to conduct research on various aspects of Flakys tests and their root causes, but also for a general understanding of behavior and how it is possible to resolve such instability in these tests.
