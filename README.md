# Morse Code Translator App

A simple **Morse Code Translator** with a GUI frontend and a C backend.

---

## Getting Started

Run the app with:

```bash
python3 ./gui.py
```

You **must** have the following files in the **same directory**:

* `input.txt`
* `output.txt`
* `variant.c`
* `gui.py`

The easiest way is to **clone the entire repository**.

---

## Usage and Syntax

### Text to Morse

* `'-'` (dash) is translated to `-....-` (its Morse equivalent)
* Spaces between words are translated to `/`
* A dot `.` is translated to `//`
* Serbian special letters:

  * **š** → `s`
  * **ć** → `c`
  * **č** → `c`
  * **đ** → `dj`
* The following characters are **not converted** and are passed as-is:
  `" , ? ! ( ) ' ; : #`
* Any other character **not** a letter (A-Z, a-z) or digit (0-9) will be translated to `?`

**Example input:**

```
Mary wanted to jump with Čika Mile.
Šaban Šaulić declined. Which is unfortunate.
He is 26 years old - very unhappy.
```

---

### Morse to Text

* `-....-` translates to `-` (dash)
* `/` translates to a space (word separator)
* `//` represents a dot `.`
* Each Morse character must be separated by a space
* The following punctuation characters are **not converted** and are printed as-is:
  `" , ? ! ( ) ' ; : #`
* Any other unrecognized Morse code is converted to `?`

**Example input:**

```
# .... .. / -.. --- / -.-- --- ..- / ( .-- .- -. -. .- ) / . .- - ? !
```

**Expected output:**

```
#HI DO YOU (WANNA) EAT ?!
```

---

## How to Write Input

* Use spaces to separate Morse code characters.
* Punctuation marks should be written normally.
* Serbian special letters are normalized as above.
* Unrecognized characters result in `?`.

---

## Example Morse Input:

```
-- .- .-. -.-- / .-- .- -. - . -.. / - --- / .--- ..- -- .--. / .-- .. - .... / .. -.- .- / -- .. .-.. . // 
.- -... .- -. / .- ..- .-.. .. -.-. / -.. . -.-. .-.. .. -. . -.. // / .-- .... .. -.-. .... / .. ... / ..- -. ..-. --- .-. - ..- -. .- - . // 
.... . / .. ... / ..--- -.... / -.-- . .- .-. ... / --- .-.. -.. / -....- / ...- . .-. -.-- / ..- -. .... .- .--. .--. -.-- // 
```

---

## About

* The **core logic is written in C** (`variant.c`) for speed and simplicity (which I might regret).
* The GUI and user interaction are handled by **Python** (`gui.py`).
* The Python frontend writes to `input.txt`, invokes the C backend, then reads from `output.txt`.

---

## Morse Code

![Morse Code Sample](/Morse-Code/OIP.jpg "Sample Morse Code")

