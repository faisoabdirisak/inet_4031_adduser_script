#!/usr/bin/python3

# INET4031
# Author: Faiso Hussein
# Date Created: October 27, 2025
# Date Last Modified: October 27, 2025

import os
import re
import sys

def main():
    # Prompt user to choose dry-run mode
    # Y = dry-run (commands will NOT be executed)
    # N = normal run (commands WILL be executed)
    dry_run_input = input("Would you like to run in dry-run mode? (Y/N): ").strip().upper()
    dry_run = dry_run_input == 'Y'

    # Inform user about chosen mode
    if dry_run:
        print("** Running in dry-run mode: OS commands will NOT be executed. **\n")
    else:
        print("** Running normally: OS commands WILL be executed. **\n")

    # Loop through each line of input (usually piped from a file)
    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()

        # Skip empty lines
        if not line:
            if dry_run:
                # Dry-run: inform user that a blank line was skipped
                print(f"Line {line_number}: Skipped blank line.")
            continue

        # Check if line is a comment (starts with #)
        match = re.match("^#", line)
        if match:
            if dry_run:
                # Dry-run: inform user that a comment line was skipped
                print(f"Line {line_number}: Skipped comment line.")
            continue

        # Split line into fields separated by colons
        fields = line.split(':')
        if len(fields) != 5:
            if dry_run:
                # Dry-run: print an error message for invalid line
                print(f"Line {line_number}: ERROR - Expected 5 fields, found {len(fields)}. Line skipped.")
            # In normal mode, silently skip invalid lines
            continue

        # Extract user info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # GECOS format: First Last,,,
        groups = fields[4].split(',')

        # Inform about account creation
        print(f"==> Creating account for {username}...")

        # Build adduser command
        add_user_cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        if dry_run:
            # Dry-run: show the command that would be executed
            print(f"[DRY-RUN] Command: {add_user_cmd}")
        else:
            # Normal run: execute the command
            os.system(add_user_cmd)

        # Set the password
        print(f"==> Setting the password for {username}...")
        set_pass_cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        if dry_run:
            print(f"[DRY-RUN] Command: {set_pass_cmd}")
        else:
            os.system(set_pass_cmd)

        # Add user to groups
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                add_group_cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run:
                    print(f"[DRY-RUN] Command: {add_group_cmd}")
                else:
                    os.system(add_group_cmd)


if __name__ == '__main__':
    main()

