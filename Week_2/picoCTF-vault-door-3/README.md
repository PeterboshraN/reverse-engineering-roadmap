## picoCTF — vault-door-3

### Objective
Analyze loop-based logic that transforms or validates input.

---

### What I Did

1. Loaded the binary into Ghidra.
2. Identified a loop iterating over input characters.
3. Analyzed how each character was transformed or compared.
4. Reconstructed the transformation logic manually.
5. Reversed the loop logic to determine the correct original input.

---

### How It Was Solved

The challenge used a loop to manipulate characters before comparison. By understanding how the loop modified each element, I reversed the transformation and rebuilt the expected input.

---

### What I Learned

- How loops are implemented using conditional jumps
- How iteration works at assembly level
- How to reverse character transformations
- How structured logic appears in low-level code
