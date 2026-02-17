## picoCTF — asm3

### Objective
Analyze arithmetic logic implemented in assembly and compute the correct result.

---

### What I Did

1. Disassembled the program.
2. Identified arithmetic operations including `add`, `sub`, and `imul`.
3. Traced how intermediate values were stored in registers.
4. Reconstructed the entire calculation manually.
5. Verified reasoning using `gdb`.

---

### How It Was Solved

The binary performed multiple arithmetic operations before comparing the result to a target value. By simulating the operations step by step, I determined the correct input/output relationship.

---

### What I Learned

- How arithmetic expressions are translated into assembly
- How comparisons are performed using `cmp`
- How flags influence conditional jumps
- How to reason about register state over time
