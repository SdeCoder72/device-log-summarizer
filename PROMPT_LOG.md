# Prompt Log

**Tool Used:** Claude, Perplexity

---
## 1. Initial prompt
> Write a Python script that loads given JSON output and generates a bar chart comparing the average temperature >per device using matplotlib
>
> (I also pasted my summary.json sample with DEV_A and DEV_C.)

---
## 2. Bug in the first attempt
- I think the most common one : The script read "device_summary.json", but my file is "summary.json", so it crashed with FileNotFoundError.
- No error handling for a missing or invalid JSON file
- The value label above the tallest bar was close to the top edge 
- X-axis labels overlaps with many devices 

---
## 3. Follow-up prompt 
**Bug 1:** File ka name "device_summary.json" se "summary.json" kar do.  
**Bug 2:** koi error handling nahi. File na ho, JSON kharab ho, ya list khali ho, to script crash karti hai ya khali chart banati hai. use try/except.  
**Bug 3:** x-axis labels overlap ho rahi hai jyada devices par. Abhi 2-3 devices pe theek tha, par 10 devices add kiye to name overlap ho rahe hai.  
**Bug 4:** upar ka text kat sakta hai. Sabse highest bar ka number, chart ki top edge se touch ho sakta hai. Y-axis ki limit ko max se thoda upar rakho.  
**Bug 5:** encoding missing. open() mein encoding="utf-8" nahi hai. 

Fix it.

---
## 4. What I changes / verified myself
- Fixed INPUT_FILE to match my main.py output
- Ran the script and checked average_temperature_by_device.png