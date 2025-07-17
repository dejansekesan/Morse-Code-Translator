# Morse Code Translator App

A simple **Morse Code Translator** with a Python GUI frontend.

---

## Getting Started

Run the app with:

```bash
python3 ./morse.py
```
Or run the compiled binary from the releases.

---

## Usage and Syntax

### Text to Morse

* Letters, digits, and common punctuation are converted to Morse.
* Spaces between words are translated to `/` (word separator).
* Newlines are treated as word separators in audio playback.
* Serbian special letters are normalized as follows:

  * **š** → `s`
  * **ć** → `c`
  * **č** → `c`
  * **đ** → `dj`
* Supported punctuation characters (converted to Morse):
  `! ? ( ) . , : ; = + - _ " $ @ /`
* Characters not in the dictionary are skipped (no output).
* Output Morse characters are separated by spaces.
* Newlines in input text create new lines of Morse output.

---

### Morse to Text

* Morse code characters must be separated by spaces.
* `/` represents a space (word separator).
* Newlines are treated as word separators (audio playback pause).
* Supported Morse codes for punctuation are converted to their characters.
* Unrecognized Morse sequences convert to an empty string.
* Serbian special letters must be input as their Morse equivalent of normalized characters (e.g. `s` for `š`).
* Spaces are allowed in Morse input.
* Output is the decoded text with normalized Serbian letters.

---

## Audio Playback

* Click **Play** to hear Morse code:

  * In **Text to Morse** mode, the Morse in the output box is played.
  * In **Morse to Text** mode, the Morse in the input box is played.
* Newlines and `/` produce word-length pauses.
* Use the **Volume** slider to adjust beep volume.
* Use the **Speed** slider (0.1s to 2.0s) to control beep duration (lower = faster).
* The **Stop** button stops playback immediately.

---

## Controls and Shortcuts

* **Convert** button converts input to output.
* Radio buttons switch conversion direction and clear both text boxes.
* In **Morse to Text** mode, input is restricted to dots (`.`), dashes (`-`), slashes (`/`), spaces, and newlines.

## Example Input (Text to Morse)

```
Mary wanted to jump with Čika Mile.
Šaban Šaulić declined. Which is unfortunate.
He is 26 years old - very unhappy.
```

---

## Example Output (Morse)

```
-- .- .-. -.-- / .-- .- -. - . -.. / - --- / .--- ..- -- .--. / .-- .. - .... / -.-. .. -.- .- / -- .. .-.. . .-.-.-
... .- -... .- -. / ... .- ..- .-.. .. -.-. / -.. . -.-. .-.. .. -. . -.. .-.-.- / .-- .... .. -.-. .... / .. ... / ..- -. ..-. --- .-. - ..- -. .- - . .-.-.-
.... . / .. ... / ..--- -.... / -.-- . .- .-. ... / --- .-.. -.. / -....- / ...- . .-. -.-- / ..- -. .... .- .--. .--. -.-- .-.-.-
```

---

## About

* Written entirely in **Python** using **Tkinter** for GUI and **pygame** for audio playback.
* Handles extended Latin (Serbian) letters by normalization.
* Plays Morse code audio with dot and dash sounds, word and letter spacing.
* Open source and easy to modify.

---
![Morse Code Sample](/Morse-Code/morse.png "Sample Morse Code")
![Morse Code Sample](/Morse-Code/OIP.jpg "Sample Morse Code")
