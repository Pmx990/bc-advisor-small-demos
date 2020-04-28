import React from 'react';
//import {Switch} from 'react-router-dom';
//import Home from './containers/Home';
//import NotFound from './containers/NotFound';
import LoginPage from './components/LoginPage';
import Sidebar from './components/Sidebar';
import {HashRouter, Route, Switch} from 'react-router-dom';
import Home from './components/Home'

import RegisterSuccess from './components/RegisterSuccess';

const Router =() => (
    <HashRouter>
    <Switch>
        <Route exact path="/Login" component={LoginPage}/>
        <Route exact path="/Success" component={RegisterSuccess}/>
        <Route exact path="/" component={Home}/>
        
    </Switch>

    </HashRouter>

);

export default Router;