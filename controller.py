#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask plot test

based on:
http://hplgit.github.io/web4sciapps/doc/web/index.html
"""
from model import InputForm
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from compute import compute

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None

    return render_template('view_bootstrap.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
