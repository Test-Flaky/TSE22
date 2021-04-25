This repository contains the dataset of flaky tests for the "**Test Flakiness Across Programming Languages**" paper.

## Anonymized Dataset

The anonymous dataset contains 1.291 issues which were extracted from projects stored on GitHub through the Script that is stored [here](https://github.com/Test-Flaky/Flakiness/blob/main/src/Script-flakiness.py).

This dataset is categorized into causes and the Flaky test solution is stored [here](https://github.com/Test-Flaky/OOPSLA21/tree/main/data).
These Root Cause involved a total of 325 open source GitHub projects written primarily in four programming languages: Go, Java, JavaScript and Python.

We classify a number of root causes (473) and solutions (390).

#### This dataset contains the following cause classifications for Flaky Tests:






| Root Cause | Initials |
| --- | --- |
| Async Wait | AW |
| Concurrency | C |
| Floating Point Operations | FPO |
| Network | N |
| Platform Dependency | PD |
| Randomness | R |
| Resource Leak | RL |
| Test Suite Timeout | TST |
| Test Case Timeout | TCT |
| Test Order Dependency | TOD |
| Time | T |
| Too Restrictive Range | TRR |
| Unordered Collections | UC |


#### This dataset contains the following fix classifications for Flaky Tests:

![myimage-alt-tag](https://github.com/Test-Flaky/OOPSLA21/blob/main/Image/Fix.png)


We believe that the data set will be useful for the research community, not only to conduct research on various aspects of Flaky tests and their root causes but also for a general understanding of behavior and how it is possible to resolve such instability in these tests.
