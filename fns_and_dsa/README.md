# Python Functions & Data Structures – ALX Tasks

This directory contains Python scripts demonstrating core concepts such as functions, modules, data structures, lists, global variables, and the `datetime` module.

Each task is implemented in its own Python file as described below.

---

## 📌 1. Arithmetic Operations  
**File:** `arithmetic_operations.py`  
**Concepts:** Functions, modules, conditional logic, error handling  

This module defines a function `perform_operation(num1, num2, operation)` that performs basic arithmetic operations.  
It is designed to be imported and used by a provided `main.py` script.

### Supported Operations:
- `add`
- `subtract`
- `multiply`
- `divide` (with zero-division handling)

---

## 📌 2. Shopping List Manager  
**File:** `shopping_list_manager.py`  
**Concepts:** Lists, loops, user input, program flow  

A simple CLI app that allows the user to:

- Add items  
- Remove items  
- View current shopping list  
- Exit program  

The program runs in a continuous loop until the user chooses to exit.

---

## 📌 3. Explore datetime Module  
**File:** `explore_datetime.py`  
**Concepts:** `datetime`, functions, user input  

This script demonstrates:
- Displaying the current date and time (`display_current_datetime()`)
- Calculating a future date based on user input (`calculate_future_date()`)

Uses:
- `datetime.now()`
- `timedelta(days=...)`

---

## 📌 4. Temperature Conversion Tool  
**File:** `temp_conversion_tool.py`  
**Concepts:** Global variables, functions, input validation  

This script converts temperatures between Celsius and Fahrenheit using:

- `FAHRENHEIT_TO_CELSIUS_FACTOR` (5/9)  
- `CELSIUS_TO_FAHRENHEIT_FACTOR` (9/5)

Features:
- Converts from C → F or F → C  
- Validates user input  
- Raises an error for invalid temperature values  

---

# 📂 Project Structure

# alx_be_python