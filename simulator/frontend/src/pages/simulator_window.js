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
            
            pagesData.results.forEach((page) => {

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
            
                newPages[page.page] = (<Page {...commonProps} />);
            });

            setPages(newPages);
            setIsLoading(false);
        })
    }, [activePage]);

    const nextPage = () => {
        if(!pages[activePage + 1]) {
            return;
        } else if(activePage < 1)
        setActivePage(activePage + 1);
        setPages(pages);
    }

    return (
        <div className={classes.root}>
            <Grid className={classes.simulator} item container direction={"row"} justify="center">
                <Grid container direction={"row"} xs={8} spacing={2}>
                    <Grid item container direction={"column"} md={2}>
                        {activePage !== 0 && 
                            <SpecialButton 
                                type={"back"}
                                onClick={() => changePage(-1)}
                            />
                        }
                    </Grid>
                    <Grid item xs={10} md={8} sm container direction={"column"} spacing={2}>
                        <Grid item xs>
                            {pages[activePage]}
                            {isLoading && <p>We are loading the scenario for you...</p>}
                            {
                                activePage === 0 && 
                                <Button onClick={() => changePage(1)}>
                                    Welcome to the Simulator...Press this button to continue.
                                </Button>
                            }
                        </Grid>
                    </Grid>
                    <Grid item container direction={"column"} md={2}>
                        {activePage !== 0 && <SpecialButton 
                            type={"next"}
                            onClick={() => changePage(1)}
                        />}
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
}

export default SimulationWindow;