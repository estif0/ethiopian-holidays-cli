# Ethiopian Festivals And Holidays Generator

- This is a python CLI program that generates the dates of main holidays of each year in ethiopian calendar.

## Features

- The program has two main features:

### 1. Prints a table of the holidays

- Assuming you are in the directory of the file `main.py`, you can enter the following command:

```sh
python3 main.py [year] -a
```

> or

```sh
python3 main.py -a
```

Example:

```sh
python3 main.py 2015 -a
```

> or you can just use the -a argument

```sh
python3 main.py -a
```

- The command will return a table like:

  ![Sample Table](/img/IMG1.PNG)

### 2. Prints a date for a specific holiday

- Again, assuming you are in the directory of the file `main.py`, you can enter the following command:

```sh
python3 main.py [year] [Holiday argument]
```

> or

```sh
python3 main.py [Holiday argument]
```

Example:

```sh
python3 main.py 2015 --fasika
```

> or

```sh
python3 main.py --fasika
```

- The command will return:

  ![Fakia Date](/img/IMG2.PNG)

- Since there are multiple parameters for the holidays, you can run the following command for help

```sh
python3 main.py -h
```

### If you want to know how all the calculations were made:

[Click Here!](https://drive.google.com/file/d/1e7AukagokWlEiuz_0YtZ8Oz3RcUoQaLC/view?usp=sharing)

---

License: The repository is licensed under the MIT License.
