import tkinter as tk
from class_de_sudokus import Case, TableauSudoku
import random
class SudokuGrid:
    def __init__(self, root):
        self.master = root

        root.title("9x9 Sudokus Grid")
        root.geometry('600x600')
        root.resizable(False, False)
        self.entry_vars = []
        self.entries = []

        # --- Top frame for buttons ---
        commandes = tk.Frame(root)
        commandes.pack(pady=10)

        tk.Button(commandes, text="Résoudre", command=self.update_grid_values).pack(side=tk.LEFT, padx=10)
        tk.Button(commandes, text="Importer un exemple", command=self.import_sudoku).pack(side=tk.LEFT, padx=10)
        tk.Button(commandes, text="Solution", command=self.verify_sudoku).pack(side=tk.LEFT, padx=10)

        # --- Grid frame ---
        grid_frame = tk.Frame(root, bg="black")  # black background to simulate bold lines
        grid_frame.pack(pady=10)

        for r in range(9):
            row_vars = []
            row_entries = []
            for c in range(9):
                var = tk.StringVar()
                entry = tk.Entry(width=3, font=("Arial", 18), justify="center", textvariable=var)

                # Determine thickness of right and bottom borders
                right_thickness = 3 if (c + 1) % 3 == 0 and c != 8 else 1
                bottom_thickness = 3 if (r + 1) % 3 == 0 and r != 8 else 1

                # Frame with only bottom and right thicker if on 3x3 boundary
                cell_frame = tk.Frame(
                    grid_frame,
                    highlightbackground="black",
                    highlightcolor="black",
                    highlightthickness=0,
                    bd=0
                )
                cell_frame.grid(row=r, column=c, sticky="nsew")

                # Nested frame to simulate borders
                border_frame = tk.Frame(
                    cell_frame,
                    bd=0,
                    highlightbackground="black",
                    highlightcolor="black",
                    highlightthickness=1,
                )
                border_frame.pack(
                    fill="both",
                    expand=True,
                    padx=(1, right_thickness),
                    pady=(1, bottom_thickness)
                )

                entry.grid(in_=border_frame, row=0, column=0, padx=1, pady=1)

                row_vars.append(var)
                row_entries.append(entry)
            self.entry_vars.append(row_vars)
            self.entries.append(row_entries)

        # Set equal size for each cell
        # for i in range(9):
        #     grid_frame.grid_columnconfigure(i, weight=1)
        #     grid_frame.grid_rowconfigure(i, weight=1)

    def get_grid_values(self):
        grid_values = []
        for r in range(9):
            row_values = []
            for c in range(9):
                row_values.append(self.entry_vars[r][c].get())
            grid_values.append(row_values)
        return grid_values

    def update_grid_values(self):
        mon_tableau = TableauSudoku()
        for i in range(9):
            for j in range(9):
                mon_tableau.ajouter_une_case(i, j, self.entry_vars[i][j].get())

        mon_tableau.solve_sudoku()

        for i in range(9):
            for j in range(9):
                self.entry_vars[i][j].set(mon_tableau.cases[mon_tableau.name_case(i, j)].number)

    def import_sudoku(self):
        filepath_list = ["exemple1.txt", "exemple2.txt", "exemple3.txt"]
        filepath = random.choice(filepath_list)

        with open(filepath, 'r') as file:
            lines = file.readlines()

        if len(lines) != 9:
            print("Invalid file: must have 9 lines.")
            return

        for i in range(9):
            line = lines[i].strip().replace(" ", "")
            if len(line) != 9:
                print(f"Line {i + 1} is not 9 characters long.")
                return

            for j in range(9):
                char = line[j]
                self.entry_vars[i][j].set(char if char in "123456789" else "")

        print("Puzzle loaded successfully.")

    def verify_sudoku(self):
        mon_tableau = TableauSudoku()
        for i in range(9):
            for j in range(9):
                mon_tableau.ajouter_une_case(i, j, self.entry_vars[i][j].get())

        if mon_tableau.is_solved():
            print("Puzzle solved successfully.")
        else:
            print("Puzzle not solved.")


# --- Main app entry ---
if __name__ == "__main__":
    root = tk.Tk()
    grid_app = SudokuGrid(root)
    root.mainloop()
