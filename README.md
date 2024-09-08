# Hacking `Math.random()` challenge

This is a programming challenge where you need to try to predict the next random number generated using `Math.random()`.

## Requirements

- `python3` and `pip3`
- `node`
- `pnpm`

## Installation

Before you can run the challenge, you need to clone the code and install dependencies:

```shell
# Clone all code from the Git repository
git clone https://github.com/sinjs/hacking-math-random.git

# Change current directory into the source code folder
cd hacking-math-random

# Install dependencies (tsx and @types/node)
pnpm install
```

## Running the challenge

To run the challenge, use the following command after installation:

```shell
pnpm challenge
```

This will start the challenge process and ask for the predicted number.

## Solution

If you want to view and run the solution, it is in the `solution` branch:

```shell
# Check out the `solution` branch
git checkout solution
```

To get the correct next number predicted, you need to modify `solution/main.py` and set the correct sequence of already known numbers:

```python
# solution/main.py

sequence_str = """
0.9749233582455272
0.2143653745005023
0.4674231674823175
0.39205016432410167
0.3063857991276704
"""
```

Afterwards, you are able to run the solution to predict the next number of the sequence.

```shell
# Runs the solution
pnpm solution
```

## Showcase your solution

If you have your own solution, you can make a pull request against the `showcase` branch to add your own solution.

Happy Hacking!
