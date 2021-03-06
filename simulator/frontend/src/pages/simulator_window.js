import React, {
    useState, 
    useEffect, 
    createContext,
} from 'react';

import { makeStyles } from '@material-ui/core/styles'

import { Grid } from '@material-ui/core';
import { BASE_URL, STUDENT_ID } from '../constants/config';
import Page from './page_factory';
import SpecialButton from './components/SpecialButton';
import {Link} from 'react-router-dom';


export const GatheredInfoContext = createContext();
export const PageContext = createContext();

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
    const [ pages, setPages ] = useState({});
    const [ isLoading, setIsLoading ] = useState(true);
    const [ finalPageIndex, setFinalPageIndex ] = useState(0);

    const stepChange = (change) => {
        let index = parseInt(activePage) + change;
 
        while(!pages[index]) {
            index = index + change;
            console.log(index);
        }
        
        setActivePage(index);
    }

    const goToPage = (pageNumber) => {
        console.log(pageNumber);
        Object.keys(pages).forEach(key => {
            if(pages[key].pageNumber === pageNumber) {
                setActivePage(key);
            }
        });
    }

    const findNextPage = (pageNumber) => {
        let nextPageKey;

        Object.keys(pages).forEach(key => {
            console.log(pages[key].pageNumber === pageNumber);
            if(pages[key].pageNumber === pageNumber) {
                nextPageKey = key;
            }
        });

        return nextPageKey;
    }

    const finish = () => {
        fetch(BASE_URL + `/student_finished/?scenario_id=${props.match.params.sid}&student_id=${STUDENT_ID}&course_id=1`, {
            method: 'PUT',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              finish: true
            })
          })
          .then(res => res.json())
          .then(data => {
            console.log('Success:', data);
          })
          .catch((err) => {
            console.error("Error: ", err)
          })
    }

    useEffect(() => {
        fetch(BASE_URL + `/get_pages/?scenario_id=${props.match.params.sid}`)
        .then(response => response.json())
        .then( (pagesData) => {

            let newPages = {};
            let allPages = pagesData.results.slice();
            let finalIndex = 0;
            allPages
            .forEach((page, index) => {

                const commonProps = {
                    id: page.id,
                    visited: false, 
                    completed: false, 
                    pageNumber: page.page, 
                    type: page.page_type,
                    nextPageNumber: page.next, 
                    title: page.page_title, 
                    content: page.body,
                    match: props.match,
                    activePage: activePage,
                    changePage: goToPage
                };
            
                newPages[index] = {
                    pageNumber: page.page,
                    component: (<Page {...commonProps} />)
                };

                finalIndex = index
            });

            setPages(newPages);
            setIsLoading(false);
            setFinalPageIndex(finalIndex)
        })
    }, []);
    console.log("activePage: " + activePage + " last index: " + finalPageIndex)
    return (
        <div className={classes.root}>
            <Grid className={classes.simulator} item container direction={"row"} justify="center">
                <Grid container direction={"row"} xs={8} spacing={2}>
                    <Grid item container direction={"column"} md={2}>
                        {
                            activePage > 0 &&
                            <SpecialButton 
                                type={"back"}
                                onClick={() => stepChange(-1)}
                            />
                        }
                    </Grid>
                    <Grid item xs={10} md={8} sm container direction={"column"} spacing={2}>
                        <Grid item xs>
                            <GatheredInfoContext.Provider value={[]}>
                                <PageContext.Provider value={{
                                    state: pages,
                                    setPages: setPages,
                                    update: (nextPage) => {
                                        let nextPageKey = findNextPage(nextPage);
                                        console.log(nextPageKey);
                                        for(let i = activePage + 1; i < nextPageKey; ++i) {
                                            console.log(pages[i]);
                                            delete pages[i];
                                        }
                                        setPages(pages);
                                        goToPage(nextPage);
                                    }
                                }}>
                                    {!isLoading && pages[activePage].component}
                                    {isLoading && <p>We are loading the scenario for you...</p>}
                                </PageContext.Provider>
                            </GatheredInfoContext.Provider>
                        </Grid>
                    </Grid>
                    <Grid item container direction={"column"} md={2}>
                        {
                            
                            (activePage < finalPageIndex) ?
                            (<SpecialButton 
                                type={"next"}
                                onClick={() => {
                                    stepChange(1)
                                }}
                            />)
                            :
                            (<Link to="/">
                                <SpecialButton
                                    type={"finish"}
                                    onClick={() => {
                                        finish()
                                    }}
                                />
                            </Link>)
                        }
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
}

export default SimulationWindow;