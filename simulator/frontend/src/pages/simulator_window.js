import React, {
    useState, 
    useEffect, 
    createContext,
} from 'react';

import { makeStyles } from '@material-ui/core/styles'

import { Grid, Typography, Box, Button } from '@material-ui/core';
import { STUDENT_ID, BASE_URL } from '../constants/config';
import Page from './page_factory';
import SpecialButton from './components/SpecialButton';

export const GatheredInfoContext = createContext();

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    simulator: {
        padding: theme.spacing(5),
    }
}));

function SimulationWindow(props) {

    const classes = useStyles();

    const [ activePage, setActivePage ] = useState(0);
    const [ pages, setPages ] = useState([]);
    const [ isLoading, setIsLoading ] = useState(true);

    const changePage = (change) => {
        const pageToGoTo = activePage + change;
        if(pages[pageToGoTo]) {
            console.log("set active page");
            setActivePage(pageToGoTo);
            setPages(pages);
        }
    }

    useEffect(() => {
        fetch(BASE_URL + `/pages/?student_id=${STUDENT_ID}&scenario_id=${props.match.params.sid}`)
        .then(response => response.json())
        .then( (pagesData) => {

            let newPages = {};

            let allPages = pagesData.results.slice();
            
            allPages.filter((page) => {
                console.log(page.scenario.toString() === props.match.params.sid)
                return page.scenario.toString() === props.match.params.sid;
            })
            .forEach((page, index) => {
                console.log(page);

                const commonProps = {
                    visited: false, 
                    completed: false, 
                    pageNumber: page.page, 
                    type: page.page_type,
                    nextPageNumber: page.next_page, 
                    title: page.page_title, 
                    content: page.body,
                    match: props.match,
                    activePage: activePage,
                    changePage: changePage
                };
            
                newPages[index] = (<Page {...commonProps} />);

                console.log(newPages);
            });

            setPages(newPages);
            setIsLoading(false);
        })
    }, [activePage]);

    return (
        <div className={classes.root}>
            <Grid className={classes.simulator} item container direction={"row"} justify="center">
                <Grid container direction={"row"} xs={8} spacing={2}>
                    <Grid item container direction={"column"} md={2}>
                        <SpecialButton 
                            type={"back"}
                            onClick={() => changePage(-1)}
                        />
                    </Grid>
                    <Grid item xs={10} md={8} sm container direction={"column"} spacing={2}>
                        <Grid item xs>
                            <GatheredInfoContext.Provider value={[]}>
                                {pages[activePage]}
                                {isLoading && <p>We are loading the scenario for you...</p>}
                            </GatheredInfoContext.Provider>
                        </Grid>
                    </Grid>
                    <Grid item container direction={"column"} md={2}>
                        <SpecialButton 
                            type={"next"}
                            onClick={() => changePage(1)}
                        />
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
}

export default SimulationWindow;