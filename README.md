# 🖥️ Console Calculator App - Documentation

Welcome to **Console Calculator App** – a simple, interactive console-based calculator written in Python. This documentation explains the source code, commands, features, and usage in detail.

---

## 📁 Project Structure

```
Console-Calculator-py/
│
├─ calculator.py        # Main program containing the console calculator logic
├─ README.md            # Project description and contact links
└─ DOCUMENTATION.md     # Full project documentation
```

---

## ⚙️ Main Features

* 🧮 Basic arithmetic operations:

  * Sum
  * Subtraction (Miness)
  * Multiplication
  * Division
* 📝 Evaluate custom expressions via Python `eval`
* 💡 Continuous input until user decides to stop
* 🛑 Exit/Cancel commands to terminate operations
* 🖼️ Interactive, console-friendly UI with dynamic headers

---

## 📝 Functions Overview

### 1️⃣ `clear_window()`

```python
def clear_window():
    os.system("cls")
```

* **Purpose:** Clears the console window.
* **Usage:** Called before printing the title to refresh the display.
* **Return Type:** None

---

### 2️⃣ `print_title(string: str)`

```python
def print_title(string):
    clear_window()
    print(("-")*50)
    print(f"\t{string}")
    print(("-")*50)
    print("\n")
```

* **Purpose:** Displays a formatted title for each command or section.
* **Parameters:**

  * `string` (str): Title text to display
* **Usage:** Called at the beginning of every command to improve UI.
* **Return Type:** None

---

## 🔹 Main Loop & Commands

The program runs in an infinite loop until the user chooses to exit. Commands are chosen using a number or keyword.

### Command Menu

```
0. Input Result
1. Sum
2. Miness
3. Multipile
4. Division
exit / cancel / c / n
```

---

### 1️⃣ Input Result (`0`)

* **Purpose:** Evaluate a custom mathematical expression.
* **Usage Example:**

```text
Input: 2 + 3 * 5
Output: Your sums resualts is 17
```

* **Implementation:** Uses `eval` with restricted built-ins for safety.

---

### 2️⃣ Sum (`1`)

* **Purpose:** Continuously sum numbers until user exits.
* **Flow:**

  1. Input numbers one by one
  2. Confirm continuation (`y/n`)
  3. Display total sum
* **Sample Session:**

```text
Enter number: 5
Continue? y
Enter number: 10
Continue? n
Output: Your sums resualts is 15
```

---

### 3️⃣ Miness (`2`)

* **Purpose:** Continuously subtract numbers from an initial value.
* **Flow:**

  1. First input initializes `miness_resualt`
  2. Subsequent numbers are subtracted
  3. User exits when done
* **Example:**

```text
Enter number: 20
Enter number: 5
Enter number: 3
Output: Your Minesss resualts is 12
```

---

### 4️⃣ Multipile (`3`)

* **Purpose:** Continuously multiply numbers.
* **Flow:** Similar to sum but multiplies numbers.
* **Example:**

```text
Enter number: 2
Enter number: 3
Output: Your Multipile resualts is 6
```

---

### 5️⃣ Division (`4`)

* **Purpose:** Continuously divide numbers.
* **Flow:**

  1. First input initializes `division_resualt`
  2. Subsequent inputs divide the previous result
* **Example:**

```text
Enter number: 100
Enter number: 2
Enter number: 5
Output: Your Division resualts is 10
```

---

### 6️⃣ Exit / Cancel

* **Commands:** `exit`, `cancel`, `c`, `n`
* **Purpose:** Stops the program and exits the calculator.

---

## 💾 Data Storage

This calculator **does not persist data** in files or databases. All values exist in memory during runtime.

**Variables in memory:**

| Variable            | Type      | Description                        |
| ------------------- | --------- | ---------------------------------- |
| `sum_resualt`       | float     | Stores sum totals                  |
| `miness_resualt`    | float     | Stores subtraction results         |
| `multipile_resualt` | float     | Stores multiplication results      |
| `division_resualt`  | float     | Stores division results            |
| `calculate_resualt` | float/int | Stores evaluated custom expression |

---

## 🛠️ Code Notes

* The program uses Python 3.10+ **match-case** for command handling.
* **UI Design:** Dynamic headers with `print_title()` and console clearing with `os.system("cls")`.
* **Safety:** `eval` is sandboxed with empty built-ins.
* **Looping:** Each arithmetic command runs in a while loop until the user chooses to stop.

---

## 🎨 Console UI Example

```
--------------------------------------------------
    Welcome to "Console Calculator App"
--------------------------------------------------

0. Input Resualt
1. Sum
2. Miness
3. Multipile
4. Division

Please write command num: 1
```

* After choosing a command, a similar header is printed for the operation.

---

## 📌 Author & Contact

* **Author:** Sobhan-SRZA (mr.sinre)
* **Website:** [https://srza.ir](https://srza.ir)
* **GitHub:** [https://github.com/Sobhan-SRZA](https://github.com/Sobhan-SRZA)
* **Telegram:** [@d_opa_mine](https://t.me/d_opa_mine) / [@Sobhan_SRZA](https://t.me/Sobhan_SRZA)
* **Instagram:** [@mr.sinre](https://www.instagram.com/mr.sinre)
* **YouTube:** [@mr_sinre](https://www.youtube.com/@mr_sinre)
* **Discord:** Sobhan-SRZA team servers linked in README

---

## ✅ Summary

**Console Calculator App** is a simple, safe, and interactive calculator for basic arithmetic operations and custom calculations.
It is perfect for **learning Python, testing math operations in console, or adding a simple utility to your projects**.
