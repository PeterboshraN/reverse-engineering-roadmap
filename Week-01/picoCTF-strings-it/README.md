## picoCTF — strings it

# Objective
Find hidden information inside a binary file.

---

# Approach
- Identified the file type using `file`
- Extracted printable strings using the `strings` command
- Located the flag directly from the output

---

# Tools Used
- strings
- file

---

# Concept Learned
- Many binaries leak useful information through embedded strings
- Quick static inspection can solve simple reversing challenges
