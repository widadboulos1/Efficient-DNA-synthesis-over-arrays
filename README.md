# Efficient-DNA-synthesis-over-arrays

Suppose you need to synthesize m·n strands, arranged in an m×n matrix,
where each cell represents a strand. In each clock cycle, the synthesis machine
generates one symbol according to its predefined synthesis sequence.
However, it can synthesize only one strand per row, but multiple strands per column.
Some of the questions that can be asked are:
1. What is the optimal way to program the synthesis machine and determine which
base to synthesize in each cycle?
2. What is the optimal way to arrange the strands in the array?

## Getting Started

In this project there are 6 files:
1) README.md
2) requirements.txt: includes the python packages that need to be installed to run the code.
3) dssp.py: includes the DSSP algorithm with 2 strings as an example, when running this file, you'll get the DSSP algorithm on those 2 strings.
4) dssp_script.py: a version of the DSSP algorithm that takes two strings as command-line input
5) machine_order_dp.py: includes the DP algorithm which decides the machine order with 4 strings as an example, when running this file, you'll get the DP algorithm on those 4 strings.
6) machine_order_dp_script.py: includes the DP algorithm which decides the machine order which takes 4 strings as input from the user.

Note: the machine_order_dp code prints the machine order, number of cycles, and the synthesis steps (in reverse order – from end to start)


### Prerequisites

You need to run this instruction before running the codes:

```
pip install -r requirements.txt
```

## Running the code

To run the DSSP algorithm with two strings, use: dssp_script.py str1 str2
For example:
```
python dssp_script.py ACGTGTA GTACTGA
```

To run the DP algorithm for the optimal machine order with 4 strings in a 2×2 array: machine_order_dp.py str1 str2 str3 str4
For example:
```
python machine_order_dp_script.py GATTACA GTACGGA CAGTTAC GCTAGGA
```

