# UDISE+ AutoFiller — Enterprise UI Redesign Specification

## ROLE

You are a Senior Python Desktop Application Architect and UI/UX Engineer specializing in:

- Tkinter
- ttk
- ttkbootstrap
- Enterprise Desktop Applications
- Windows UI Design
- Productivity Software

Your task is to redesign **ONLY** the graphical user interface of my existing Tkinter application.

---

# 🚨 CRITICAL REQUIREMENT — UI REDESIGN ONLY

This is **STRICTLY** a UI redesign project.

The application is already working correctly.

The backend has been tested and is considered production-ready.

Your responsibility is ONLY to redesign the user interface.

## Think of this as

Replacing the dashboard of a car while leaving the engine, wiring, transmission, brakes, and electronics untouched.

---

# ABSOLUTE RULES

## ✅ You MAY

- Rearrange widgets
- Improve layouts
- Improve spacing
- Improve typography
- Improve colors
- Improve icons
- Improve Treeview appearance
- Improve Notebook appearance
- Improve button styling
- Improve status indicators
- Add cards
- Add separators
- Add progress bars
- Add modern scrollbars
- Add tooltips
- Add status dashboard
- Improve resizing
- Improve responsiveness
- Improve usability
- Improve accessibility
- Improve alignment
- Add animations (UI only)

---

## ❌ You MUST NOT

- Modify automation logic
- Modify browser automation
- Modify Playwright/Selenium
- Modify Chrome connection
- Modify JSON parsing
- Modify scanning
- Modify field mapping
- Modify writing logic
- Modify validation logic
- Modify logging logic
- Modify business logic
- Modify threading
- Modify queues
- Modify timers
- Modify delays
- Modify callbacks
- Modify event handlers
- Modify APIs
- Modify JSON structure
- Rename methods
- Rename classes
- Rename variables
- Remove existing functionality
- Replace backend implementations
- Change application workflow

Every existing callback must remain exactly the same.

Every button must call exactly the same function.

Every backend method must remain untouched.

Only the presentation layer may change.

---

# APPLICATION PURPOSE

Application Name

**UDISE+ AutoFiller**

Purpose

The software

- Loads a JSON file
- Connects to Chrome
- Scans the current UDISE+ page
- Maps webpage fields with JSON keys
- Writes student data
- Verifies completion

---

# IMPORTANT WORKFLOW

This application processes **ONE STUDENT AT A TIME**.

The operator manually selects a JSON file.

Each JSON file contains data for exactly one student.

After the student has been written successfully, another JSON file is loaded manually.

This is **NOT** a batch-processing application.

---

# DO NOT SHOW

- Student 27 / 430
- Students Processed
- Total Students
- Queue
- Batch Progress
- Remaining Students
- Batch Statistics

These are not applicable.

---

# OPTIMIZE THE UI FOR

Load JSON

↓

Connect Browser

↓

Scan Page

↓

Map Fields

↓

Write Student Data

↓

Verify

↓

Load Next Student JSON

---

# DESIGN STYLE

The interface should resemble professional desktop software such as

- Visual Studio Code
- GitHub Desktop
- JetBrains IDE
- Microsoft PowerToys
- Windows 11
- Modern Enterprise Dashboard

Avoid the appearance of traditional Tkinter applications.

---

# TECHNOLOGY

Preferred

- ttkbootstrap

Fallback

- themed ttk

Use

- grid()
- PanedWindow
- Notebook
- reusable widgets

Create modular UI methods such as

```
create_header()

create_toolbar()

create_dashboard()

create_student_card()

create_status_card()

create_main_tabs()

create_mapping_tab()

create_logs_tab()

create_debug_tab()

create_statusbar()
```

---

# WINDOW

Minimum

1200 × 800

Default

1400 × 900

Resizable

High DPI Compatible

---

# COLOR PALETTE

Background

```
#1E1E1E
```

Panels

```
#252526
```

Borders

```
#333333
```

Primary

```
#3B82F6
```

Success

```
#22C55E
```

Warning

```
#F59E0B
```

Error

```
#EF4444
```

Text

```
#FFFFFF
```

Secondary Text

```
#B0B0B0
```

---

# APPLICATION LAYOUT

```
┌──────────────────────────────────────────────────────────────┐
│ Header                                                       │
├──────────────────────────────────────────────────────────────┤
│ Toolbar                                                      │
├──────────────────────────────────────────────────────────────┤
│ Student Card │ Session Card │ System Status Dashboard        │
├──────────────────────────────────────────────────────────────┤
│                                                      │
│              Notebook (Main Working Area)            │
│                                                      │
├──────────────────────────────────────────────────────────────┤
│ Status Bar                                                   │
└──────────────────────────────────────────────────────────────┘
```

---

# HEADER

Display

Application Icon

UDISE+ AutoFiller

Subtitle

```
by Debanshu Ghosh
```

Right Side

- Browser Status
- Current Page
- Settings
- About

---

# TOOLBAR

Modern horizontal toolbar.

Buttons

📂 Load JSON

🌐 Launch Chrome

🔗 Connect

🔍 Scan

✍ Write

⏹ Stop

Requirements

- Same callbacks
- Same backend
- Icons
- Tooltips
- Hover effects
- Disabled state
- Equal size

---

# DASHBOARD

Three cards.

---

## CARD 1

# CURRENT STUDENT

Display

👤 Student Name

Gender

DOB

Admission Class

Aadhaar

Student Status

Examples

🟢 Ready

🔵 Scanning

🔵 Writing

🟢 Completed

🟡 Waiting

🔴 Error

---

## CARD 2

# SESSION INFORMATION

Display

✔ JSON Loaded

✔ Browser Connected

✔ Current Page

✔ Fields Detected

✔ Fields Mapped

✔ Fields Written

✔ Missing Fields

✔ Errors

Elapsed Time

Current Activity

---

## CARD 3

# LIVE SYSTEM STATUS

Always visible.

This dashboard must display the real-time status of every important component.

Use ONLY existing backend states.

Do NOT create new backend logic.

Display

📄 JSON File

🌐 Browser

🔍 Scanner

🔗 Field Mapping

✍ Writing Engine

🧠 Automation

📝 Logging

⚠ Error Monitor

Current Process

Example

```
JSON File
🟢 Loaded

Browser
🟢 Connected

Scanner
🔵 Scanning

Field Mapping
🟢 Ready

Writing
⚪ Idle

Automation
🟢 Ready

Logging
🟢 Active

Errors
🟢 None

Current Process

Writing Father's Name
```

---

# STATUS COLORS

Gray

Idle

Blue

Running

Green

Ready

Loaded

Connected

Completed

Yellow

Waiting

Orange

Warning

Red

Error

Dark Gray

Disconnected

Use modern rounded badges.

Examples

🟢 READY

🔵 WRITING

🟡 WAITING

🟠 WARNING

🔴 ERROR

⚪ IDLE

---

# FIELD WRITING PROGRESS

Since the application processes ONE student only,

display progress for the CURRENT STUDENT'S fields.

Example

```
Field Writing Progress

████████████████░░░░

18 / 25 Fields Written

72%
```

Display

Total Fields

Written

Remaining

Skipped

Failed

Missing

Current Field

Current Action

Elapsed Time

Status

Example

```
Current Field

Father Name

Current Action

Writing...

Elapsed

00:00:17
```

When complete

```
████████████████████

25 / 25

🟢 Completed Successfully
```

---

# NOTEBOOK

Tabs

📋 Field Mapping

📜 Logs

🛠 Debug

(No Statistics tab, as the application is single-student oriented.)

---

# FIELD MAPPING TAB

This is the primary workspace.

Large Treeview.

Columns

Website Label

Website Selector

JSON Field

JSON Value

Status

Message

Requirements

- Large headers
- Alternating rows
- 30 px row height
- Resizable columns
- Sortable columns
- Smooth scrolling
- Modern scrollbar

Status icons

✔ Written

🟡 Ready

⚠ Missing

❌ Error

Right Click

Copy Website Label

Copy JSON Key

Copy Value

Retry Write

Double Click

Copy value

Minimum

25 visible rows.

---

# LOGS TAB

Move the existing log viewer here.

Do NOT change backend logging.

Features

- Search
- Clear
- Export
- Copy
- Auto Scroll
- Timestamp

Example

```
[12:42:11]

Connected to Chrome
```

Color Levels

Blue

INFO

Green

SUCCESS

Orange

WARNING

Red

ERROR

Keep

Maximum

5000 entries.

---

# DEBUG TAB

Display

Detected HTML Field

Detected Label

XPath

CSS Selector

Matched JSON Key

Current Value

Screenshot Placeholder

Read-only.

Useful for troubleshooting.

---

# STATUS BAR

Persistent.

Left

Application Status

Center

Current Activity

Right

Chrome

JSON

Memory Usage

Clock

---

# TREEVIEW STYLE

Professional.

Row Height

30 px

Bold Headers

Alternating Colors

Resizable

Modern Scrollbars

Hover Highlight (if practical)

---

# USER EXPERIENCE

The UI must NEVER freeze.

Respect

Existing Threads

Existing Queues

Existing Events

Disable buttons during operations.

Show spinner during scanning.

Show progress while writing.

Show non-blocking notifications.

Use

8–12 px spacing.

---

# CODE ORGANIZATION

Separate UI into methods.

Example

```
create_header()

create_toolbar()

create_dashboard()

create_student_card()

create_session_card()

create_status_dashboard()

create_mapping_tab()

create_logs_tab()

create_debug_tab()

create_statusbar()
```

Keep code clean.

Avoid duplication.

---

# FINAL REQUIREMENTS

The application must remain **100% functionally identical**.

Do not touch backend logic.

Do not touch automation.

Do not touch browser communication.

Do not touch Playwright/Selenium.

Do not touch JSON parsing.

Do not touch threading.

Do not touch callbacks.

Do not touch queues.

Do not touch variables.

Do not rename methods.

Do not change application workflow.

Only redesign the presentation layer.

The final result should look like a polished enterprise-grade Windows desktop application that users can operate efficiently for processing one student at a time, with a clean, modern interface and comprehensive live status indicators.