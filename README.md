# Project-C
> This program is designed as a simple yet effective parental control tool to help manage and restrict access to specific websites or applications on your computer. It provides an automated way to block certain pages or programs based on predefined keywords, ensuring a safer and more controlled digital environment.

### Features
> Website and Application Monitoring: Continuously scans all open window titles for specific keywords associated with restricted websites or applications.

> Automatic Blocking: Instantly closes tabs or windows containing [banned keywords](https://raw.githubusercontent.com/zgndia/Project-C/refs/heads/main/banned_words.json) to prevent access.

> Background Operation: Runs silently in the background, periodically checking for restricted content without disturbing normal computer usage.

> Startup Integration: Automatically configures itself to run every time the computer starts, ensuring consistent protection.

> Self-Cleanup: Deletes its own installation files after setup to avoid unnecessary clutter or tampering.
### How It Works
> Monitoring: The program scans all currently open windows for titles containing restricted keywords.

> Detection: If a window matches one of the predefined banned keywords, the program identifies it as restricted.

> Action: The restricted window or tab is automatically closed using efficient system commands.

> Persistent Protection: The program ensures that it activates at every system startup by copying itself to the Windows Startup folder.
### Purpose
> This program was created to support parents and guardians in maintaining a controlled and safe digital environment for children. By automatically blocking access to predefined sites or applications, it helps enforce rules around internet usage and limits exposure to inappropriate content.

### Customization
> Keyword List: The program allows customization of banned keywords, giving parents full control over what content should be restricted.

> Adjustable Behavior: The program's behavior can be tailored to suit individual needs, such as extending the scan interval or adding specific websites to the block list.
### Notes
> The program requires Python to be installed on your system for proper functionality. (if you are using older versions, which isn't recommended.)
> Dependencies are installed automatically via the requirements.txt file during setup.
> Once set up, the program operates without any additional input but can be updated or customized as needed.
> This tool is a straightforward and reliable way to create a safer digital experience for your family, offering peace of mind for parents and guardians.
