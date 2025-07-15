from class_de_sudokus import Case, TableauSudoku
import tkinter as tk

class SudokuGrid:
    def __init__(self, TableauSudoku):
        self.master = TableauSudoku
        TableauSudoku.title("9x9 Sudokus Grid")

        self.entry_vars = []  # To store StringVar objects for each entry
        self.entries = []  # To store Entry widgets

        for r in range(9):
            row_vars = []
            row_entries = []
            for c in range(9):
                # Create a StringVar for each entry
                var = tk.StringVar(TableauSudoku)
                row_vars.append(var)

                # Create an Entry widget and link it to the StringVar
                entry = tk.Entry(TableauSudoku, textvariable=var, width=6, justify='center')
                entry.grid(row=r + 1, column=c, padx=6, pady=6)
                row_entries.append(entry)

                # Add padding to create visual separation for 3x3 blocks

                if (c + 1) % 3 == 0 and c != 8:
                    entry.grid(padx=(1, 5))

            self.entry_vars.append(row_vars)
            self.entries.append(row_entries)

            if (r + 1) % 3 == 0 and r != 8:
                # Add padding to create visual separation for 3x3 blocks
                TableauSudoku.grid_rowconfigure(r, pad=5)

        ## Ajouter un bouton pour Résoudre le sudokus
        tk.Button(
            TableauSudoku, text="Résoudre", command=self.update_grid_values
        ).grid(row=0, column=9, padx=6, pady=5)


        # Ajouter un bouton pour importer un sudokus
        tk.Button(
            TableauSudoku, text="importer un exemple", command=self.import_sudoku
        ).grid(row=0, column=10, padx=6, pady=5)

        tk.Button(
            TableauSudoku, text="Solution", command=self.verify_sudoku
        ).grid(row=0, column=11, padx=6, pady=5)
    def get_grid_values(self):
        """Retrieves the current values from all entry widgets."""
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
        filepath = "exemple3.txt"

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

                if char in "123456789":
                    self.entry_vars[i][j].set(char)
                else:
                    self.entry_vars[i][j].set("")


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

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    grid_app = SudokuGrid(root)

    # You can set initial values if needed
    # grid_app.entry_vars[0][0].set("5")

    # Example of retrieving values after user input
    # def print_values():
    #     print(grid_app.get_grid_values())
    # tk.Button(root, text="Get Values", command=print_values).grid(row=9, columnspan=9)

    root.mainloop()