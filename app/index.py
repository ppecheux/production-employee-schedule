# import for requirements

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app, server
from flask_login import logout_user, current_user


from views import login, error, profile, user_admin, navbar
from views.navbar import navBar, dashboard_pages, mix_page
from datetime import datetime as dt
from math import exp, log
import sys


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        navBar,
        html.Div(id='pageContent')
    ])
], id='table-wrapper')



@app.callback(Output('pageContent', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    for pathname_dashboard, file in dashboard_pages.items():
        if pathname == pathname_dashboard:
            if file:
                if current_user.is_authenticated:
                    return file.layout
                else:
                    return login.layout
    if pathname == '/':
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login.layout

    if pathname == '/mix_page':
        if current_user.is_authenticated:
            return mix_page.layout
        else:
            return mix_page.layout

    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
        return login.layout

    if pathname == '/profile':
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login.layout

    if pathname == '/admin':
        if current_user.is_authenticated:
            if current_user.admin:
                return user_admin.layout
            else:
                return error.layout
        else:
            return login.layout

    else:
        return error.layout


if __name__ == '__main__':
    host = '127.0.0.1'
    if len(sys.argv) > 1:
        host = sys.argv[1]
    app.run_server(host=host, debug=True)
