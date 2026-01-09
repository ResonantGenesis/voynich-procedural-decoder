# Voynich Procedural Renderer

**Is the Voynich Manuscript a book to be read, or a program to be executed?**

This repository contains a Python tool that tests the **"Physics/Procedural Hypothesis"** on the Voynich Manuscript. 

## The Hypothesis

Traditional linguistic analysis assumes the Voynich text is a natural language (Subject-Verb-Object). However, simple substitution ciphers have consistently failed for centuries.

This project proposes that the "text" is actually a **Procedural Algorithm** (similar to knitting patterns, weaving instructions, or star chart coordinates).
* **Words are Coordinates:** Tokens do not represent vocabulary, but geometric instructions $(r, \theta)$.
* **Prefixes are Operators:** The frequent prefix `4` (EVA `q`) is not a letter, but a function call (e.g., `ROTATE` or `NEXT_STEP`).
* **Suffixes are Variables:** Digits like `89`, `9`, and `8` represent magnitude or radius.

## Results

When the text is parsed as a set of polar coordinate instructions, it does not produce a straight line of text. It generates **spirals and concentric circles** that closely match the visual layout of the manuscript's cosmological diagrams (e.g., Folio 68r).

## Installation

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
