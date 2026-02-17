## picoCTF — vault-door-1

### Objective
Reverse input validation logic to determine the correct password.

---

### What I Did

1. Opened the binary in Ghidra.
2. Located the main validation function.
3. Identified multiple if conditions checking specific characters.
4. Reconstructed the expected input by reversing each condition.
5. Combined all conditions into the final correct string.

---

### How It Was Solved

The program checked specific indices of the input string against expected values. By analyzing each comparison, I reconstructed the required password character by character.

---

### What I Learned

- How input validation appears in assembly/decompiled code
- How conditional branching implements logical checks
- How to reverse engineer string-based comparisons
