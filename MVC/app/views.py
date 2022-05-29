from flask import Flask, render_template, request, redirect, url_for, session
import re
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/projet', methods=['GET', 'POST'])
def projet():
    return render_template('projet.html')

@app.route('/LFI_RFI', methods=['GET', 'POST'])
def LFI_RFI():
    return render_template('LFI_RFI.html')

@app.route('/HeartBleed', methods=['GET', 'POST'])
def HeartBleed():
    return render_template('HeartBleed.html')

@app.route('/Shellshock', methods=['GET', 'POST'])
def Shellshock():
    return render_template('Shellshock.html')

@app.route('/XSS', methods=['GET', 'POST'])
def XSS():
    return render_template('XSS.html')

@app.route('/MITM', methods=['GET', 'POST'])
def MITM():
    return render_template('MITM.html')

@app.route('/LFI_RFI_results', methods=['GET', 'POST'])
def LFI_RFI_results():
    score = 0
    scoreMax=5
    if request.form.get("1-1"):
        score += 1
    if request.form.get("2-2"):
        score += 1
    if request.form.get("3-1"):
        score += 1
    if request.form.get("4-1"):
        score += 1
    if request.form.get("5-2"):
        score += 1
    return render_template('results.html',score=score,scoreMax=scoreMax)


@app.route('/MITM_results', methods=['GET', 'POST'])
def MITM_results():
    score = 0
    scoreMax=3
    if request.form.get("1-2"):
        score += 1
    if request.form.get("2-1"):
        score += 1
    if request.form.get("3-3"):
        score += 1
    return render_template('results.html',score=score,scoreMax=scoreMax)


@app.route('/HeartBleed_results', methods=['GET', 'POST'])
def HeartBleed_results():
    score = 0
    scoreMax=3
    if request.form.get("1-1"):
        score += 1
    if request.form.get("2-1"):
        score += 1
    if request.form.get("3-2"):
        score += 1
    return render_template('results.html',score=score,scoreMax=scoreMax)


@app.route('/Shellshock_results', methods=['GET', 'POST'])
def Shellshock_results():
    score = 0
    scoreMax=4
    if request.form.get("1-2"):
        score += 1
    if request.form.get("2-1"):
        score += 1
    if request.form.get("3-2"):
        score += 1
    if request.form.get("4-3"):
        score += 1
    return render_template('results.html',score=score,scoreMax=scoreMax)


@app.route('/XSS_results', methods=['GET', 'POST'])
def XSS_results():
    score = 0
    scoreMax=4
    if request.form.get("1-2"):
        score += 1
    if request.form.get("2-3"):
        score += 1
    if request.form.get("3-1"):
        score += 1
    if request.form.get("4-2"):
        score += 1
    return render_template('results.html',score=score,scoreMax=scoreMax)
