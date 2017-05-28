#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask plot test

based on:
http://hplgit.github.io/web4sciapps/doc/web/index.html
"""

from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def damped_vibrations(t, A, b, w):
    return A * exp(-b * t) * cos(w * t)


def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution + 1)
    u = damped_vibrations(t, A, b, w)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, u)
    plt.grid(True)
    plt.title('A=%g, b=%g, w=%g' % (A, b, w))

    # Make Matplotlib write to BytesIO file object and grab
    # return the object's string
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    figdata_png = base64.b64encode(figfile.getvalue())

    return figdata_png.decode("utf-8")


def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution + 1)
    u = damped_vibrations(t, A, b, w)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, u)
    plt.grid(True)
    plt.title('A=%g, b=%g, w=%g' % (A, b, w))

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    figdata_png = base64.b64encode(figfile.getvalue()).decode("utf-8")

    figfile = BytesIO()
    plt.savefig(figfile, format='svg')
    figfile.seek(0)
    figdata_svg = '<svg' + figfile.getvalue().decode("utf-8").split('<svg')[1]
    return figdata_png, figdata_svg


if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20)[1])
