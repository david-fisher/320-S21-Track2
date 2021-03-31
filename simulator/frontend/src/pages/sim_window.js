import React, { Component } from 'react';
import { Grid, Box, Typography, ListItemAvatar, Button } from '@material-ui/core';
import Axios from 'axios';
import { BASE_URL, STUDENT_ID } from '../constants/config';
import { Link, BrowserRouter, Route } from 'react-router-dom';
import Page from './page_factory';
import InfoGatheredList from './components/gatheredList';
import Stepper from './components/stepper';

class SimulationWindow extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activePage: 0,
            pages: [],
            loading: true,
            error: false
        };
    }

    /**
     * url="http://localhost:8000/api/pages/?student_id=1&scenario_id=1"
     */
    componentDidMount() {
        this.fetchPages(`${BASE_URL}/pages/?student_id=${STUDENT_ID}&scenario_id=${this.props.match.params.sid}`, {
            "method": "GET"
        });
    }

    /**
     * Example Data Returned:
     * { 
     *      "count": 1, // we dont need to care about this
     *      "next": null, // we dont need to care about this
     *      "previous": null, // we dont need to care about this
     *      "results": [
                {
                    "page": 1,
                    "page_type": "I",
                    "page_title": "Introduction",
                    "body": "You are a software engineer..."
                    "next_page": 2,
                    "scenario": 1
                }
            ]
     * }
     */
    fetchPages = (url) => {
        fetch(url)
        .then(results => results.json())
        .then((pagesData) => {
            let pages = pagesData.results.slice().map((page) => {
                const commonProps = {
                    visited: false, 
                    completed: false, 
                    pageNumber: page.page, 
                    type: page.page_type,
                    nextPageNumber: page.next_page, 
                    title: page.page_title, 
                    content: page.body,
                    match: this.props.match
                }
                return (<Page {...commonProps} />);
            });

            console.log(pages);

            this.setState({
                ...this.state,
                pages
            });
        })
        .catch((error) => console.log(error));
    }

    render() {
        let { pages, activePage } = this.state;
        console.log(pages);
        console.log(activePage)
        return (
            <div className="SimWindow">
                <BrowserRouter>
                <Grid container spacing={2}>
                    <Grid item lg={3} md={2} sm={2}>
                        {(this.state.activePage !== 0) 
                        ? <Stepper activePage={activePage} pages={pages} setPages={this.setState} setActivePage={this.setState} key={activePage} />    
                        : null}
                    </Grid>
                    <Grid item lg={6} md={8} sm={8}>
                        <Box mb={6}>
                            {(this.state.activePage === 0) ?
                                // Button displayed to bring you to intro page when clicked...gives time for pages to load in
                                (<nav>
                                    <Link 
                                        to={`${this.props.match.url}/${1}`}
                                        onClick={() => {
                                            activePage++;

                                            this.setState({
                                                ...this.state,
                                                activePage
                                            });
                                        }}
                                    >
                                        <Button>
                                            Click to Start!
                                        </Button>
                                    </Link>
                                </nav>) : null}
                            {/** All the routes are dynamically loaded so that pages will appear when url is changed.
                             * i.e. http://localhost:3000/simulation/:sid/:page -> http://localhost:3000/simulation/:1/:1 would bring you to the intro page
                             */}
                            {pages.map((page, index) => {
                                return (
                                    <Route exact 
                                        key={index} 
                                        path={`${this.props.match.url}/${index + 1}`} 
                                    >
                                        {page}
                                    </Route>
                                );
                            })}
                        </Box>
                    </Grid>
                    <Grid container item lg={3} md={2} sm={2}>
                    </Grid>
                </Grid>
                </BrowserRouter>
            </div>
        )
    }

}

export default SimulationWindow;