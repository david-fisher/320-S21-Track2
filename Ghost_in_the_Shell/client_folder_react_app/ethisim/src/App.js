import React from 'react';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import Signup from './pages/signup';
import Login from './pages/login';
import RedirectPage from './pages/redirect';
import Dashboard from './pages/dashboard';
import Editor from './pages/editor';
import Data from './pages/data';
import Homepage from './pages/homepage';
import ToSimulator from './pages/toSimulator';

export default function App() {
    return (
        <Router basename="/se">
            <Route exact path="/">
                <Redirect to="/home" />
            </Route>
            <Route path="/home" component={Homepage} />
            <Route path="/login" component={Login} />
            <Route path="/redirect" component={RedirectPage} />
            <Route path="/signup" component={Signup} />
            <Route path="/dashboard" component={Dashboard} />
            <Route
                path="/editor/:id"
                render={(props) => <Editor {...props} />}
            />
            <Route path="/data/:id" render={(props) => <Data {...props} />} />
            <Route
                path="/toSimulator"
                component={() => {
                    window.location.href =
                        'https://ethisim2.cs.umass.edu/simulator/';
                    return null;
                }}
            />
        </Router>
    );
}

/*
            <Route path="/login" component={Login}>
                <Redirect to="https://ethisim2.cs.umass.edu/Shibboleth.sso/Login?target=http://localhost:3000/login" />
            </Route>
*/
//<Route path="/login" component={Login} />
/*<Route path="/login" component={() => { 
                window.location.href = 'https://ethisim2.cs.umass.edu/Shibboleth.sso/Login?target=https://ethisim2.cs.umass.edu/se/dashboard'; 
                return null;
            }}/>*/
