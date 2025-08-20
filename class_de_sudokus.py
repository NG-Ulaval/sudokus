

class Case:
    def __init__(self, number = ""):
        self.number = number
        self.possibility = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def number_known(self):
        if self.number in "123456789":
            self.possibility = [self.number]


class TableauSudoku:
    def __init__(self):
        self.cases = {}

    def __repr__(self):
        return str(self.cases)

    def name_case(self, axe_x, axe_y):
        # return is name
        return f"{axe_x},{axe_y}"

    def ajouter_une_case(self, axe_x, axe_y, valeur):
        self.cases[self.name_case(axe_x, axe_y)] = Case(number = valeur)
        if valeur != "":
            self.cases[self.name_case(axe_x, axe_y)].possibility = [valeur]

    def changer_valeur_case(self, axe_x, axe_y, valeur):
        self.cases[self.name_case(axe_x,axe_y)].number = valeur
        self.cases[self.name_case(axe_x,axe_y)].number_known()

    def check_x_value(self, axe_x, axe_y):
        # Regarde les valeurs possibles de la cases sur l'axe des x
        # Créer une liste des numéro des autres cases
        liste = list(range(9))
        liste.remove(axe_x)

        # Pour chaque possibilité
        for number in self.cases[self.name_case(axe_x, axe_y)].possibility:
            conteur = 0

            # Pour toutes les cases autres
            for i in liste:
                # Si le nombre n'est pas possible pour la case
                if number not in self.cases[self.name_case(axe_x,i)].possibility:
                    conteur += 1
            # Si la possibité était seulement possible dans cette case
            if conteur == 8:
                try:
                    if self.cases[self.name_case(axe_x, axe_y)].number != "" and self.cases[self.name_case(axe_x, axe_y)].number != number:
                        raise Exception(f"nombre qui devrait être la valeur: {number}\n Nombre qui est la valeur: {self.cases[self.name_case(axe_x, axe_y)].number}")
                except Exception:
                    "Deux valeurs possibles ... Il y a une erreur"

                self.changer_valeur_case(axe_x, axe_y, number)

    def check_y_value(self, axe_x, axe_y):
        # Regarde les valeurs possibles de la cases sur l'axe des y
        # Créer une liste des numéro des autres cases
        liste = list(range(9))
        liste.remove(axe_y)

        # Pour chaque possibilité
        for number in self.cases[self.name_case(axe_x, axe_y)].possibility:
            conteur = 0

            # Pour toutes les cases autres
            for i in liste:
                # Si le nombre n'est pas possible pour la case
                if number not in self.cases[self.name_case(i, axe_y)].possibility:
                    conteur += 1
            # Si la possibité était seulement possible dans cette case
            if conteur == 8:
                try:
                    if self.cases[self.name_case(axe_x, axe_y)].number != "" and self.cases[self.name_case(axe_x, axe_y)].number != number:
                        raise Exception(f"nombre qui devrait être la valeur: {number}\n Nombre qui est la valeur: {self.cases[self.name_case(axe_x, axe_y)].number}")
                except Exception:
                    "Deux valeurs possibles ... Il y a une erreur"

                self.changer_valeur_case(axe_x, axe_y, number)

    def check_box_value(self, axe_x, axe_y):
        square_x = axe_x // 3 * 3
        square_y = axe_y // 3 * 3
        for number in self.cases[self.name_case(axe_x, axe_y)].possibility:
            conteur = 0
            for i in range(square_x, square_x + 3):
                for j in range(square_y, square_y + 3):
                    if number not in self.cases[self.name_case(i, j)].possibility:
                        conteur += 1
            if conteur == 8:
                try:
                    if self.cases[self.name_case(axe_x, axe_y)].number != "" and self.cases[self.name_case(axe_x, axe_y)].number != number:
                        raise Exception(f"nombre qui devrait être la valeur: {number}\n Nombre qui est la valeur: {self.cases[self.name_case(axe_x, axe_y)].number}")
                except Exception:
                    "Deux valeurs possibles ... Il y a une erreur"
                self.changer_valeur_case(axe_x, axe_y, number)
                return


    def check_value(self, axe_x, axe_y):
        if len(self.cases[self.name_case(axe_x, axe_y)].possibility) != 1:
            self.check_x_value(axe_x, axe_y)
            self.check_y_value(axe_x, axe_y)
            self.check_box_value(axe_x, axe_y)
        else:
            self.cases[self.name_case(axe_x, axe_y)].number = self.cases[self.name_case(axe_x, axe_y)].possibility[0]

    def check_every_value(self):
        for i in range(9):
            for j in range(9):
                self.check_value(i, j)

    def check_possibility(self, axe_x, axe_y):
        # Check x Value
        for i in range(9):
            if self.cases[self.name_case(axe_x, i)].number in self.cases[self.name_case(axe_x, axe_y)].possibility and i != axe_y:
                self.cases[self.name_case(axe_x, axe_y)].possibility.remove(self.cases[self.name_case(axe_x, i)].number)

        # Check y value
        for j in range(9):
            if self.cases[self.name_case(j, axe_y)].number in self.cases[self.name_case(axe_x, axe_y)].possibility and j != axe_x:
                self.cases[self.name_case(axe_x, axe_y)].possibility.remove(self.cases[self.name_case(j, axe_y)].number)

        # check square value
        square_x_ = axe_x //3 * 3
        square_y_ = axe_y //3 * 3
        for i in range(square_x_, square_x_ + 3):
            for j in range(square_y_, square_y_ + 3):
                if self.cases[self.name_case(i, j)].number in self.cases[self.name_case(axe_x, axe_y)].possibility and (i, j) != (axe_x, axe_y):
                    self.cases[self.name_case(axe_x, axe_y)].possibility.remove(self.cases[self.name_case(i, j)].number)

    def check_every_possibility(self):
        for i in range(9):
            for j in range(9):
                if self.cases[self.name_case(i, j)].number == "":
                    self.check_possibility(axe_x=i, axe_y=j)

    def is_solved(self, extra = True):
        if extra:
            nb_bonne_reponse = 0
            for i in range(9):
                for j in range(9):
                    name = self.name_case(i, j)
                    self.cases[name].possibility = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    self.check_possibility(i, j)

                    if [str(self.cases[name].number)] == self.cases[name].possibility:
                        nb_bonne_reponse += 1
            if nb_bonne_reponse == 81:
                return True
            return False

        known_values = 0
        for i in self.cases.keys():
            if str(self.cases[i].number) in "0123456789" and self.cases[i].number != "":
                known_values += float(self.cases[i].number)

        return known_values == 495



    def normal_solve(self):
        start_check = 1
        known_values = 0

        # implimenting known_values
        for i in self.cases.keys():
            if self.cases[i].number in "0123456789" and self.cases[i].number != "":
                known_values += float(self.cases[i].number)

        while start_check != known_values:
            self.check_every_possibility()
            self.check_every_value()

            # making sure progress is made
            start_check = known_values
            known_values = 0
            for i in self.cases.keys():
                if self.cases[i].number in "0123456789" and self.cases[i].number != "":
                    known_values += float(self.cases[i].number)

    # Force solve method
    def is_valid(self, num, axe_x, axe_y):
        # Check x Value
        for i in range(9):
            if self.cases[self.name_case(axe_x, i)].number == num and i  != axe_y:
                return False

        # Check y value
        for i in range(9):
            if self.cases[self.name_case(i, axe_y)].number == num and i != axe_x:
                return False

        # check square value
        square_x_ = axe_x // 3 * 3
        square_y_ = axe_y // 3 * 3

        for i in range(square_x_, square_x_ + 3):
            for j in range(square_y_, square_y_ + 3):
                if self.cases[self.name_case(i, j)].number == num and (i, j) != (axe_x, axe_y):
                    return False
        return True

    # For solve method
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cases[self.name_case(i, j)].number == "":
                    return i, j
        return None

    def force_solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            axe_x, axe_y = find
        for num in range(1, 10):
            num = str(num)
            if self.is_valid(num, axe_x, axe_y):
                self.cases[self.name_case(axe_x, axe_y)].number = num
                # Next one to find
                if self.force_solve():
                    return True

                self.cases[self.name_case(axe_x, axe_y)].number = ""

        return False

    def solve_sudoku(self):
        self.normal_solve()

        if self.is_solved():
            return

        print("solving sudoku with force")
        self.force_solve()



