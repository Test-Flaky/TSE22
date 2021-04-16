This repository contains the dataset of flaky tests for the "**A Study of Test Flakiness Across Programming Languages**" paper.

## Anonymized Dataset

The anonymous dataset contains 1.291 issues which were extracted from projects stored on GitHub through the Script that is stored [here](https://github.com/Test-Flaky/Flakiness/blob/main/src/Script-flakiness.py).

This dataset is categorized into causes and the Flaky test solution is stored [here](https://github.com/Test-Flaky/Flakiness/blob/main/data/IssuesGH_Flaky.xlsx).
These problems involved a total of 325 open source GitHub projects written primarily in four programming languages: [Go](https://img.shields.io/badge/issues-1291-red), [Java](https://www.java.com/pt-BR/), [JavaScript](https://www.javascript.com/), and [Python](https://www.python.org/).

We classify a number of root causes (473) and solutions (390).

### This dataset contains the following cause classifications for Flaky Tests and the following classifications of solution strategies:

| Cause | Initials | Solution |  | Cause | Initials | Solution |
| --- | --- | --- | --- | --- | --- | --- |
| Async Wait | AW | AW - Add/modify waitFor |  | Randomness | R | R - Control the Seed |
|  |  | AW - Add/modify sleep |  |  |  | R - No Math.Random |
|  |  | AW - Reorder execution |  | Resource Leak | RL | RL - Release resource |
| Concurrency | C | C - Other |  | Test Suite Timeout | TST | TST - Split Test Suite |
|  |  | C - Add/modify waitFor |  |  |  | TST - Skip Non-Initialized Part |
|  |  | C - Change condition |  | Test Case Timeout | TCT | TCT - Increase Timeout |
|  |  | C - Protect regions |  | Test Order Dependency | TOD | TOD - Remove Dependency |
| Floating Point Operations | FPO | FPO - Revise assertions |  |  |  | TOD - Setup/cleanup state |
| Network | N | N - Add/modify waitFor |  | Time | T | T - Avoid Time Imprecision |
|  |  | N - Add/modify Mocks |  | Too Restrictive Range | TRR | TRR - Calibrate assertion |
| Platform Dependency | PD | PD - Add/modify tests |  | Unordered Collections | UC | UC - Not Specific Ordering |
|  |  | PD - Correct Directories |  | All categories |  | Hard to Classify |


We believe that the data set will be useful for the research community, not only to conduct research on various aspects of Flaky tests and their root causes but also for a general understanding of behavior and how it is possible to resolve such instability in these tests.
