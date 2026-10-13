# AI Flip Font
AI Flip Font is a Python program that creates text intended to be readable to humans but not LLMs. Unlike many of the other techniques for doing this, Flip Font outputs text you can simply copy and paste.
## How does it work?
Unicode bidirectional (bidi) control characters change the direction in which text is displayed. They were originally intended for use in switching to and back from languages that display right to left, but are somewhat obsolete today. Among others, they include U+202E (right to left override) and U+202D (left to right override), the two of which are the characters I use in this project. AI flip font works simply by adding the first X letters of the text, inserting a 202E, flipping the rest of the text and adding the next X letters, inserting a 202D, and repeating until the whole string has been converted. Humans read the text perfectly, as the bidi characters render on the display. But some AI systems trim these characters out for security reason as they can be used to inject malicious payloads. For example:
```
          "Hello, World!"
                |
                V
Program - Flips and inserts bidi chars
                |
                V
           Hel‮!dl‭lo ‮roW‭
Appears to human as "Hello World!"
Appears to LLM as "Hel!dllo roW"
```
## How well does it work?
Unfortunately, most LLMs have stopped stripping bidi characters from inputs, so it's not as effective as when I first started working on this. There are a few minor bugs which I am working on. I'm planning on building a website so anyone can run this online. In the meantime please star this project and follow!
