from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

components = {}

# PAGE ENDPOINTS

@app.route('/')
def index():
    with open('data/index.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    title="Home",
    project_name="HackerSpace",
    main_heading="</hackerspace>",
    content="Development Club of PES University",
    stylesheets=["<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Poppins&display=swap');</style>", ''],
    body_classes="font-pop",
    heading_classes="font-hsp text-white",
    content_classes="text-white",
    subhead_classes="font-hsp text-white",
    button_classes="border-white border-2 rounded-full text-white font-pop",
    components=components
    )

@app.route('/rr')
def rr():
    with open('data/rr-campus.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    title="RR Campus",
    project_name="HackerSpace",
    main_heading="</hackerspace>",
    content="Development Club of PES University",
    stylesheets=["<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Poppins&display=swap');</style>", ''],
    body_classes="bg-hsp font-pop",
    heading_classes="font-hsp text-white",
    content_classes="text-white",
    subhead_classes="font-hsp text-white",
    button_classes="border-white border-2 rounded-full text-white font-pop",
    components=components
    )

@app.route('/ec')
def ec():
    with open('data/ec-campus.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    title="EC Campus",
    project_name="HackerSpace",
    main_heading="</hackerspace>",
    content="Development Club of PES University",
    stylesheets=["<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Poppins&display=swap');</style>", ''],
    body_classes="bg-hsp font-pop",
    heading_classes="font-hsp text-white",
    content_classes="text-white",
    subhead_classes="font-hsp text-white",
    button_classes="border-white border-2 rounded-full text-white font-pop",
    components=components
    )

@app.route('/discord')
def discord():
    return redirect('https://discord.gg/9m7ad5mDVK')

@app.route('/github')
def github():
    return redirect('https://bit.ly/hackerspace-github')

@app.route('/twitter')
def twitter():
    return redirect('http://bit.ly/hackerspace-twitter-rr')

@app.route('/linkedin')
def linkedin():
    return redirect('https://bit.ly/hackerspace-linkedin')

@app.route('/instagram')
def instagram():
    return redirect('https://www.instagram.com/peshackerspace/')

@app.route('/youtube')
def youtube():
    return redirect('http://bit.ly/hackerspace-youtube')

