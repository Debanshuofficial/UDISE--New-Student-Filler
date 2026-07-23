You are a senior Python Desktop Application Architect and UI/UX Engineer with expertise in Tkinter, ttk, ttkbootstrap, modern desktop applications, and enterprise software.

Your task is to redesign ONLY the user interface of my existing Tkinter application.

================================================================================
🚨 CRITICAL REQUIREMENT - UI REDESIGN ONLY
================================================================================

THIS IS STRICTLY A UI REDESIGN TASK.

The application is already fully functional.

The backend has been tested and works correctly.

Your responsibility is ONLY to improve the user interface.

DO NOT change ANY application logic.

Think of this as renovating a house without touching the electrical wiring, plumbing, or foundation.

================================================================================
ABSOLUTE RULES
================================================================================

You MAY:

✔ Rearrange widgets
✔ Improve layouts
✔ Improve spacing
✔ Improve typography
✔ Improve colors
✔ Improve icons
✔ Improve Treeview styling
✔ Improve Notebook styling
✔ Improve status indicators
✔ Add cards
✔ Add progress bars
✔ Add better panels
✔ Add better navigation
✔ Add visual dashboards
✔ Improve resizing
✔ Improve responsiveness
✔ Improve usability
✔ Improve accessibility
✔ Improve alignment
✔ Add tooltips
✔ Add visual separators
✔ Improve scrollbars
✔ Improve animations where possible

You MUST NOT:

❌ Change browser automation
❌ Change JSON loading
❌ Change browser connection
❌ Change scanning
❌ Change field mapping
❌ Change writing process
❌ Change automation workflow
❌ Change business logic
❌ Change threading
❌ Change queues
❌ Change timers
❌ Change callbacks
❌ Change event handlers
❌ Change backend functions
❌ Rename methods
❌ Rename variables
❌ Rename classes
❌ Change APIs
❌ Change delays
❌ Change logging logic
❌ Change JSON structure
❌ Change data processing
❌ Remove existing functionality
❌ Replace existing automation

Every existing button MUST call exactly the same callback.

Every existing variable MUST remain unchanged.

Every existing thread MUST remain unchanged.

Every existing queue MUST remain unchanged.

Every backend function MUST remain unchanged.

If preserving the backend makes a UI decision difficult, adapt the UI around the backend.

DO NOT refactor backend code.

================================================================================
APPLICATION PURPOSE
================================================================================

Application Name

UDISE+ AutoFiller

Purpose

The application:

• Loads a JSON file containing student information.
• Connects to an already running Chrome browser.
• Scans the current UDISE+ webpage.
• Automatically maps webpage fields with JSON keys.
• Writes data into webpage fields.
• Processes hundreds of students continuously.

This is an operator productivity tool.

Priority:

1. Speed
2. Visibility
3. Monitoring
4. Easy debugging
5. Workflow clarity

================================================================================
DESIGN STYLE
================================================================================

Create a professional Windows desktop application similar to:

• Visual Studio Code
• GitHub Desktop
• JetBrains IDE
• Microsoft PowerToys
• Windows 11
• Modern Enterprise Dashboard

The application must NOT look like a traditional Tkinter application.

It should feel like professional commercial software.

================================================================================
TECHNOLOGY
================================================================================

Preferred

ttkbootstrap

Fallback

Modern ttk styling

Use grid() wherever practical.

Organize UI code into reusable methods.

Example

create_header()

create_toolbar()

create_dashboard()

create_student_panel()

create_status_panel()

create_main_tabs()

create_mapping_tab()

create_logs_tab()

create_statistics_tab()

create_debug_tab()

create_statusbar()

Keep UI code clean and modular.

================================================================================
WINDOW
================================================================================

Minimum Size

1200 x 800

Default

1400 x 900

Resizable

High DPI compatible

================================================================================
COLOR PALETTE
================================================================================

Background
#1E1E1E

Panels
#252526

Borders
#333333

Primary Blue
#3B82F6

Success
#22C55E

Warning
#F59E0B

Error
#EF4444

Text
#FFFFFF

Secondary Text
#B0B0B0

================================================================================
APPLICATION LAYOUT
================================================================================

The application should be divided into five sections.

────────────────────────────────────────────────────────

HEADER

Contains

Application Icon

UDISE+ AutoFiller

Subtitle

"by Debanshu Ghosh"

Right side

Connection indicator

Current Page

Settings button

About button

────────────────────────────────────────────────────────

TOOLBAR

Modern horizontal toolbar.

Buttons

📂 Load JSON

🌐 Launch Chrome

🔗 Connect

🔍 Scan

✍ Write

⏹ Stop

Every button keeps the SAME callback.

Only visual appearance changes.

Use icons.

Hover effects.

Disabled state.

Tooltips.

Equal size.

────────────────────────────────────────────────────────

TOP DASHBOARD

Split into three cards.

========================================================
CARD 1
CURRENT STUDENT
========================================================

Display

👤 Student Name

Gender

DOB

Admission Class

Aadhaar

Current Student

27 / 430

Large progress bar.

Current status badge.

========================================================
CARD 2
CURRENT SESSION
========================================================

Show

✔ JSON Loaded

✔ Browser Connected

✔ Current Page

✔ Fields Found

✔ Fields Written

✔ Students Completed

⚠ Warnings

❌ Errors

Elapsed Time

Remaining Time

========================================================
CARD 3
SYSTEM STATUS
========================================================

Always visible.

Live indicators.

This card should update automatically using the EXISTING backend states.

Display

📄 JSON File

🌐 Browser

🔍 Scanner

🔗 Field Mapping

✍ Writing Engine

📦 Student Data

🧠 Automation

📝 Logging

⚠ Errors

Current Process

Example

JSON File

🟢 Loaded

Browser

🟢 Connected

Scanner

🔵 Scanning

Writing

⚪ Idle

Automation

🟢 Ready

Errors

🟢 None

Current Process

Writing Student 27 / 430

================================================================================
STATUS COLORS
================================================================================

Gray

Idle

Blue

In Progress

Green

Ready

Connected

Loaded

Completed

Yellow

Waiting

Orange

Warning

Red

Error

Dark Gray

Disconnected

Use rounded status badges similar to GitHub.

Examples

🟢 READY

🔵 SCANNING

⚪ IDLE

🟡 WAITING

🟠 WARNING

🔴 ERROR

================================================================================
LIVE PROGRESS
================================================================================

Always display

Overall Student Progress

█████████████░░░░░

Student

218 / 430

Writing Progress

██████████░░░░░░

15 / 28 Fields

Current Field

Father Name

Current Activity

Writing...

Elapsed Time

Remaining Time

================================================================================
MAIN AREA
================================================================================

Use ttk.Notebook.

Tabs

Field Mapping

Logs

Statistics

Debug

================================================================================
FIELD MAPPING TAB
================================================================================

This should occupy most of the application.

Large Treeview.

Columns

Website Label

Website Selector

JSON Field

JSON Value

Status

Message

Requirements

Alternating row colors.

Large headers.

Resizable columns.

Sortable columns.

Hover highlight.

Double-click copies value.

Right-click menu

Copy Label

Copy JSON Field

Copy Value

Retry Write

Status icons

✔ Written

🟡 Ready

⚠ Missing

❌ Error

Show at least 25 visible rows.

================================================================================
LOG TAB
================================================================================

Move the existing log viewer into this tab.

Do NOT change logging backend.

Features

Search

Clear

Copy

Export

Auto-scroll

Timestamp

Color coded log levels

INFO

SUCCESS

WARNING

ERROR

Maximum 5000 retained entries.

================================================================================
STATISTICS TAB
================================================================================

Display cards.

Students Processed

Fields Written

Skipped

Errors

Warnings

Average Time

Estimated Remaining

Progress visualization if possible.

================================================================================
DEBUG TAB
================================================================================

Read-only information.

Detected HTML Field

Detected Label

XPath

CSS Selector

Matched JSON Key

Current Value

Screenshot placeholder

Useful for debugging mappings.

================================================================================
BOTTOM STATUS BAR
================================================================================

Persistent.

Left

Application Status

Center

Current Student

Right

Chrome Status

JSON Status

Memory Usage

Current Time

================================================================================
TREEVIEW STYLE
================================================================================

Modern enterprise appearance.

30px row height.

Large bold headers.

Alternating rows.

Professional scrollbar.

Resizable columns.

================================================================================
USER EXPERIENCE
================================================================================

UI must never freeze.

Respect existing threading.

Respect existing queues.

Respect existing callbacks.

Disable buttons while processing.

Show spinner while scanning.

Show progress while writing.

Show modern notifications.

Consistent spacing.

8–12 px padding.

================================================================================
IMPORTANT
================================================================================

The application already works.

Do NOT improve the backend.

Do NOT optimize the backend.

Do NOT replace working code.

Do NOT rewrite functions.

Do NOT change application behavior.

Do NOT rename methods.

Do NOT rename variables.

Do NOT modify callbacks.

Do NOT modify threading.

Do NOT modify queues.

Do NOT modify automation.

Do NOT modify scanning.

Do NOT modify browser communication.

Do NOT modify JSON processing.

Do NOT modify writing logic.

Only redesign the visual presentation layer.

The redesigned interface must be a drop-in replacement that looks like a premium enterprise Windows desktop application while remaining 100% functionally identical to the existing application.