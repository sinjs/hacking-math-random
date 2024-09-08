# Solution using the z3 theorem prover from Microsoft Research
# Solving for seed states in XorShift128+ used in V8 (Node.js, Chrome)
# Tested on Node.js v20.17.0

import z3
import struct
import sys

# Insert the already known random sequence here (Done as a string for easy copy pasting)
sequence_str = """
0.009000476471095364
0.23883389315317372
0.8204247865044838
0.9219057574539395
0.8729524470337475
"""

sequence = list(map(lambda s: float(s), sequence_str.strip().split("\n")))

# Numbers presented in the entropy pool are reversed
sequence = sequence[::-1]

solver = z3.Solver()

# Create states
# Reference: https://github.com/v8/v8/blob/main/src/base/utils/random-number-generator.h#L119
se_state0, se_state1 = z3.BitVecs("se_state0 se_state1", 64)

for i in range(len(sequence)):
    # The XorShift128+ Algorithm
    # Reference: https://github.com/v8/v8/blob/main/src/base/utils/random-number-generator.h#L119
    se_s1 = se_state0
    se_s0 = se_state1
    se_state0 = se_s0
    se_s1 ^= se_s1 << 23
    se_s1 ^= z3.LShR(se_s1, 17)  # Logical shift instead of Arthmetric shift
    se_s1 ^= se_s0
    se_s1 ^= z3.LShR(se_s0, 26)
    se_state1 = se_s1

    float_64 = struct.pack("d", sequence[i] + 1)
    u_long_long_64 = struct.unpack("<Q", float_64)[0]

    # Get the lower 52 bits (mantissa)
    mantissa = u_long_long_64 & ((1 << 52) - 1)

    # Compare Mantissas
    solver.add(int(mantissa) == z3.LShR(se_state0, 12))


if solver.check() == z3.sat:
    model = solver.model()

    states = {}
    for state in model.decls():
        states[state.__str__()] = model[state]
    
    print(states)

    state0 = states["se_state0"].as_long()

    # Extract mantissa
    # Reference: https://github.com/v8/v8/blob/main/src/base/utils/random-number-generator.h#L111
    u_long_long_64 = (state0 >> 12) | 0x3FF0000000000000
    float_64 = struct.pack("<Q", u_long_long_64)
    next_sequence = struct.unpack("d", float_64)[0]
    next_sequence -= 1

    print(f"The next number is: {next_sequence}")
