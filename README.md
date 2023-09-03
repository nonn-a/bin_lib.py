![binlib](https://github.com/nonn-a/bin_lib.py/assets/86384221/a3784e9d-9359-4039-94f9-9f12d15a8391)

<p align="center">
A minimal python library for binary data.  
</p>

---

![gettingstarted](https://github.com/nonn-a/bin_lib.py/assets/86384221/71e402fd-b1c7-41ba-a788-536125636d01)

<p align="center">
<strong>Installing.</strong>
</p>

No specific installation is required for `bin_lib.py`. You can use it by importing it directly into your Python scripts or projects:
* **Download** the file `bin_lib.py`
* **Place** it in the same folder of your main code.
* **Import** with `import "bin_lib.py"`.
* **Done**.

---

![technicalities](https://github.com/nonn-a/bin_lib.py/assets/86384221/f84e4219-5da6-4786-948d-60babe45ecf7)

<p align="center">
<strong>Documentation.</strong> Complete explaination of the code.
</p>

## What does 'bin_lib.py' introduce?

It introduces two minimal features:
* `BinAlike`: an alias for every objec that has similar properties to `Bin` numbers.  
These objects include: `Bin`s, `int`s, `list`s and can be added to, compared to and used to define objects from the `Bin` class.
* `Bin`: a class used for bin numbers.

### **Operations and comparisons**
`Bin` objects can be added and compared to other `Bin`, `int` or appropriate `list` objects.  
Any comparison works fine (`<, <= , ==, =>, >, !=`).

### **Artificial lenght**
This can be used to solve some nieche problems.  
You can make your Bin numbers have a maximum lenght.  
For example, `Bin(64, 2)` will give an `OverflowError`, as `64` doesn't fit in `2` bits.
