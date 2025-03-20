# Plus One Problem

## 📌 Problem Statement:

The "Plus One" problem requires adding 1 to a number represented as an array of digits. Each element in the array represents a single digit of the number. The function should return a new array with the updated number.

---

## 🔍 How the Code Works:

### 1️⃣ Start from the Last Digit:

- Since numbers increase from the rightmost digit, we begin at the last index.
- We check if this digit is **less than 9**.

### 2️⃣ Simple Addition:

- If the digit is **less than 9**, we simply **add 1** to it and return the updated array.

### 3️⃣ Handle the Case of 9:

- If the digit is **9**, adding 1 makes it **10**, so we set it to **0** and move to the previous digit.
- This process continues until we find a digit that is not 9.

### 4️⃣ Handling All Nines (999 → 1000):

- If all digits were 9, we need to create a **new array** with an extra space.
- The new array starts with **1**, followed by all zeros. Example: `[1,0,0,0]`.

### 5️⃣ Return the Updated Array:

- The function **returns the modified array**, representing the correct incremented number.

---

## ⏳ Time Complexity:

- **O(n)** → In the worst case, we check each digit once.

## 💾 Space Complexity:

- **O(n)** → If all digits are 9 (e.g., `999 → 1000`), we create a new array.

---

## ✅ Example:

### **Input:**

```python
digits = [1, 2, 3]
```
