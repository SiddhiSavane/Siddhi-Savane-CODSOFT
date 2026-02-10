import tkinter as tk
import random
from tkinter import messagebox

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("450x500")
        self.root.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Rock Paper Scissors", font=("Arial", 22, "bold"))
        title.pack(pady=15)

        info = tk.Label(self.root, text="Choose one option below:", font=("Arial", 12))
        info.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), fg="blue")
        self.result_label.pack(pady=10)

        self.choice_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.choice_label.pack(pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        rock_btn = tk.Button(btn_frame, text="Rock", width=10, height=2,
                             command=lambda: self.play("Rock"))
        rock_btn.grid(row=0, column=0, padx=10)

        paper_btn = tk.Button(btn_frame, text="Paper", width=10, height=2,
                              command=lambda: self.play("Paper"))
        paper_btn.grid(row=0, column=1, padx=10)

        scissor_btn = tk.Button(btn_frame, text="Scissors", width=10, height=2,
                                command=lambda: self.play("Scissors"))
        scissor_btn.grid(row=0, column=2, padx=10)

        # Score
        self.score_label = tk.Label(self.root, text="You: 0   Computer: 0",
                                    font=("Arial", 13, "bold"))
        self.score_label.pack(pady=20)

        reset_btn = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        reset_btn.pack(pady=10)

        exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_btn.pack(pady=5)

    def play(self, user_choice):
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)

        self.choice_label.config(
            text=f"You chose: {user_choice}\nComputer chose: {computer_choice}"
        )

        if user_choice == computer_choice:
            self.result_label.config(text="It's a Tie!", fg="orange")

        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            self.result_label.config(text="You Win!", fg="green")
            self.user_score += 1

        else:
            self.result_label.config(text="You Lose!", fg="red")
            self.computer_score += 1

        self.update_score()

    def update_score(self):
        self.score_label.config(
            text=f"You: {self.user_score}   Computer: {self.computer_score}"
        )

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.choice_label.config(text="")
        self.update_score()
        messagebox.showinfo("Reset", "Game has been reset.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    app.run()
