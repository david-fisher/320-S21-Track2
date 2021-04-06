import React, { useState, useEffect, createContext } from 'react';
import { Grid, Typography, Box, Button } from '@material-ui/core';
import { STUDENT_ID, BASE_URL } from '../constants/config';
import Page from './page_factory';

export const GatheredInfoContext = createContext();

function SimulationWindow(props) {
    const [ activePage, setActivePage ] = useState(0);
    const [ pages, setPages ] = useState([]);
    const [ isLoading, setIsLoading ] = useState(true);

    useEffect(() => {
        fetch(BASE_URL + `/pages/?student_id=${STUDENT_ID}&scenario_id=${props.match.params.sid}`)
        .then(response => response.json())
        .then( (pagesData) => {

            let newPages = {};
            
            pagesData.results.forEach((page) => {

                const commonProps = {
                    visited: false, 
                    completed: false, 
                    pageNumber: page.page, 
                    type: page.page_type,
                    nextPageNumber: page.next_page, 
                    title: page.page_title, 
                    content: page.body,
                    match: props.match
                };
            
                newPages[page.page] = (<Page {...commonProps} />);
            });

            setPages(newPages);
            setIsLoading(false);
        })
    }, [activePage]);

    const nextPage = () => {
        if(!pages[activePage + 1]) {
            return;
        }
        setActivePage(activePage + 1);
        setPages(pages);
    }

    return (
        <div className="SimWindow">
            <Grid container spacing={2}>
                <Grid item lg={3} md={2} sm={2}>
                </Grid>
                <Grid item lg={6} md={8} sm={8}>
                    <Box mb={6}>
                        <GatheredInfoContext.Provider value={[]}>
                            {isLoading && <p>We are loading the scenario for you...</p>}
                            {pages[activePage]}
                        </GatheredInfoContext.Provider>
                    </Box>
                </Grid>
                <Grid container item lg={3} md={2} sm={2}>
                    <Button onClick={nextPage}>
                        Click this for next page
                    </Button>
                </Grid>
            </Grid>
        </div>
    );
}

export default SimulationWindow;