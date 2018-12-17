# !/usr/bin/env python3
"""
tile.py: 判断边长为a，b的砖能否在m，n的墙上铺满，并计算有几种铺法，最后可视化输出铺砖的样式

__date__   = "2018.12.15"
__author__ = "Wang Yanze"
__pkuid__  = "1800011721"
__email__  = "1800011721@pku.edu.cn"
"""
import turtle


def is_add(m, a, b):
    """
    判断一个数是否为两个数的整数倍之和, 同时判断含零非法值
    :param m: 判断值
    :param a: 第一个数
    :param b: 第二个数
    :return: 判断真为True，判断假为False
    """
    if a * b == 0:
        return False
    for i in range(m // a + 1):
        if (m - i * a) % b == 0:
            return True
    return False


def is_ok(m, n, a, b):
    """
    初步判断强能否被密铺，即从面积和边长是否为整数倍判断
    :param m, n: 墙的边常
    :param a, b: 砖的边长
    :return: 能铺满为True，不能铺满为False。
    """
    alist = [m, n, a, b]
    for i in alist:
        if i <= 0:
            print('砖或墙的边长应该大于0')
            return False
        elif not isinstance(i, int):
            print('请输入整数边长')
            return False
    if (m * n) % (a * b) == 0 and is_add(m, a, b) and is_add(n, a, b):
        return True
    else:
        print('所用砖块无法完整铺满墙面')
        return False


def brick(x, a, b, m, wall, k):
    """
    通过改变列表数值实现铺砖
    :param x: 第一块砖在墙上的位置的编号
    :param a，b: 砖的边长
    :param m: 墙的长边
    :param wall: 代表墙的列表
    :param k: 铺入的第k块砖
    :return: 铺入砖后墙的新的列表
    """
    for i in range(b):
        for r in range(a):
            wall[x + i * m + r] = k
    return wall


def can_filled(x, a, b, m, n, wall):
    """
    判断能否在x位置放置砖块
    参数与上一个函数的参数意义相同
    :return: 能够在该位置铺入为True，不能为False
    """
    if x % m + a > m:
        return False
    elif x // m + b > n:
        return False
    else:
        num = 0
        for i in range(b):
            for r in range(a):
                num = wall[x + i * m + r] + num
        if num > 0:
            return False
        else:
            return True


def fill_wall(m, n, a, b, my_wall, k, edge):
    """
    不断递归，寻找列表中第一个为0的位置，判断能否铺入，若能，递归进入下一块，当列表中不再有0时返回
    如果砖的边长相等，不进入递归
    :param edge: 代表砖块的边长的列表，用于实现长短边的变换
    :return: None
    """
    global number

    if a == b:
        for pos in range(int((m*n)/(a*b))):
            my_wall = brick(int(((pos % (m / a)) * a + (pos // (m / a)) * (m * a))), a, b, m, my_wall, pos + 1)
        ans = [[n for (n, m) in enumerate(my_wall) if m == x] for x in range(1, int((m * n) / (a * b) + 1))]
        answer.append(ans)
        print(my_wall)
        number = 1
        print("仅有一种铺法：")
        print(ans)
        return

    if 0 not in my_wall:
        ans = [[n for (n, m) in enumerate(my_wall) if m == x] for x in range(1, int((m * n) / (a * b) + 1))]
        answer.append(ans)
        number = number + 1
        print('铺法', number, ":")
        print(ans)
        return
    q = my_wall.index(0)
    for cir in range(2):
        if can_filled(q, edge[cir], edge[-cir - 1], m, n, my_wall):
            my_wall = brick(q, edge[cir], edge[-cir - 1], m, my_wall, k)
            fill_wall(m, n, a, b, my_wall, k + 1, edge)
            my_wall = brick(q, edge[cir], edge[-cir - 1], m, my_wall, 0)
    return


def set_wall(length, width):
    """
    在turtle中布置背景，数字和线框。
    :param ：墙的长和宽
    :return: None
    """
    t.up()
    t.color("blue")
    t.speed(0)
    for w in range(width):
        for l in range(length):
            t.goto(l, w)
            t.write(l + w * length, False, "center")

    for w in range(width + 1):
        t.up()
        t.goto(-0.5, w - 0.5)
        t.down()
        t.fd(length)

    t.left(90)
    for l in range(length + 1):
        t.up()
        t.goto(l - 0.5, -0.5)
        t.down()
        t.fd(width)


def set_brick(f, g, m):
    """
    将以数字f开头，以数字g结尾的砖画出
    :param f: 起始的砖块的位置
    :param g: 末尾的砖块的位置
    :param m: 墙的长
    :return: None
    """
    t.pensize(3)
    t.color("black")
    t.speed(0)
    t.up()
    t.goto(f % m - 0.5, f // m - 0.5)
    t.down()
    t.goto(f % m - 0.5, g // m + 0.5)
    t.goto(g % m + 0.5, g // m + 0.5)
    t.goto(g % m + 0.5, f // m - 0.5)
    t.goto(f % m - 0.5, f // m - 0.5)


def main():
    """
    通过递归实现铺砖的过程，最终可视化输出
    :return:
    """
    global t
    wall_length = int(input("请输入墙的长"))
    wall_width = int(input("请输入墙的宽"))
    brick_length = int(input("请输入砖块的长"))
    brick_width = int(input("请输入砖块的宽"))
    while is_ok(wall_length, wall_width, brick_length, brick_width) is False:
        wall_length = int(input("请输入墙的长"))
        wall_width = int(input("请输入墙的宽"))
        brick_length = int(input("请输入砖块的长"))
        brick_width = int(input("请输入砖块的宽"))

    edge = [brick_length, brick_width]
    wall = [0] * (wall_length * wall_width)
    fill_wall(wall_length, wall_width, brick_length, brick_width, wall, 1, edge)
    unit = dict(enumerate(answer))
    num = int(input("请选择方案(1-%d)" % len(answer)))
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-2, -2, 1.2*wall_length, 1.2*wall_width)
    wn.setup(0.8, 0.8)
    set_wall(wall_length, wall_width)
    for i in unit[num - 1]:
        set_brick(i[0], i[-1], wall_length)
    turtle.done()


if __name__ == "__main__":
    number = 0
    answer = []
    main()











