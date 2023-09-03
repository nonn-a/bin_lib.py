![binlib](https://github.com/nonn-a/bin_lib.py/assets/86384221/a3784e9d-9359-4039-94f9-9f12d15a8391)

<p align="center">
A minimal python library for binary data.  
</p>

---

![gettingstarted](https://github.com/nonn-a/bin_lib.py/assets/86384221/d5f550a1-a55f-4ae6-b1a3-e46d09438bfb)

<p align="center">
<strong>Installing.</strong>
</p>

No specific installation is required for **bin_lib.py**. You can use it by importing it directly into your Python scripts or projects:

**>** **Download** the file `bin_lib.py`.  
**>** **Place** it in the same folder of your main code.  
**>** **Import** with `import "bin_lib.py"`.  
**>** **Done**.  

---

![technicalities](https://github.com/nonn-a/bin_lib.py/assets/86384221/6ecd37d2-9525-4463-8859-260d029160f1)

<p align="center">
<strong>Documentation.</strong> Complete explaination of the code.
</p>

## What does 'bin_lib.py' introduce?

It introduces two minimal features:  
**>** `BinAlike`: an alias that represents objects that have similar properties to `Bin` numbers.  
These objects include: `Bin`s, `int`s, `list`s and can be added to, compared to and used to define objects from the `Bin` class.  
**>** `Bin`: main feature, a class used to store and interact with **binary data**.

### `Bin`'s constructor:
```py
class Bin():
    def __init__(self, definition: BinAlike, length: int = -1):
        [···]
```
**>** `definition`: needs to be a `BinAlike` value. It is what gets turned into its binary representation.  
**>** `lenght`: maximum bit-wise lenght of a stored value. It has some nieche uses (see operations and comparisons).

A few examples of **valid** Bin definitions:
```py
#Examples.
bin1 = Bin(45) #Value: 101101, the value of 45 converted to binary.
bin2 = Bin([0, 0, 0, 1, 0, 1, 0, 0, 0]) #Value: 1011000
bin3 = Bin([True, False, False, True]) #Value: 1001
bin4 = Bin(2, length = 3) #Value: 10. This works because 2 occupies just 2 out of the 3 (maximum, 3rd included) bits given.
```
\***p.s.** Some other definitions are valid but strongly unsuggested for readability purposes. When defining `Bins` with `list`s, everything that gets evaluated to be a `True` value gets interpreted as a `1` and everything that gets evaluated to be a `False` value gets interpreted as a `0`.

### Modules.
`Bin`'s class offers a single non-standard module:
```py
        [···]
        get_bit(self, a: int, b: int = -1):
            [···]
```
**>** `get_bit` returns bits as a list from index a to b. If b is -1, only the bit at index a is returned. If b is provided, it returns a list of  
 bits from a to b.

### Operations and comparisons.
**>** At the moment `Bin` objects can be added to other `BinAlike` objects.  
The `lenght` of the addition result is the biggest of the addends' lenghts.  
**>** `Bin` objects can be compared to other `BinAlike` objects.  
Supported comparisons: `==, !=, <, <=, =>, >`.  

### Small code example.
```py
import "bin_lib.py" #Importing the library

bin_1, bin_2 = Bin(45), Bin([0, 1, 0, 1]) #Binary number definitions.
if bin_2 < bin_1 < [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: #(Bin, Bin) and (Bin, list) comparisons.
    print(bin_1 + bin_2)
elif bin_2 < 99999999: #(Bin, int) comparison.
    print(Bin([False]))
```

![contribute](https://github.com/nonn-a/bin_lib.py/assets/86384221/4efad539-4058-46ef-9e72-a43012ae4e9b)

<p align="center">
<strong>Conclusion.</strong> Contribution info and such.
</p>

Feel free to explore the capabilities of the library and integrate it into your projects as needed. Should you have any questions or encounter issues, refer to the provided documentation and MIT License for usage terms. Support this project by contributing to its development.

Happy coding with binary data using bin_lib.py!
