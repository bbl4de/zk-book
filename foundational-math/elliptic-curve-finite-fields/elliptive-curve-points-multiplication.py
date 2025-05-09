import matplotlib.pyplot as plt

def add_points(x1, y1, x2, y2, a, b, p):
    # point-at-infinity shortcuts
    if (x1, y1) == (None, None):
        return x2, y2
    if (x2, y2) == (None, None):
        return x1, y1

    # same point? do doubling
    if x1 == x2 and y1 == y2:
        num = (3*x1*x1 + a) % p
        den = pow(2*y1, -1, p)
    elif x1 == x2:
        # vertical line => sum is point at infinity
        return None, None
    else:
        num = (y2 - y1) % p
        den = pow((x2 - x1) % p, -1, p)
    lam = (num * den) % p

    xr = (lam*lam - x1 - x2) % p
    yr = (lam*(x1 - xr) - y1) % p
    return xr, yr


def main():
    print("Elliptic curve: y^2 ≡ x^3 + a x + b  (mod p)")
    p = int(input("p = "))
    a = int(input("a = "))
    b = int(input("b = "))

    # Gather all valid curve points
    pts = []
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        for y in range(p):
            if (y*y - rhs) % p == 0:
                pts.append((x, y))
    # Include point at infinity as last option
    pts.append((None, None))

    # List all points with indices
    print("\nAvailable points on the curve:")
    for idx, pt in enumerate(pts):
        label = "∞" if pt == (None, None) else f"({pt[0]}, {pt[1]})"
        print(f"  {idx:3}: {label}")

    def choose_point(name):
        while True:
            try:
                idx = int(input(f"Select index for {name}: "))
                if 0 <= idx < len(pts):
                    return pts[idx]
            except ValueError:
                pass
            print(f"↳ Enter a number between 0 and {len(pts)-1}.")

    P = choose_point("P")
    Q = choose_point("Q")
    R = add_points(*(P + Q), a, b, p)
    print(f"\nP + Q = {R}\n")

    # Plot all curve points
    fig, ax = plt.subplots(figsize=(6,6))
    finite = [(x, y) for x,y in pts if x is not None]
    xs, ys = zip(*finite)
    ax.scatter(xs, ys, c="lightgray", s=30, label="Curve points")

        # Plot P, Q, R
    for pt, col, lab in [(P, "red", "P"), (Q, "blue", "Q"), (R, "green", "R")]:
        if pt[0] is not None:
            ax.scatter([pt[0]], [pt[1]], c=col, s=100)
            ax.text(pt[0]+0.2, pt[1]+0.2, lab, color=col)

    # Draw chord (with wrap) and flip if finite
    if P[0] is not None and Q[0] is not None:
        x1, y1 = P; x2, y2 = Q
        # Compute slope for distinct points; lam=None for vertical
        if x1 != x2:
            lam = ((y2 - y1) * pow((x2 - x1) % p, -1, p)) % p
            # minimal dx via wrap-around
            dx_raw = (x2 - x1) % p
            dx = dx_raw - p if dx_raw > p/2 else dx_raw
            x2p = x1 + dx
            y2p = y1 + lam * dx
            ax.plot([x1, x2p], [y1, y2p], "--", c="black", label="Chord")
        else:
            # vertical chord
            ax.plot([x1, x1], [y1, y2], "--", c="black", label="Chord")

        # Flip to get the final sum
        xr, yr = R
        if xr is not None:
            y_reflect = (-yr) % p
            ax.plot([xr, xr], [y_reflect, yr], ":", c="orange", label="Flip")

    plt.show()()

if __name__ == "__main__":
    main()
