from flask import render_template, redirect, url_for, request
from twittor.forms import LoginForm
from twittor.models import User, Tweet
from flask_login import login_user, current_user, logout_user, login_required

@login_required
def index():
    # name = {'username': current_user.username}
    posts = [
        {
            'author': {'username': 'root'},
            'body': "hi I'm root!"
        },
        {
            'author': {'username': 'test'},
            'body': "hi I'm test!"
        },
        {
            'author': {'username': 'test1'},
            'body': "hi I'm test1!"
        },        
    ]
    return render_template('index.html',  posts=posts)
def login():
    # form = LoginForm(csrf_enabled = False)
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # msg = 'username = {}, password = {}, remember_me = {}'.format(
        #     form.username.data,
        #     form.password.data,
        #     form.remember_me.data
        # )
        # print(msg)
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('invalid username or password')
            return redirect(url_for('login'))
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # print(next_page)
        if next_page:
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
def logout():
    logout_user()
    return redirect(url_for('login'))