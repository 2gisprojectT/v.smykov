class Lion:
    def __init__(self, table, def_state="голодный"):
        self.state_table = table
        self.state = def_state

    def action(self, subject):
        reaction = self.state_table[subject, self.state][0]
        self.state = self.state_table[subject, self.state][1]
        return reaction

if __name__ == "__main__":
    state_table = {
        ("охотник", "голодный"): ("Лев убегает. Все еще голодный.", "голодный"),
        ("охотник", "сытый"): ("Лев убегает. Проголодался.", "голодный"),
        ("антилопа", "голодный"): ("Лев съедает антилопу. Лев сытый.", "сытый"),
        ("антилопа", "сытый"): ("Лев ложится вздремнуть. Проголодался.", "голодный"),
        ("дерево", "голодный"): ("Лев ждет добычу под деревом. Все еще голодный.", "голодный"),
        ("дерево", "сытый"): ("Лев вздремул под деревом. Проголодался.", "голодный")
    }

    def_state="голодный"
    Lion = Lion(state_table, def_state)

    print("Лев " + Lion.state + ".")

    while True:
        print("Введите объект (охоник, антилопа, дерево).")
        subject = input().lower()
        if subject == "exit":
            break

        try:
            print(Lion.action(subject) + "\n")
        except:
            print(subject + " неизвеснтый объект \n")
