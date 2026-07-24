import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import os
import sys
from models.new_student import NewStudent
from storage.json_loader import JsonLoader
from utils.logger import AppLogger
from browser.browser_controller import BrowserController
from browser.udise_automation import UdiseNewStudentAutomation


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("UDISE+ AutoFiller By Debanshu Ghosh")
        self.geometry("800x850")

        # Core components
        self.logger = AppLogger()
        self.browser_ctrl = BrowserController(self.logger)
        self.automation = None
        self.current_student: NewStudent = None

        self._setup_ui()
        self.logger.set_ui_callback(self._log_to_ui)

        self.logger.info("Application Started. Please select a JSON file.")

    def _setup_ui(self):
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # ── Fonts ─────────────────────────────────────────────────────────────
        title_font    = ctk.CTkFont(family="Segoe UI", size=22, weight="bold")
        heading_font  = ctk.CTkFont(family="Segoe UI", size=16, weight="bold")
        body_font     = ctk.CTkFont(family="Segoe UI", size=12)
        btn_font      = ctk.CTkFont(family="Segoe UI", size=11, weight="bold")
        label_font    = ctk.CTkFont(family="Segoe UI", size=11)
        mono_font     = ctk.CTkFont(family="Consolas",  size=10)

        # ══════════════════════════════════════════════════════════════════════
        # 1. STICKY TOP HEADER
        # ══════════════════════════════════════════════════════════════════════
        header = ctk.CTkFrame(self, fg_color="#0d0d0d", corner_radius=0)
        header.pack(fill="x", side="top")

        header_inner = ctk.CTkFrame(header, fg_color="transparent")
        header_inner.pack(fill="both", expand=True, padx=20)

        # Left — logo + title
        left = ctk.CTkFrame(header_inner, fg_color="transparent")
        left.pack(side="left", fill="y", pady=12)
        ctk.CTkLabel(
            left, text="🎓  UDISE+ AutoFiller",
            font=title_font, text_color="#3a86ff",
        ).pack(side="left", padx=(0, 8))
        ctk.CTkLabel(
            left, text="by Debanshu Ghosh",
            font=body_font, text_color="white",
        ).pack(side="left", pady=(8, 0))

        # Right — redesigned Chrome pill button
        ctk.CTkButton(
            header_inner,
            text="🌐   Launch Chrome",
            command=self._launch_chrome,
            fg_color="#071a0f",
            hover_color="#0a2e1a",
            text_color="#1db954",
            font=btn_font,
            corner_radius=24,
            height=40,
            width=170,
            border_width=1,
            border_color="#1db954"
        ).pack(side="right", pady=12)

        # Thin accent line under header
        ctk.CTkFrame(self, fg_color="#1db954", height=2, corner_radius=0).pack(fill="x", side="top")

        # ══════════════════════════════════════════════════════════════════════
        # 2. LED INDICATOR STRIP  (just below header)
        # ══════════════════════════════════════════════════════════════════════
        led_bar = ctk.CTkFrame(self, fg_color="#111111", corner_radius=0, height=44)
        led_bar.pack(fill="x", side="top")
        led_bar.pack_propagate(False)

        led_inner = ctk.CTkFrame(led_bar, fg_color="transparent")
        led_inner.pack(expand=True, fill="y")

        def _make_led(parent, label_text):
            dot = ctk.CTkLabel(parent, text="⬤", font=ctk.CTkFont(size=12), text_color="#2a2a2a")
            dot.pack(side="left", padx=(18, 4))
            ctk.CTkLabel(parent, text=label_text, font=label_font, text_color="white").pack(side="left", padx=(0, 8))
            return dot

        self.led_json_ind     = _make_led(led_inner, "JSON Loaded")
        self.led_browser_ind  = _make_led(led_inner, "Browser Connected")
        self.led_ready_ind    = _make_led(led_inner, "Ready")
        self.led_progress_ind = _make_led(led_inner, "")
        self.led_progress_lbl = ctk.CTkLabel(led_inner, text="Idle", font=label_font, text_color="white")
        self.led_progress_lbl.pack(side="left", padx=(0, 18))

        # Divider under LED strip
        ctk.CTkFrame(self, fg_color="#1a1a1a", height=1, corner_radius=0).pack(fill="x", side="top")

        # ══════════════════════════════════════════════════════════════════════
        # 3. STICKY BOTTOM ACTION BAR  (pack BEFORE main so it anchors bottom)
        # ══════════════════════════════════════════════════════════════════════
        ctk.CTkFrame(self, fg_color="#1a1a1a", height=1, corner_radius=0).pack(fill="x", side="bottom")

        bottom_bar = ctk.CTkFrame(self, fg_color="#0d0d0d", corner_radius=0)
        bottom_bar.pack(fill="x", side="bottom")

        bar_inner = ctk.CTkFrame(bottom_bar, fg_color="transparent")
        bar_inner.pack(fill="both", expand=True, padx=16, pady=10)

        # File name display (left side)
        self.json_path_var = ctk.StringVar(value="No file selected")
        ctk.CTkLabel(
            bar_inner,
            textvariable=self.json_path_var,
            font=mono_font,
            text_color="white",
            anchor="w",
            width=200,
        ).pack(side="left", padx=(0, 12))

        # ── Buttons ────────────────────────────────────────────────────────
        btn_frame = ctk.CTkFrame(bar_inner, fg_color="transparent")
        btn_frame.pack(side="right")

        # 1. Load JSON — blue tint
        ctk.CTkButton(
            btn_frame,
            text="📂  Load JSON",
            command=self._browse_json,
            fg_color="#0e2240",
            hover_color="#163460",
            text_color="#60a5fa",
            font=btn_font,
            corner_radius=10,
            height=36,
            width=160,
        ).grid(row=0, column=0, padx=4, pady=4)

        # 3. Scan Page — amber tint
        self.btn_scan = ctk.CTkButton(
            btn_frame,
            text="🔍  Scan Page",
            command=self._scan_page,
            state="disabled",
            fg_color="#1e1400",
            hover_color="#2d1e00",
            text_color="#fbbf24",
            font=btn_font,
            corner_radius=10,
            height=36,
            width=160,
        )
        self.btn_scan.grid(row=0, column=1, padx=4, pady=4)

        # 2. Connect & Scan — green tint
        self.btn_connect = ctk.CTkButton(
            btn_frame,
            text="🔗  Connect & Scan",
            command=self._check_connection,
            fg_color="#0a2218",
            hover_color="#0f3323",
            text_color="#4ade80",
            font=btn_font,
            corner_radius=10,
            height=36,
            width=160,
        )
        self.btn_connect.grid(row=1, column=0, padx=4, pady=4)

        # 4. Write Data — purple tint
        self.btn_write = ctk.CTkButton(
            btn_frame,
            text="✍  Write Data",
            command=self._write_data,
            state="disabled",
            fg_color="#1a0a2e",
            hover_color="#280f44",
            text_color="#c084fc",
            font=btn_font,
            corner_radius=10,
            height=36,
            width=160,
        )
        self.btn_write.grid(row=1, column=1, padx=4, pady=4)

        # ══════════════════════════════════════════════════════════════════════
        # 4. MAIN CONTENT
        # ══════════════════════════════════════════════════════════════════════
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=(12, 8))

        # — Student / connection info bar ——————————————————————————————————
        info_bar = ctk.CTkFrame(
            main_frame, fg_color="#141414",
            corner_radius=12, border_width=1, border_color="#222222",
        )
        info_bar.pack(fill="x", pady=(0, 14))

        self.student_name_lbl = ctk.CTkLabel(
            info_bar,
            text="👤  Student Name: —",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color="#3a86ff",
        )
        self.student_name_lbl.pack(side="left", padx=16, pady=14)

        self.browser_status_lbl = ctk.CTkLabel(
            info_bar,
            text="🔴  Not Connected",
            font=label_font,
            text_color="white",
        )
        self.browser_status_lbl.pack(side="right", padx=16, pady=14)

        # — Tabview ————————————————————————————————————————————————————————
        self.tabview = ctk.CTkTabview(main_frame, corner_radius=12, fg_color="#141414", border_width=0, segmented_button_fg_color="#141414")
        self.tabview.pack(fill="both", expand=True)

        tab_json = self.tabview.add("JSON")
        tab_mapping = self.tabview.add("Field Mapping")
        tab_logs = self.tabview.add("Execution Logs")

        # — Field Mapping Table (Tab 1) ————————————————————————————————————
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#1a1a1a", foreground="#e0e0e0",
                        fieldbackground="#1a1a1a", rowheight=38,
                        borderwidth=0, font=("Segoe UI", 12))
        style.configure("Treeview.Heading",
                        background="#0a3a6e", foreground="white",
                        borderwidth=0, font=("Segoe UI", 12, "bold"))
        style.map("Treeview", background=[("selected", "#1d4ed8")])

        table_frame = ctk.CTkFrame(tab_mapping, fg_color="transparent")
        table_frame.pack(fill="both", expand=True, pady=(10, 0))

        columns = ("site_label", "json_field", "json_value", "status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        self.tree.heading("site_label", text="Website Field Label")
        self.tree.heading("json_field",  text="JSON Field Name")
        self.tree.heading("json_value",  text="JSON Value")
        self.tree.heading("status",      text="Status")

        self.tree.column("site_label", width=210, anchor="w")
        self.tree.column("json_field",  width=140, anchor="center")
        self.tree.column("json_value",  width=160, anchor="center")
        self.tree.column("status",      width=120, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # — Logs (Tab 2) ———————————————————————————————————————————————————
        log_frame = ctk.CTkFrame(tab_logs, fg_color="transparent")
        log_frame.pack(fill="both", expand=True, pady=(10, 0))

        self.log_box = ctk.CTkTextbox(
            log_frame,
            font=("Consolas", 11),
            fg_color="#0e0e0e",
            text_color="#d4d4d4",
            corner_radius=8,
        )
        self.log_box.pack(fill="both", expand=True)
        self.log_box.configure(state="disabled")

        # — JSON (Tab 3) ———————————————————————————————————————————————————
        json_frame = ctk.CTkFrame(tab_json, fg_color="transparent")
        json_frame.pack(fill="both", expand=True, pady=(10, 0))

        self.json_edit_box = ctk.CTkTextbox(
            json_frame,
            font=("Consolas", 11),
            fg_color="#0e0e0e",
            text_color="#d4d4d4",
            corner_radius=8,
        )
        self.json_edit_box.pack(fill="both", expand=True, pady=(0, 10))

        ctk.CTkButton(
            json_frame,
            text="Apply Pasted JSON",
            command=self._apply_pasted_json,
            fg_color="#0a3d1f",
            hover_color="#0f5c2e",
            text_color="#1aff6b",
            font=btn_font,
            corner_radius=8,
            height=36,
        ).pack(side="right")

    # ═════════════════════════════════════════════════════════════════════════
    # LED UPDATER
    # ═════════════════════════════════════════════════════════════════════════
    def _update_leds(self, in_progress=False, has_error=False):
        COLOR_OFF    = "#2a2a2a"
        COLOR_GREEN  = "#22c55e"
        COLOR_RED    = "#ef4444"
        COLOR_YELLOW = "#f59e0b"

        self.led_json_ind.configure(
            text_color=COLOR_GREEN if self.current_student else COLOR_OFF)

        self.led_browser_ind.configure(
            text_color=COLOR_GREEN if self.browser_ctrl.connected else COLOR_OFF)

        is_ready = bool(self.current_student and self.browser_ctrl.connected and self.automation)
        self.led_ready_ind.configure(
            text_color=COLOR_GREEN if (is_ready and not in_progress and not has_error) else COLOR_OFF)

        if has_error:
            self.led_progress_ind.configure(text_color=COLOR_RED)
            self.led_progress_lbl.configure(text="Error", text_color=COLOR_RED)
        elif in_progress:
            self.led_progress_ind.configure(text_color=COLOR_YELLOW)
            self.led_progress_lbl.configure(text="In Progress", text_color=COLOR_YELLOW)
        else:
            self.led_progress_ind.configure(text_color=COLOR_GREEN)
            self.led_progress_lbl.configure(text="Idle", text_color="white")

    # ═════════════════════════════════════════════════════════════════════════
    # LOG CALLBACK
    # ═════════════════════════════════════════════════════════════════════════
    def _log_to_ui(self, msg: str):
        def append():
            self.log_box.configure(state="normal")
            self.log_box.insert("end", msg)
            self.log_box.see("end")
            self.log_box.configure(state="disabled")
        self.after(0, append)

    # ═════════════════════════════════════════════════════════════════════════
    # BROWSE JSON
    # ═════════════════════════════════════════════════════════════════════════
    def _browse_json(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filepath:
            self.json_path_var.set(os.path.basename(filepath))
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.json_edit_box.delete("1.0", "end")
                    self.json_edit_box.insert("1.0", content)
            except Exception as e:
                self.logger.error(f"Failed to read JSON file: {e}")

            student, errors = JsonLoader.load(filepath)

            if errors:
                for err in errors:
                    self.logger.error(err)
                self.current_student = None
                self.student_name_lbl.configure(text="Student Name: [Error loading]")
                self._update_write_btn_state()
                self._update_leds(has_error=True)
            else:
                self.current_student = student
                self.student_name_lbl.configure(text=f"👤  Student Name: {student.student_name}")
                self.logger.info(f"Loaded data for {student.student_name} 🟢")
                self._update_write_btn_state()
                self._update_leds()

    def _apply_pasted_json(self):
        content = self.json_edit_box.get("1.0", "end").strip()
        if not content:
            self.logger.error("JSON text is empty.")
            return

        import tempfile
        try:
            fd, temp_path = tempfile.mkstemp(suffix=".json")
            with os.fdopen(fd, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.json_path_var.set("Pasted JSON")
            student, errors = JsonLoader.load(temp_path)
            os.remove(temp_path)

            if errors:
                for err in errors:
                    self.logger.error(err)
                self.current_student = None
                self.student_name_lbl.configure(text="Student Name: [Error loading]")
                self._update_write_btn_state()
                self._update_leds(has_error=True)
            else:
                self.current_student = student
                self.student_name_lbl.configure(text=f"👤  Student Name: {student.student_name}")
                self.logger.info(f"Loaded pasted JSON data for {student.student_name} 🟢")
                self._update_write_btn_state()
                self._update_leds()
        except Exception as e:
            self.logger.error(f"Failed to apply pasted JSON: {e}")

    # ═════════════════════════════════════════════════════════════════════════
    # LAUNCH CHROME
    # ═════════════════════════════════════════════════════════════════════════
    def _launch_chrome(self):
        import subprocess
        self.logger.info("Launching Chrome with remote debugging...")
        try:
            temp_dir = os.environ.get("TEMP", "C:\\Temp")
            profile_dir = os.path.join(temp_dir, "chrome_debug_profile_new")
            subprocess.Popen(
                f'start chrome --remote-debugging-port=9222 --user-data-dir="{profile_dir}"',
                shell=True,
            )
            self.logger.info("Chrome launched. Please log in and navigate to the Add New Student page.")
        except Exception as e:
            self.logger.error(f"Failed to launch Chrome: {e}")

    # ═════════════════════════════════════════════════════════════════════════
    # CHECK CONNECTION
    # ═════════════════════════════════════════════════════════════════════════
    def _check_connection(self):
        self.logger.info("Checking connection...")
        success, msg = self.browser_ctrl.connect()
        if success:
            self.browser_status_lbl.configure(text="🟢  Connected", text_color="#22c55e")
            page = self.browser_ctrl.get_page()
            if page:
                self.automation = UdiseNewStudentAutomation(page, self.logger)
                self.logger.info(f"Attached to page: {page.title()}")
                found_fields = self.automation.scan_page_fields(self.current_student)
                self._update_comparison_table(found_fields)
        else:
            self.browser_status_lbl.configure(text="🔴  Not Connected", text_color="white")
            self.automation = None
            self._update_comparison_table([])

        self._update_write_btn_state()
        self._update_leds()

    # ═════════════════════════════════════════════════════════════════════════
    # COMPARISON TABLE
    # ═════════════════════════════════════════════════════════════════════════
    def _update_comparison_table(self, found_fields: list):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not self.automation or not found_fields:
            self.tree.configure(height=1)
            return

        for display_name, field_name, value in found_fields:
            status = "Ready" if value else "Empty in JSON"
            self.tree.insert("", "end", values=(display_name, field_name, value, status))

        self.tree.configure(height=max(1, len(found_fields)))

    # ═════════════════════════════════════════════════════════════════════════
    # BUTTON STATE
    # ═════════════════════════════════════════════════════════════════════════
    def _update_write_btn_state(self):
        if self.browser_ctrl.connected:
            self.btn_scan.configure(state="normal")
            self.btn_connect.configure(state="disabled")
            if self.current_student:
                self.btn_write.configure(state="normal")
            else:
                self.btn_write.configure(state="disabled")
        else:
            self.btn_scan.configure(state="disabled")
            self.btn_write.configure(state="disabled")
            self.btn_connect.configure(state="normal")

    # ═════════════════════════════════════════════════════════════════════════
    # SCAN PAGE
    # ═════════════════════════════════════════════════════════════════════════
    def _scan_page(self):
        if not self.automation:
            return
        self.logger.info("Manual scan triggered...")
        self.btn_scan.configure(state="disabled")
        self._update_leds(in_progress=True)

        def task():
            found_fields = self.automation.scan_page_fields(self.current_student)
            self._update_comparison_table(found_fields)
            self.btn_scan.configure(state="normal")
            self._update_leds(in_progress=False)

        self.after(100, task)

    # ═════════════════════════════════════════════════════════════════════════
    # WRITE DATA
    # ═════════════════════════════════════════════════════════════════════════
    def _write_data(self):
        if not self.automation or not self.current_student:
            return

        self.logger.info("Starting write process for visible fields...")
        self.btn_write.configure(state="disabled")
        self._update_leds(in_progress=True)

        def task():
            filled_fields = self.automation.fill_visible_fields(self.current_student)

            for item in self.tree.get_children():
                values = self.tree.item(item, "values")
                field_name = values[1]
                if field_name in filled_fields:
                    self.tree.item(item, values=(values[0], values[1], values[2], "Written ✓"))

            if filled_fields:
                self.logger.info("Write process completed. Please review and save manually.")
                self.btn_write.configure(state="normal")
                self._update_leds(in_progress=False)
            else:
                self.logger.error("No fields were successfully written.")
                self.btn_write.configure(state="normal")
                self._update_leds(in_progress=False, has_error=True)

        self.after(100, task)

    # ═════════════════════════════════════════════════════════════════════════
    # CLOSE
    # ═════════════════════════════════════════════════════════════════════════
    def on_closing(self):
        self.browser_ctrl.disconnect()
        self.destroy()
