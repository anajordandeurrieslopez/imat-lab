# IMAT-LAB

A Python command-line toolkit for modular arithmetic, developed as a collaborative university project for the Discrete Mathematics course at ICAI, Universidad Pontificia Comillas.

## Features

- Primality testing and prime number generation.
- Integer factorization.
- Greatest common divisor and coprimality checks.
- Modular exponentiation and multiplicative inverses.
- Euler's totient function and Legendre symbol.
- Systems of linear congruences.
- Interactive and batch processing modes.

## Requirements

Python 3.9 or later. No external dependencies are required.

## Usage

Keep `imatlab.py` and `modular.py` in the same folder.

Start the interactive interface:

```bash
python imatlab.py
```

Enter commands such as:

```text
primo(17)
factorizar(60)
mcd(24,36)
pow(2,10,7)
inv(3,7)
euler(12)
```

Submit an empty line to exit.

To read commands from a text file and save the results:

```bash
python imatlab.py input.txt output.txt
```

## Project structure

- `imatlab.py`: command interpreter and interactive/batch interface.
- `modular.py`: mathematical functions and algorithms.

## Authors

- Ana Jordán de Urries López
- Nerea Alonso González

## Academic context

This project was created for educational purposes to apply number theory and modular arithmetic through Python programming. Commands and source code documentation are in Spanish.
