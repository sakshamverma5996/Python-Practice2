# The sample string we will work with
text = "  python is Amazing, isn't it?  "

print(f"Original: '{text}'\n")

# --- 1. CASE TRANSFORMATIONS ---
print("## 1. Case Transformations")
print(f"Uppercase:      {text.upper()}")
print(f"Lowercase:      {text.lower()}")
print(f"Title Case:     {text.title()}")
print(f"Capitalize:     {text.strip().capitalize()}") # Stripped to see effect
print(f"Swap Case:      {text.swapcase()}")

# --- 2. CLEANING & PADDING ---
print("\n## 2. Cleaning & Padding")
print(f"Strip (both):   '{text.strip()}'")
print(f"L-Strip:        '{text.lstrip()}'") # Removes leading spaces
print(f"Center:         '{text.strip().center(30, '*')}'")
print(f"L-Justify:      '{text.strip().ljust(30, '-')}'")

# --- 3. SEARCHING & COUNTING ---
print("\n## 3. Searching & Counting")
print(f"Count 'i':      {text.count('i')}")
print(f"Find 'is':      {text.find('is')} (index of first match)")
print(f"Starts with ' ': {text.startswith(' ')}")
print(f"Ends with '?':   {text.strip().endswith('?')}")

# --- 4. REPLACEMENT & SPLITTING ---
print("\n## 4. Replacement & Splitting")
# Replace 'Amazing' with 'Incredible'
replaced = text.replace("Amazing", "Incredible")
print(f"Replace:        {replaced.strip()}")

# Split into a list based on a delimiter
words = text.strip().split(" ")
print(f"Split (list):   {words}")

# Join a list back into a string
joined = "-".join(words)
print(f"Joined:         {joined}")

# --- 5. CHARACTER CHECKS (BOOLEANS) ---
print("\n## 5. Character Checks")
alpha_test = "Python3"
print(f"Is '{alpha_test}' Alpha-Numeric? {alpha_test.isalnum()}")
print(f"Is '12345' Digit?            {'12345'.isdigit()}")
print(f"Is '   ' Space?              {'   '.isspace()}")

# --- 6. SLICING (The Pythonic Way) ---
print("\n## 6. Slicing [start:stop:step]")
clean_text = text.strip()
print(f"First 6 chars:  {clean_text[:6]}")
print(f"Reverse string: {clean_text[::-1]}")
print(f"Every 2nd char: {clean_text[::2]}")