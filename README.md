# Artdle 🎨🟩🟨⬛

### tldr:

**You need to install colorama by using this code.**
```bash
pip install -r requirements.txt
```

---

Artdle is a Python project that **recreates art patterns using Wordle rules**.  
You give it:
- **Today's Wordle answer**  
- A custom art pattern made of `c` (colored) and `b` (blank) tiles

It then finds valid 5-letter Wordle words that match your pattern — line by line — and outputs them to form your “Wordle art.”

---

## 📂 Project Structure

```text
artdle/
├── artdle.py              # Main CLI script
├── valid-wordle-words.txt # Valid wordle words
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🚀 How It Works

1. **Load Wordle words**  
   Reads all valid 5-letter Wordle words from `valid-wordle-words.txt`.

2. **Ask for today's Wordle answer**  
   You type in the real Wordle answer for the day.

3. **Design your art**  
   You enter each line of your art using:
   - `c` → Green-colored tile (letter in correct position)  
   - `b` → Blank/gray tile (letter not in that position)  
   Example for a heart shape:

4. **Find matching words**  
For each line, the program finds a valid Wordle word that fits your pattern.

5. **Display the result**  
Shows your final Wordle art made out of real valid Wordle words.

---

## 📦 Requirements

- Python **3.7+**
- colorama is required

---

## 🛠 Usage

``` bash
Today Wordle('x' to close the program): sword

Please input the art you want to recreate line by line (c = colored | b = blank)
Type 'x' to end early
Art line 1: cbccb
Art line 2: bccbb
Art line 3: x

====ANSWER====
Word 1: score  #'s', 'o', and 'r' will has green background
Word 2: awoke  #'w' and 'o' will has green background
