# Ethiopian Festivals And Holidays Generator

- This is a python CLI program that generates the dates of main holidays of each year in ethiopian calendar.

## Features

- The program has two main features:

### 1. Prints a table of the holidays

- Assuming you are in the directory of the file `oop_main.py`, you can enter the following command:

```
python3 oop_main.py [year]
```

Example:

```
python3 oop_main.py 2015
```

- The command will return a table like:

  ![Sample Table](/img/IMG1.PNG)

### 2. Prints a date for a specific holiday

- Again, assuming you are in the directory of the file `oop_main.py`, you can enter the following command:

```
python3 oop_main.py [year] [Holiday argument]
```

Example:

```
python3 oop_main.py 2015 --fasika
```

- The command will return:

  ![Fakia Date][/img/img2.png]

- Since there are multiple parameters for the holidays, you can run the following command for help

```
python3 oop_main.py -h
```

---

License: The repository is licensed under the MIT License.
