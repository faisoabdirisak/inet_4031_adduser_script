#!/usr/bin/python3

# INET4031
# Author: Faiso Hussein
# Date Created: October 26, 2025
# Date Last Modified: October 26, 2025

# The 'os' module allows running operating system commands like adding users or setting passwords.
# The 're' module handles pattern matching using regular expressions.
# The 'sys' module enables reading input directly from standard input (stdin).
import os
import re
import sys


def main():
    # Loop through each line of input coming from stdin (usually piped from an input file)
    for line in sys.stdin:

        # This checks if a line begins with '#'. Such lines are comments in the input file and should be skipped.
        match = re.match("^#", line)

        # Strips leading/trailing whitespace and splits each valid line into fields separated by colons (:).
        # Each field represents specific user info: username, password, last name, first name, and group(s).
        fields = line.strip().split(':')

        # If the line is a comment or does not have exactly five fields, skip it.
        # Ensures only valid, properly formatted user records are processed.
        if match or len(fields) != 5:
            continue

        # Extract user information for creating accounts and filling GECOS data (used in /etc/passwd).
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # The fifth field (groups) may contain multiple groups separated by commas; split them into a list.
        groups = fields[4].split(',')

        # Display a message showing which account is being created.
        print("==> Creating account for %s..." % (username))

        # Build a Linux command to create the user with no initial password but with full GECOS information.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # print(cmd)
        # os.system(cmd)  # Uncomment to actually create the user.

        # Inform the user that the password is being set for the new account.
        print("==> Setting the password for %s..." % (username))

        # Construct a command that sets the password by piping it into the 'passwd' command.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # print(cmd)
        # os.system(cmd)  # Uncomment to actually set the password.

        # Add the user to each group listed, unless the group field is '-'.
        for group in groups:
            # Check if the group is not '-', meaning the user should be added to the specified group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print(cmd)
                # os.system(cmd)  # Uncomment to assign the user to the group.


if __name__ == '__main__':
    main()
