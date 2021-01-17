import simple_draw as sd


def bubble(point, step):
    radius = 50
    for _ in range(7):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


point = sd.get_point(300,300)
bubble(point=point, step=10)