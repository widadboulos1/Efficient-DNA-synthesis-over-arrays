# Efficient-DNA-synthesis-over-arrays

Suppose you need to synthesize m·n strands, arranged in an m×n matrix,
where each cell represents a strand. In each clock cycle, the synthesis machine
generates one symbol according to its predefined synthesis sequence.
However, it can synthesize only one strand per row but multiple strands
per column.
some of the questions that can be asked:
1. What is the optimal way to program the synthesis machine and determine which
base to synthesize in each cycle?
2. What is the optimal way to arrage the strands in the array?

## Getting Started

In this project there are 6 files:
1) README file
2) requirements.txt: includes the python packages that need to be installed to run the code.
3) dssp.py: includes the DSSP algorithm with 2 strings as an example, when running this file, you'll get the DSSP algorithm on those 2 strings.
4) dssp_script.py: includes the DSSP algorithm which takes 2 strings as input from the user.
5) machine_order_dp.py: includes the DP algorith which decides the machine order with 4 strings as an example, when running this file, you'll get the DSSP algorithm on those 4 strings.
6) machine_order_dp_script.py: includes the DP algorith which decides the machine order which takes 4 strings as input from the user.


### Prerequisites

You need to run this instruction before running the codes:

```
pip install -r requirements.txt
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```
