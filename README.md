This repository contains the dataset of flaky tests for the "**Test Flakiness Across Programming Languages**" paper.

## Anonymized Dataset

The anonymous dataset contains 1.291 issues which were extracted from projects stored on GitHub through the Script that is stored [here](https://github.com/Test-Flaky/Flakiness/blob/main/src/Script-flakiness.py).

This dataset is categorized into causes and the Flaky test solution is stored [here](https://github.com/Test-Flaky/OOPSLA21/tree/main/data).
These problems involved a total of 325 open source GitHub projects written primarily in four programming languages: Go, Java, JavaScript and Python.
We classify a number of root causes (473) and solutions (390).

#### This dataset contains the following cause classifications for Flaky Tests:

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

#### This dataset contains the following fix classifications for Flaky Tests:






We believe that the data set will be useful for the research community, not only to conduct research on various aspects of Flaky tests and their root causes but also for a general understanding of behavior and how it is possible to resolve such instability in these tests.
