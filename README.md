# Item Numbers Text Parsing

This is a simple script to assist with reviewing construction documents for item numbers. Following design, often estimating work is required in which design engineers must review plans and estimate quantities for the contractors bid.

This script will parse a text file generated following plan creation and search for regular expressions in the form of ITEM XX.XXXX.

Upon running the script the user will be prompted to select the text file for parsing and then the script will save a text file with the sorted item numbers found.

## Installation

Clone the repository for use of the processing python script.

```bash
item_number_processing.py
```

## Requirements

```python
import re
import tkinter as tk
from tkinter import filedialog
import sys

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
