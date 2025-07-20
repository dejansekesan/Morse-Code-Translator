# Variant - Morse Code Converter
 
   A feature-rich Morse code translator built with Python, featuring a clean GUI,
   real-time conversion, and a unique interactive audio player.
   
   ![Morse Code Sample](
   https://raw.githubusercontent.com/zihajlo/Morse-Code/main/morse.png "Application 
   Screenshot")
   
   ---
   
   ## ✨ Features
   
   *   **Bidirectional Conversion:** Translate from Text to Morse and Morse to Text in
   real-time.
   *   **Interactive Audio Playback:** A unique audio player that allows you to pause,
      stop, and resume playback from any position using your cursor.
   *   **Adjustable Audio:** Control the playback speed, inter-character gap, and
   volume with intuitive sliders.
   *   **Serbian Latin Support:** Correctly normalizes extended Latin characters (š,
   đ, č, ć, ž) for accurate conversion.
   *   **Modern UI:** A clean, themed interface built with Tkinter.
   *   **Cross-Platform:** Runs on any system with Python. Packaged binaries are also
   available.
   *   **Full Keyboard Control:** Includes standard editing shortcuts for a smoot workflow.
   
   ---
  
   ## 🚀 Getting Started
   
   ### Running from Source
   
   1.  **Prerequisites:** Ensure you have Python 3 installed.
   2.  **Install Dependencies:** This project uses `pygame` for audio playback.
      Install it via pip:

      pip install pygame


   3.  **Run the App:**

      python3 ./morse.py


   
   ### Using the Binary
   Download the compiled binary for your operating system from the **Releases**
  section on GitHub and run it directly.
   
   ---
  
   ## 📖 How to Use
   
   ### Main Interface
   1.  **Select Mode:** Use the radio buttons at the top to choose between **Text to
   Morse** or **Morse to Text**. The text boxes will clear automatically.
   2.  **Input Text:** Type or paste your text into the "Input" box.
   3.  **Convert:** Click the **Convert** button to see the translation in the
   "Output" box.
   
   ### Interactive Audio Player
   The audio player gives you precise control over the playback. It plays the Morse
      code from the correct text box depending on the selected mode.
   
   *   **Play:** Starts playback from the beginning of the text. If playback is
   already active, it does nothing.
   *   **Pause / Resume at Cursor:**
       *   Clicking **Pause** will freeze the playback, and the button's text will
   change to **"Resume at Cursor"**.
       *   To resume, move your cursor and click anywhere in the Morse code text.
       *   Click **"Resume at Cursor"**, and playback will continue from your new
   cursor position.
   *   **Stop:** Immediately stops playback and resets the position to the beginning.
   *   **Sliders:**
       *   **Volume:** Adjusts the beep volume.
       *   **Speed:** Controls the duration of dots and dashes (lower is faster).
       *   **Gap:** Adds extra time between each dot or dash, allowing you to slow
   down the playback for clarity.
   
   ### Keyboard Shortcuts
   Standard text editing shortcuts are available in both input and output boxes.
    
   | Shortcut      | Action         |
   |---------------|----------------|
   | `Ctrl + A`    | Select All     |
   | `Ctrl + C`    | Copy           |
   | `Ctrl + V`    | Paste          |
   | `Ctrl + X`    | Cut            |
   | `Ctrl + Z`    | Undo           |
   | `Ctrl + Y`    | Redo           |
   
   ---
  
   ## 📝 Morse Code Syntax Rules
  
   ### Text to Morse
   > When converting from plain text to Morse code:
   > *   Spaces between words are translated to `/`.
   > *   Newlines are preserved and create a long pause during audio playback.
   > *   Serbian special letters are normalized: `š`→`s`, `đ`→`dj`, `č`→`c`, `ć`→`c`,
      `ž`→`z`.
   > *   Any character not in the Morse dictionary is skipped (see below pictures).
  
   ### Morse to Text
   > When converting from Morse code to plain text:
   > *   Morse characters (dots and dashes) for a single letter must not have spaces
      between them (e.g., `.-` is 'A').
   > *   Each letter's Morse code must be separated by a single space (e.g., `.... . 
      .-.. .-.. ---`).
   > *   A slash (`/`) is used to represent a space between words.
   
  ---
   
   ## 💡 Example
   
   #### Input (Text to Morse)
```
  Mary wanted to jump with Čika Mile.
  Šaban Šaulić declined. Which is unfortunate.
  He is 26 years old - very unhappy.
```
  
  ---

  
  #### Output (Morse)
```
  -- .- .-. -.-- / .-- .- -. - . -.. / - --- / .--- ..- -- .--. / .-- .. - .... / -.-. .. -.- .-
   / -- .. .-.. . .-.-.-
  ... .- -... .- -. / ... .- ..- .-.. .. -.-. / -.. . -.-. .-.. .. -. . -.. .-.-.- / .-- .... ..
   -.-. .... / .. ... / ..- -. ..-. --- .-. - ..- -. .- - . .-.-.-
  .... . / .. ... / ..--- -.... / -.-- . .- .-. ... / --- .-.. -.. / -....- / ...- . .-. -.-- /
  ..- -. .... .- .--. .--. -.-- .-.-.-

```
  
 ---
 
 ## 🛠️ About
 
 *   Written entirely in **Python**.
 *   GUI built with the standard **Tkinter** library.
 *   Audio playback powered by **pygame**.
 *   Open source and easy to modify.

 ## 📷 Photos

![Morse Code Sample](/Morse-Code/morse.png "Sample Morse Code")
![Morse Code Sample](/Morse-Code/OIP.jpg "Sample Morse Code")
