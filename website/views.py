from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user
from .models import Flip
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    #variables to display as totals underneath each sessions info
    total_wins = 0
    total_loses = 0
    total_flips = 0
    streak = 0
    average_win = 0

    #loop to pull from "Flip" table and calculate bottom row
    for flip in current_user.flips:
        total_wins += flip.wins
        total_loses += flip.loses
        total_flips += flip.total_games
        if streak < flip.highest_streak:
            streak = flip.highest_streak

    #stopping potential divide by 0 while calc overall average_win percentage
    if total_wins != 0 or total_loses != 0:    
        average_win = round((total_wins / total_flips) * 100, 2)

    return render_template("home.html", user=current_user, total_wins=total_wins, total_loses=total_loses, total_flips=total_flips, streak=streak, average_win=average_win)

@views.route('/flip', methods=['GET', 'POST'])
@login_required
def flip():
    if request.method == 'POST':
        highest_streak = request.form.get('counter_highest')
        wins = request.form.get('wins')
        loses = request.form.get('loses')
        if int(wins) != 0 or int(loses) != 0:
            win_percentage = round(int(wins) / (int(wins) + int(loses)) * 100, 2)

            total_games = int(wins) + int(loses)
            #print(round(win_percentage, 2))

            new_flip = Flip(highest_streak=highest_streak, wins=wins, loses=loses, total_games=total_games, win_percentage=win_percentage, user_id=current_user.id)
            db.session.add(new_flip)
            db.session.commit()

            flash('Session Added', category='success')
            return render_template("flip.html", user=current_user)
        else:
            flash('Can\'t submit, 0 flips', category='error')
            return render_template("flip.html", user=current_user)

    return render_template("flip.html", user=current_user)

#route/method to delete user stats
@views.route('/delete-stats', methods=['POST'])
@login_required
def delete_stats():
    for flip in current_user.flips:
        db.session.delete(flip)
        db.session.commit()
    flash('Stats Reset', category='success')
    return render_template("home.html", user=current_user, total_wins=0, total_loses=0, total_flips=0, streak=0, average_win=0)