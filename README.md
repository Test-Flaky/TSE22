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

| Fix Strategy |
| --- |
| AW - Add/modify waitFor |
| AW - Add/modify sleep |
| AW - Reorder execution |
| C - Other |
| C - Add/modify waitFor |
| C - Change condition |
| C - Protect regions |
| FPO - Revise assertions |
| N - Add/modify waitFor |
| N - Add/modify Mocks |
| PD - Add/modify tests |
| PD - Correct Directories |
| R - Control the Seed |
| R - No Math.Random |
| RL - Release resource |
| TST - Split Test Suite |
| TST - Skip Non-Initialized Part |
| TCT - Increase Timeout |
| TOD - Remove Dependency |
| TOD - Setup/cleanup state |
| T - Avoid Time Imprecision |
| TRR - Calibrate assertion |
| UC - Not Specific Ordering |
| Hard to Classify |


We believe that the data set will be useful for the research community, not only to conduct research on various aspects of Flaky tests and their root causes but also for a general understanding of behavior and how it is possible to resolve such instability in these tests.
