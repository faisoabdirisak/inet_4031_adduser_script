# `inet_4031_adduser_script`

## Program Description
This Python program automates the creation of user accounts on Ubuntu systems. Instead of manually running commands such as `adduser`, `passwd`, and `usermod`, the script executes them automatically using Python’s `subprocess` module. It simplifies user management and reduces the potential for manual errors.

---

## Program User Operation
The script automates the creation of new user accounts based on an input file provided by the user. For each line in the file, the program reads the user details and executes the necessary Linux commands (`adduser`, `passwd`, and `usermod`). Comments within the code explain the internal workings of each step.

### Input File Format
- Each line must include the following information separated by spaces:  
  `username password full_name [groups]`  
- Lines starting with `#` are treated as comments and skipped.  
- Blank lines are ignored.  
- If no groups are listed, the user will not be added to any additional groups.

---

### Command Execution
1. Ensure the Python script is executable:
```bash
chmod +x create-users.py
```
2. Run the script with the input file:
```bash
./create-users.py < createusers.input
```
The script will read the user data from the specified input file and create the accounts accordingly.

---

### Dry Run Option
The script includes a **“dry run”** mode. When enabled, it displays the commands that **would be executed** without making any actual changes to the system. This allows users to safely review and verify the process before performing the actual account creation.

