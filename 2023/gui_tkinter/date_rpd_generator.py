import tkinter as tk
from pathlib import Path
from typing import Dict

from ruamel.yaml.scalarstring import DoubleQuotedScalarString

from yaml_config import yaml
from ruamel.yaml.scanner import ScannerError
import sys
from PIL import Image, ImageTk
import os


def on_closing():
    sys.exit()


MODELS_PATH = Path(
    "/Users/maximecasara/git/picnic-data-engineering/jobs/dbt-models/dbt_models/models"
)


class WindowFrame(tk.Tk):

    def __init__(self):
        super().__init__()
        self.content: Dict[str, str] = {}
        self.rpd_content: Dict[str, str] = {}
        self.key_altered = False

        # Intercept closing window
        self.wm_protocol("WM_DELETE_WINDOW", on_closing)

        # Set window geometry
        self.geometry("900x900")

        # Load logo
        self.image_logo = Image.open("logo.png").resize((150, 150), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.image_logo)

        # Create Labels and Entries
        self.image_grid = tk.Label(self, image=self.logo)
        prompt_original_model = tk.Label(self, text="Enter source model name:")
        self.entry_original_model = tk.Entry(self)
        self.success = tk.Label(self, text="")
        self.failure = tk.Label(self, text="")
        self.text = tk.Text(self, height=10, width=10)

        # Create listbox
        self.list_box = tk.Listbox(self)

        # Create text scrollbar
        sb = tk.Scrollbar(self, orient=tk.VERTICAL)

        # Create buttons
        button_dump = tk.Button(
            self, text="Dump", command=self._dump_to_yml, relief="solid"
        )
        button_load = tk.Button(self, text="Load", command=self._load, relief="solid")
        button_load_rpd = tk.Button(
            self, text="Load RPDs", command=self.load_rpd, relief="solid"
        )
        button_delete_rpd = tk.Button(
            self, text="Delete RPDs", command=self.remove_item, relief="solid"
        )

        # Create grid
        self.image_grid.grid(
            column=0, row=0, sticky=tk.NSEW, padx=5, pady=5, columnspan=2
        )
        prompt_original_model.grid(column=0, row=2, padx=5, pady=5)
        self.entry_original_model.grid(column=1, row=2, padx=5, pady=5)
        button_load.grid(column=0, row=3, padx=5, pady=5)
        button_load_rpd.grid(column=4, row=3, padx=5, pady=5)
        button_delete_rpd.grid(column=4, row=4, padx=50, pady=5)
        button_dump.grid(column=0, row=6, padx=5, pady=5)
        self.text.grid(column=0, row=1, sticky=tk.NSEW, padx=5, pady=5, columnspan=2)
        sb.grid(row=1, column=2, sticky=tk.NS)
        self.list_box.grid(row=1, column=4, sticky=tk.NS)

        # Attach scrollbar to text widget
        self.text.config(yscrollcommand=sb.set)
        sb.config(command=self.text.yview)

        # For testing
        self.entry_original_model.insert(index=tk.END, string="dm_date")

    def forget_success_failure(self):
        self.failure.grid_forget()
        self.success.grid_forget()

    def _load(self):
        path = Path(self.entry_original_model.get()).with_suffix(".yml")
        if os.path.exists(path):
            with open(path, "r") as file:
                try:
                    content = yaml.load(file)
                    self.content = content
                    self.rpd_content = content
                    self.forget_success_failure()
                    self.success.configure(
                        text=f"Model {path} loaded successfully!", fg="green"
                    )
                    self.success.grid(column=1, row=3, padx=5, pady=5)
                    self.text.insert(index=tk.END, chars=str(self.rpd_content))
                except ScannerError:
                    self.forget_success_failure()
                    self.failure.configure(text="YML wrongly formatted!")
                    self.failure.grid(column=1, row=3, padx=5, pady=5)
        else:
            self.forget_success_failure()
            self.failure.configure(text="File not found!", fg="red")
            self.failure.grid(column=1, row=3, padx=5, pady=5)

    def alter_key(self, rpd):
        original_rpd = self.entry_original_model.get()
        kernel_rpd = rpd.replace(original_rpd + "_", "", 1)
        for name in self.rpd_content["models"][0]["columns"]:
            if "key_" in name["name"]:
                name["name"] = name["name"].replace("key_", f"key_{kernel_rpd}_")
            else:
                name["name"] = f"{kernel_rpd}_" + name["name"]

    def alter_fields(self):
        for column_config in self.rpd_content["models"][0]["columns"]:
            column_config.pop("description", None)
            column_config.pop("constraints", None)
            column_config.pop("tests", None)
            column_config.pop("tags", None)
        self.rpd_content["models"][0].pop("tests", None)

    def alter_config(self, rpd):
        original_name = self.entry_original_model.get()
        rpd_noun = self.entry_original_model.get().split("_")[1].capitalize()
        comment = f"{rpd_noun} {rpd.replace(original_name+'''_''', '', 1)} role playing dimension"
        self.rpd_content["models"][0]["name"] = rpd
        self.rpd_content["models"][0]["description"] = f"{{{{ doc('{rpd}') }}}}"
        self.rpd_content["models"][0]["config"]["materialized"] = "picnic_view"
        self.rpd_content["models"][0]["meta"]["comment"] = DoubleQuotedScalarString(
            comment
        )

    def _dump_to_yml(self) -> None:
        try:
            for rpd in self.list_box.get(0, tk.END):
                name = Path(rpd).with_suffix(".yml")
                Path(
                    f"/Users/maximecasara/git/advent_of_code/2023/gui_tkinter/{rpd}"
                ).mkdir(parents=True, exist_ok=True)

                with open(
                    Path(
                        f"/Users/maximecasara/git/advent_of_code/2023/gui_tkinter/{rpd}"
                    )
                    / name,
                    "w+",
                ) as f:
                    self.alter_key(rpd)
                    self.alter_config(rpd)
                    self.alter_fields()
                    yaml.dump(self.rpd_content, f)
                    self._load()
            self.forget_success_failure()
            self.success.configure(text=f"RPDs dumped successfully!", fg="green")
            self.success.grid(column=1, row=6, padx=5, pady=5)
        except ValueError:
            self.forget_success_failure()
            self.failure.configure(text="Nothing to dump!", fg="red")
            self.failure.grid(column=1, row=6, padx=5, pady=5)

    def load_rpd(self):
        model_name = self.entry_original_model.get()
        self.list_box.delete(0, tk.END)
        for path in os.listdir(MODELS_PATH / "dim"):
            pos = 0
            if model_name in path and model_name != path:
                self.list_box.insert(pos, path)
                pos += 1

    def remove_item(self):
        selected_checkboxs = self.list_box.curselection()
        for selected_checkbox in selected_checkboxs[::-1]:
            self.list_box.delete(selected_checkbox)


if __name__ == "__main__":
    WindowFrame().mainloop()
