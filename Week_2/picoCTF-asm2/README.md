## picoCTF — asm2

### Objective
Understand stack behavior and determine how values are stored and retrieved.

---

### What I Did

1. Disassembled the binary using `objdump`.
2. Identified `push` and `pop` instructions affecting the stack.
3. Analyzed how the function created a stack frame.
4. Tracked how values were placed on the stack and later accessed.
5. Used `gdb` to observe stack and register values during execution.

---

### How It Was Solved

The solution required understanding how the stack pointer (esp/rsp) changes during execution. By following stack modifications carefully, I reconstructed the correct values used in the comparison.

---

### What I Learned

- How stack frames are structured
- The role of `push` and `pop`
- How local variables are stored on the stack
- Why understanding stack layout is critical for exploitation later
