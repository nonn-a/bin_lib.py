![bin_lib](https://github.com/nonn-a/bin_lib.py/assets/86384221/20a255ce-ac62-4671-831c-516ff3e8c6a1)

# Bin_lib.py

A minimal python library for binary numbers.

------------------------------------------------------------------------------
## Getting Started

### Dependencies

* Python 3.

### Installing

* **Download** the file `bin_lib.py`
* **Place** it in the same folder of your main code.
* **Import** with `import "bin_lib.py"`.
* **Done**.

------------------------------------------------------------------------------
## Defining a Bin variable.

### **Examples of definitions.**

| Definition                 | Output        |
| -------------------------- | ------------- |
| `Bin(6)`                   | 110           |
| `Bin([1, 1, 0])`           | 110           |
| `Bin([True, True, False])` | 110           |

### **Operations and comparisons**
`Bin` objects can be added and compared to other `Bin`, `int` or appropriate `list` objects.  
Any comparison works fine (`<, <= , ==, =>, >, !=`).

### **Artificial lenght**
This can be used to solve some nieche problems.  
You can make your Bin numbers have a maximum lenght.  
For example, `Bin(64, 2)` will give an `OverflowError` because 64 doesn't fit in `2` bits.
