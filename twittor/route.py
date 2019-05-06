from flask import render_template, redirect, url_for, request, abort
from twittor.forms import LoginForm, RegisterForm,EditProfileForm
from twittor.models import User, Tweet
from flask_login import login_user, current_user, logout_user, login_required
from twittor import db
@login_required
def index():
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
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        u = User.query.filter_by(username=form.username.data).first()
        login_user(u, remember=True)
        return redirect(url_for('index'))
    return render_template('register.html', title='Registration', form=form)
@login_required
def user(username):
    u = User.query.filter_by(username=username).first()
    # if not u and u!=current_user:
    if u is None:
        abort(404)
    # posts = [
    #     {
    #         'author': {'username': u.username},
    #         'body': "hi I'm {}!".format(u.username)
    #     },
    #     {
    #         'author': {'username': u.username},
    #         'body': "hi I'm {}!".format(u.username)
    #     },      
    # ]
    # posts = Tweet.query.filter_by(author=u)
    posts = u.tweets
    if request.method =='POST':
        if request.form['request_button'] == 'Follow':
            current_user.follow(u)
            db.session.commit()
        else:
            current_user.unfollow(u)
            db.session.commit()
    return render_template('user.html', title='Profile', user=u,posts=posts)

@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == 'GET':
        form.about_me.data = current_user.about_me
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('profile', username=current_user.username))
    return render_template('edit_profile.html', form=form)