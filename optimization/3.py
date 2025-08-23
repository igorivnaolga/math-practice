import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams.update({"font.size": 12})


x = np.linspace(0, 4, 100)


f1 = 2 * x
f2 = (1 / 3) * x
f3 = 1 - x
f4 = 5 / 2 - (1 / 2) * x
ff = 0.5 * x


fig, ax = plt.subplots(figsize=(9, 8))
# вказуємо в аргументі label текст легенди
plt.plot(x, f1, ":b", label="x2<2x1")
plt.plot(x, f2, "k", label="x2>1/3x1")
plt.plot(x, f3, "--b", label="x2>1-x1")
plt.plot(x, f4, "--g", label="x2<5/2-1/2x1")


# додаємо стрілки
plt.arrow(1, 0, 0.2, 0.2, length_includes_head=True, head_width=0.05, head_length=0.1)
plt.arrow(
    0.8, 2.1, -0.1, -0.2, length_includes_head=True, head_width=0.05, head_length=0.1
)
plt.arrow(
    1.1, 2.2, 0.2, -0.1, length_includes_head=True, head_width=0.05, head_length=0.1
)
plt.arrow(
    3.3, 1.1, -0.1, 0.2, length_includes_head=True, head_width=0.05, head_length=0.1
)


# заповнюємо ОДЗ та додаємо підписи до точок
v_x = [1 / 3, 1, 3, 3 / 4]
v_y = [2 / 3, 2, 1, 1 / 4]
v_names = ["A", "B", "C", "D"]
plt.fill(v_x, v_y, "red", alpha=0.3)


plt.grid(True)
for x, y, label in zip(v_x, v_y, v_names):
    plt.scatter(x, y, c="red")
    plt.text(x - 0.03, y + 0.06, label)


plt.xlabel(r"$x1$", fontsize=16)
plt.ylabel(r"$x2$", fontsize=16)


plt.xlim([0, 3.5])
plt.ylim([0, 3])


# виводимо легенду
plt.legend(fontsize=14)


plt.gca().set_aspect("equal")
plt.tight_layout()
plt.show()
