
<center>
  (¬P ∨ ¬Q)
</center>


## ✅ De Morgan’s Laws (Propositional Logic) – Easy & Step-by-Step

De Morgan’s Laws are very important in **GATE**, **Boolean algebra**, **Digital Logic**, and **Discrete Mathematics**.

They help you **remove negation (NOT) from brackets**.

---

# 🔹 1️⃣ What is the Problem De Morgan Solves?

Sometimes we get expressions like:

```
¬(P ∧ Q)
¬(P ∨ Q)
```

It is difficult to directly evaluate them.

👉 De Morgan’s Laws help us rewrite these expressions in a simpler form.

---

# 🔹 2️⃣ The Two De Morgan’s Laws

### 📌 Law 1:

[
\neg (P \land Q) \equiv (\neg P \lor \neg Q)
]

👉 **NOT of AND becomes OR of NOTs**

---

### 📌 Law 2:

[
\neg (P \lor Q) \equiv (\neg P \land \neg Q)
]

👉 **NOT of OR becomes AND of NOTs**

---

# 🔹 3️⃣ Easy Trick to Remember (Exam Shortcut)

### ⭐ Rule:

1. **Remove the NOT outside**
2. **Change the operator**

   * AND ↔ OR
3. **Put NOT on each variable**

---

### 🧠 Memory Trick:

> "Break the bracket, change the sign, negate everything."

---

# 🔹 4️⃣ Truth Table Proof (Step-by-Step)

Let’s prove:

[
\neg (P \land Q) = (\neg P \lor \neg Q)
]

| P | Q | P ∧ Q | ¬(P ∧ Q) | ¬P | ¬Q | ¬P ∨ ¬Q |
| - | - | ----- | -------- | -- | -- | ------- |
| T | T | T     | F        | F  | F  | F       |
| T | F | F     | T        | F  | T  | T       |
| F | T | F     | T        | T  | F  | T       |
| F | F | F     | T        | T  | T  | T       |

👉 Both last columns are same
✔ Therefore proved.

Same method works for second law.

---

# 🔹 5️⃣ Example Problems (Important for GATE)

---

### ✅ Example 1

Simplify:

[
\neg (P \lor Q)
]

Using Law 2:

[
= (\neg P \land \neg Q)
]

---

### ✅ Example 2

Simplify:

[
\neg (P \land (Q \lor R))
]

Step 1: Apply De Morgan to outer bracket:

[
= \neg P \lor \neg (Q \lor R)
]

Step 2: Apply again inside:

[
= \neg P \lor (\neg Q \land \neg R)
]

---

# 🔹 6️⃣ Real World Example

Let:

* P = "It is raining"
* Q = "It is cold"

Now consider:

[
\neg (P \land Q)
]

Meaning:

"It is NOT true that it is raining AND cold"

According to De Morgan:

[
= \neg P \lor \neg Q
]

Meaning:

"Either it is NOT raining OR it is NOT cold"

Same meaning in real life.

---

# 🔹 7️⃣ Why Important for GATE?

✔ Used in:

* Boolean algebra
* Digital circuits
* Logic simplification
* Proofs
* CNF and DNF conversion
* Complement of sets
* NAND/NOR gate implementation

---

# 🔹 8️⃣ Connection to Boolean Algebra (Digital Logic)

In Boolean algebra:

[
(A \cdot B)' = A' + B'
]

[
(A + B)' = A' \cdot B'
]

This is same De Morgan law.

Very important for:

* NAND gates
* NOR gates
* Logic design

---

# 🔹 9️⃣ Multiple Variables Case (Very Important)

De Morgan works for any number of variables:

[
\neg (A \land B \land C)
========================

\neg A \lor \neg B \lor \neg C
]

[
\neg (A \lor B \lor C)
======================

\neg A \land \neg B \land \neg C
]

---

# 🔹 🔥 Common GATE Mistakes

❌ Forgetting to change AND to OR
❌ Forgetting to negate every variable
❌ Missing brackets
❌ Applying only once when nested

---

# 🔹 🎯 Quick Exam Shortcuts

### If question says:

"Find negation of statement"

👉 Directly apply De Morgan.

Example:

Negation of:

"All students are intelligent"

Becomes:

"Some students are NOT intelligent"

(This is predicate logic version of De Morgan.)

---

# 🔹 🔥 One-Line Summary

| Expression | After Applying De Morgan |
| ---------- | ------------------------ |
| ¬(A ∧ B)   | ¬A ∨ ¬B                  |
| ¬(A ∨ B)   | ¬A ∧ ¬B                  |

---

# ✅ Final Key Points to Remember (Very Important)

✔ NOT distributes inside
✔ AND ↔ OR
✔ Negate everything
✔ Works for any number of variables
✔ Used heavily in GATE

---

If you want, I can next explain:

* 👉 How De Morgan is used in CNF/DNF conversion
* 👉 How it appears in previous GATE questions
* 👉 Relation with NAND/NOR implementation
* 👉 Predicate logic version

Just tell me 😊
