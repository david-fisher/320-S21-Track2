import React, { useState, useEffect } from 'react';
import { makeStyles, useTheme, withStyles } from '@material-ui/core/styles';
import { Drawer, Box, Button, Typography } from '@material-ui/core';
import clsx from 'clsx';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import Logistics from '../components/EditorComponents/LogisticsPageComponents/Logistics';
import Generic from '../components/EditorComponents/GenericPageComponents/Generic';
import ConfigureIssues from '../components/EditorComponents/ConfigureIssuesComponents/ConfigureIssues';
import ConversationEditor from '../components/EditorComponents/ConversationEditorComponents/ConversationEditor';
import Reflection from '../components/EditorComponents/ReflectionPageComponents/Reflection';
import Action from '../components/EditorComponents/ActionPageComponents/Action';
import Introduction from '../components/EditorComponents/GenericPageComponents/Introduction';
import ICMatrix from '../components/EditorComponents/IssueCoverageMatrixComponents/IssueCoverageMatrixPage';
import Consequences from '../components/EditorComponents/ConsequencePageComponents/Consequences';
import FlowDiagram from '../components/EditorComponents/FlowDiagramComponents/FlowDiagram';
import AddNewSimulationScenarioPageDialog from '../components//EditorComponents/AddNewSimulationScenarioPageDialog';
import NavSideBarList from '../components/ConfigurationSideBarComponents/NavSideBarList';
import ToDoListDialog from '../components/EditorComponents/ToDoListDialog';
import AddIcon from '@material-ui/icons/Add';
import { Link } from 'react-router-dom';
import LoadingSpinner from '../components/LoadingSpinner';
import SuccessBanner from '../components/Banners/SuccessBanner';
import ErrorBanner from '../components/Banners/ErrorBanner';
import PropTypes from 'prop-types';
import { useLocation } from 'react-router-dom';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import ViewListIcon from '@material-ui/icons/ViewList';

import universalPost from '../universalHTTPRequests/post.js';
import universalFetch from '../universalHTTPRequests/get.js';
import universalDelete from '../universalHTTPRequests/delete.js';
//  setResponse, endpoint, onError, onSuccess, requestBody

const drawerWidth = 250;

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
    },
    appBar: {
        transition: theme.transitions.create(['margin', 'width'], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
    },
    appBarShift: {
        width: `calc(100% - ${drawerWidth}px)`,
        marginLeft: drawerWidth,
        transition: theme.transitions.create(['margin', 'width'], {
            easing: theme.transitions.easing.easeOut,
            duration: theme.transitions.duration.enteringScreen,
        }),
    },
    exitButton: {
        margin: theme.spacing(2),
        borderStyle: 'solid',
        borderColor: 'white',
        border: 2,
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    hide: {
        display: 'none',
    },
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
    },
    drawerPaper: {
        width: drawerWidth,
    },
    content: {
        flexGrow: 1,
        padding: theme.spacing(3),
    },
    container: {
        marginTop: theme.spacing(1),
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
    },
    bannerContainer: {
        marginTop: theme.spacing(1),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    title: {
        textAlign: 'center',
    },
    copyright: {
        margin: theme.spacing(2),
        opacity: 0.5,
    },
    addPageButton: {
        margin: theme.spacing(2),
        textTransform: 'unset',
        border: 'solid 3px',
        borderColor: theme.palette.primary.light,
    },
    drawerHeader: {
        display: 'flex',
        alignItems: 'center',
        padding: theme.spacing(0, 1),
        // necessary for content to be below app bar
        ...theme.mixins.toolbar,
        justifyContent: 'flex-end',
    },
    content1: {
        flexGrow: 1,
        padding: theme.spacing(3),
        transition: theme.transitions.create('margin', {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        marginLeft: -drawerWidth,
    },
    contentShift: {
        transition: theme.transitions.create('margin', {
            easing: theme.transitions.easing.easeOut,
            duration: theme.transitions.duration.enteringScreen,
        }),
        marginLeft: 0,
    },
    issue: {
        marginTop: theme.spacing(10),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    errorContainer: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    iconError: {
        paddingRight: theme.spacing(2),
        fontSize: '75px',
    },
    iconRefreshLarge: {
        fontSize: '75px',
    },
    iconRefreshSmall: {
        fontSize: '30px',
    },
}));

Editor.propTypes = {
    location: PropTypes.any,
};

export default function Editor(props) {
    const [showComponent, setShowComponent] = useState(true);
    const [openPopup, setOpenPopup] = useState(false);
    const [openToDo, setOpenToDo] = useState(false);

    const location = useLocation();
    console.log(location);
    const scenarioIDFromURL = location.pathname.split('/').pop();
    console.log(scenarioIDFromURL);

    const scenario_ID = props.location.data
        ? props.location.data.SCENARIO_ID
        : scenarioIDFromURL;

    console.log(scenario_ID);

    //TODO when version control is implemented
    const tempVersionID = 1;

    const [getValues, setGetValues] = useState({
        data: null,
        loading: true,
        error: null,
    });

    // eslint-disable-next-line
    const [deleteValues, setDeleteValues] = useState({
        data: null,
        loading: true,
        error: null,
    });

    // eslint-disable-next-line
    const [postValues, setPostValues] = useState({
        data: null,
        loading: true,
        error: null,
    });

    const [scenarioComponents, setScenarioComponents] = useState([]);
    const [scenarioComponent, setScenarioComponent] = useState(null);
    const [showEditor, setShowEditor] = useState(false);
    const [addNewPageIndex, setAddNewPageIndex] = useState(null);
    const [currentPageID, setCurrentPageID] = useState(-1);

    let handleLogisticsGet = function handleLogisticsGet() {
        let initialComponents = [
            {
                id: -1,
                title: 'Logistics',
                component: <Logistics />,
            },
            {
                id: -2,
                title: 'Configure Issues',
                component: <ConfigureIssues />,
            },
            {
                id: -3,
                title: 'Conversation Editor',
                component: <ConversationEditor />,
            },
            {
                id: -4,
                title: 'Issue Coverage Matrix',
                component: <ICMatrix />,
            },
            {
                id: -5,
                title: 'Flow Diagram',
                component: <FlowDiagram />,
            },
            {
                id: -6,
                title: 'Consequences',
                component: <Consequences />,
            },
        ];

        const endpoint = '/logistics?scenario=' + scenario_ID;

        function onSuccess(resp) {
            let p = null;
            let logistics_and_pages = resp.data;
            p = {
                scenario_ID: logistics_and_pages.SCENARIO_ID,
                version_ID: logistics_and_pages.VERSION,
                title: logistics_and_pages.NAME,
                is_finished: logistics_and_pages.IS_FINISHED,
                public_scenario: logistics_and_pages.PUBLIC,
                num_convos: logistics_and_pages.NUM_CONVERSATION,
                professors: [logistics_and_pages.PROFESSOR],
                courses: logistics_and_pages.COURSES,
            };

            initialComponents[0].component = <Logistics {...p}></Logistics>;
            initialComponents[1].component = (
                <ConfigureIssues scenario_ID={p.scenario_ID}></ConfigureIssues>
            );
            initialComponents[2].component = (
                <ConversationEditor
                    scenario_ID={p.scenario_ID}
                ></ConversationEditor>
            );
            initialComponents[3].component = (
                <ICMatrix scenario_ID={p.scenario_ID}></ICMatrix>
            );
            initialComponents[4].component = (
                <FlowDiagram scenario_ID={p.scenario_ID}></FlowDiagram>
            );
            initialComponents[5].component = (
                <Consequences scenario_ID={p.scenario_ID}></Consequences>
            );

            let pages = logistics_and_pages.pages;

            for (let i = 0; i < pages.length; i++) {
                //Already have component in initial components
                if (pages[i].page_type === 'S') {
                    continue;
                }
                //Intro page is first page on sidebar
                if (pages[i].page_type === 'I') {
                    initialComponents.splice(6, 0, {
                        id: pages[i].page,
                        title: pages[i].page_title,
                        isIntroPage: true,
                        component: null,
                    });
                } else {
                    initialComponents.push({
                        id: pages[i].page,
                        title: pages[i].page_title,
                        component: null,
                    });
                }
            }
            setScenarioComponents(initialComponents);
            if (addNewPageIndex) {
                handlePageGet(
                    setGetValues,
                    initialComponents[addNewPageIndex].id,
                    initialComponents
                );
                setAddNewPageIndex(null);
            } else {
                setScenarioComponent(initialComponents[0].component);
            }
            setShowEditor(true);
        }

        function onFailure() {
            //console.log('Failed to get logistics info');
        }

        universalFetch(setGetValues, endpoint, onFailure, onSuccess, {
            scenario: scenario_ID,
        });
    };

    //TODO implement banner
    function handleDelete(setDeleteValues, d_id) {
        const endpoint = '/page?page_id=' + d_id;
        function onSuccess(resp) {
            setSuccessBannerFade(true);
            setSuccessBannerMessage('Successfully deleted page!');
            setShowEditor(true);
        }
        function onFailure() {
            setErrorBannerFade(true);
            setErrorBannerMessage('Failed to save page! Please try again.');
        }

        universalDelete(setDeleteValues, endpoint, onFailure, onSuccess, {
            page: d_id,
        });
    }

    function handlePageGet(setGetValues, g_id, scenarioComponentsArray) {
        const endpoint = '/page?page_id=' + g_id;

        function onSuccess(resp) {
            let p = null;
            let c = null;

            let currPageInfo = resp.data;
            if (currPageInfo.page_type === 'I') {
                p = {
                    scenarioComponents: scenarioComponentsArray,
                    setScenarioComponents: setScenarioComponents,
                    setCurrentPageID: setCurrentPageID,
                    page_id: currPageInfo.page,
                    page_type: currPageInfo.page_type,
                    page_title: currPageInfo.page_title,
                    scenario_ID: currPageInfo.scenario,
                    version_ID: tempversionid,
                    next_page: currPageInfo.next_page,
                    next_page_version: 0,
                    body: currPageInfo.page_body,
                    bodies: currPageInfo.bodies,
                    xCoord: currPageInfo.x_coordinate,
                    yCoord: currPageInfo.y_coordinate,
                    created: false,
                };
                c = <Introduction {...p}></Introduction>;
            } else if (currPageInfo.page_type === 'G') {
                p = {
                    scenarioComponents: scenarioComponentsArray,
                    setScenarioComponents: setScenarioComponents,
                    setCurrentPageID: setCurrentPageID,
                    page_id: currPageInfo.page,
                    page_type: currPageInfo.page_type,
                    page_title: currPageInfo.page_title,
                    scenario_ID: currPageInfo.scenario,
                    version_ID: tempversionid,
                    next_page: currPageInfo.next_page,
                    next_page_version: 0,
                    body: currPageInfo.page_body,
                    bodies: currPageInfo.bodies,
                    xCoord: currPageInfo.x_coordinate,
                    yCoord: currPageInfo.y_coordinate,
                    created: false,
                };
                c = <Generic {...p}></Generic>;
            } else if (currPageInfo.page_type === 'A') {
                p = {
                    scenarioComponents: scenarioComponentsArray,
                    setScenarioComponents: setScenarioComponents,
                    setCurrentPageID: setCurrentPageID,
                    page_id: currPageInfo.page,
                    page_type: currPageInfo.page_type,
                    page_title: currPageInfo.page_title,
                    scenario_ID: currPageInfo.scenario,
                    next_page: currPageInfo.next_page,
                    next_page_version: 0,
                    version_ID: tempversionid,
                    body: currPageInfo.page_body,
                    choice1: currPageInfo.choices[0]
                        ? currPageInfo.choices[0].choice
                        : '',
                    r1: currPageInfo.choices[0]
                        ? currPageInfo.choices[0].result_page
                        : null,
                    choice2: currPageInfo.choices[1]
                        ? currPageInfo.choices[1].choice
                        : '',
                    r2: currPageInfo.choices[1]
                        ? currPageInfo.choices[1].result_page
                        : null,
                    xCoord: currPageInfo.x_coordinate,
                    yCoord: currPageInfo.y_coordinate,
                    created: false,
                };
                c = <Action {...p}></Action>;
            } else if (currPageInfo.page_type === 'R') {
                p = {
                    scenarioComponents: scenarioComponentsArray,
                    setScenarioComponents: setScenarioComponents,
                    setCurrentPageID: setCurrentPageID,
                    page_id: currPageInfo.page,
                    page_type: currPageInfo.page_type,
                    page_title: currPageInfo.page_title,
                    scenario_ID: currPageInfo.scenario,
                    version_ID: tempversionid,
                    next_page: currPageInfo.next_page,
                    next_page_version: 0,
                    body: currPageInfo.page_body,
                    reflection_questions: currPageInfo.reflection_questions,
                    xCoord: currPageInfo.x_coordinate,
                    yCoord: currPageInfo.y_coordinate,
                    created: false,
                };
                c = <Reflection {...p}></Reflection>;
            }

            let newScenarioComponents = [...scenarioComponentsArray];
            newScenarioComponents = newScenarioComponents.map((x) =>
                x.id === resp.data.page ? { ...x, component: c } : x
            );
            setCurrentPageID(currPageInfo.page);
            setScenarioComponents(newScenarioComponents);
            setScenarioComponent(c);
            setShowComponent(true);
        }

        function onFailure() {
            //console.log('Get failed');
        }

        universalFetch(setGetValues, endpoint, onFailure, onSuccess, {
            page: g_id,
        });
    }

    const classes = useStyles();
    const theme = useTheme();
    const [open, setOpen] = React.useState(false);
    const handleDrawerOpen = () => {
        setOpen(true);
    };
    const handleDrawerClose = () => {
        setOpen(false);
    };

    const WhiteTextTypography = withStyles({
        root: {
            color: '#FFFFFF',
        },
    })(Typography);

    const BlackTextTypography = withStyles({
        root: {
            color: '#000000',
        },
    })(Typography);

    const [shouldFetch, setShouldFetch] = useState(0);
    useEffect(handleLogisticsGet, [shouldFetch]);

    let onClick = (id, title, scenarioPages) => {
        setCurrentPageID(id);
        if (
            id !== -1 &&
            id !== -2 &&
            id !== -3 &&
            id !== -4 &&
            id !== -5 &&
            id !== -6
        ) {
            handlePageGet(setGetValues, id, scenarioPages);
        }
        setScenarioComponent(
            scenarioComponents.find((x) => x.id === id).component
        );
    };

    const deleteByID = (d_id) => {
        //If on page that is going to be deleted, redirect back to logistics page
        if (
            scenarioComponents.filter((i) => i.id === d_id)[0].id ===
            currentPageID
        ) {
            setCurrentPageID(-1);
            setScenarioComponent(scenarioComponents[0].component);
        }
        setScenarioComponents(scenarioComponents.filter((i) => i.id !== d_id));
        setShowEditor(false);
        handleDelete(setDeleteValues, d_id);
    };

    const [successBannerMessage, setSuccessBannerMessage] = useState('');
    const [successBannerFade, setSuccessBannerFade] = useState(false);

    useEffect(() => {
        const timeout = setTimeout(() => {
            setSuccessBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [successBannerFade]);

    const [errorBannerMessage, setErrorBannerMessage] = useState('');
    const [errorBannerFade, setErrorBannerFade] = useState(false);

    useEffect(() => {
        const timeout = setTimeout(() => {
            setErrorBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [errorBannerFade]);

    function Sidebar() {
        const classes = useStyles();

        const addNewPage = (pageType, pageName, pageBody) => {
            setShowComponent(false);
            const endpoint = '/api/pages/';
            // eslint-disable-next-line
            let c = null;
            // eslint-disable-next-line
            let p = null;
            let postReqBody;

            function onSuccess(resp) {
                setAddNewPageIndex(scenarioComponents.length);
                setShouldFetch(shouldFetch + 1);
            }

            function onFailure() {
                setShowEditor(true);
            }

            switch (pageType) {
                case 'Generic':
                    postReqBody = {
                        page_type: 'G',
                        page_title: pageName,
                        page_body: pageBody,
                        scenario: scenario_ID,
                        version: 70, //
                        next_page: null,
                        //next_page_version: null,
                        x_coordinate: 0,
                        y_coordinate: 0,
                    };

                    p = {
                        setScenarioComponents: setScenarioComponents,
                        page_type: 'G',
                        page_title: pageName,
                        scenario: scenario_ID,
                        body: pageBody,
                        bodies: [],
                        version_ID: 70,
                        next_page: null,
                        //next_page_version: null,
                        created: true,
                        xCoord: 0,
                        yCoord: 0,
                    };
                    break;
                case 'Reflection':
                    postReqBody = {
                        page_type: 'R',
                        page_title: pageName,
                        page_body: pageBody,
                        scenario: scenario_ID,
                        version: 80,
                        next_page: null,
                        //next_page_version: null,
                        x_coordinate: 0,
                        y_coordinate: 0,
                    };
                    p = {
                        setScenarioComponents: setScenarioComponents,
                        page_type: 'R',
                        page_title: pageName,
                        scenario_ID: scenario_ID,
                        version_ID: 80,
                        next_page: null,
                        //next_page_version: null,
                        body: pageBody,
                        reflection_questions: [],
                        created: true,
                        xCoord: 0,
                        yCoord: 0,
                    };
                    break;
                case 'Action':
                    postReqBody = {
                        page_type: 'A',
                        page_title: pageName,
                        page_body: pageBody,
                        scenario: scenario_ID,
                        version: 90,
                        next_page: null,
                        //next_page_version: null,
                        x_coordinate: 0,
                        y_coordinate: 0,
                    };
                    p = {
                        setScenarioComponents: setScenarioComponents,
                        page_type: 'A',
                        page_title: pageName,
                        scenario_ID: scenario_ID,
                        version_ID: 90,
                        next_page: null,
                        //next_page_version: null,
                        body: pageBody,
                        choice1: '',
                        r1: null,
                        choice2: '',
                        r2: null,
                        created: true,
                        xCoord: 0,
                        yCoord: 0,
                    };
                    break;
                default:
                    c = <Typography>Error</Typography>;
            }

            setShowEditor(false);

            universalPost(
                setPostValues,
                endpoint,
                onFailure,
                onSuccess,
                postReqBody
            );
        };

        function handleAddNewComponent() {
            setOpenPopup(true);
        }

        function openToDoListDialog() {
            setOpenToDo(true);
        }

        return (
            <div>
                <Drawer
                    className={classes.drawer}
                    variant="persistent"
                    anchor="left"
                    open={open}
                    classes={{
                        paper: classes.drawerPaper,
                    }}
                >
                    <IconButton onClick={handleDrawerClose}>
                        {theme.direction === 'ltr' ? (
                            <ChevronLeftIcon />
                        ) : (
                            <ChevronRightIcon />
                        )}
                        <BlackTextTypography variant="h6">
                            Hide Menu
                        </BlackTextTypography>
                    </IconButton>

                    <NavSideBarList
                        onClick={onClick}
                        deleteByID={deleteByID}
                        scenarioPages={scenarioComponents}
                    />
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleAddNewComponent}
                        className={classes.addPageButton}
                    >
                        <AddIcon />
                        Add Page
                    </Button>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={openToDoListDialog}
                        className={classes.addPageButton}
                    >
                        <ViewListIcon />
                        To Do List
                    </Button>
                </Drawer>
                <AddNewSimulationScenarioPageDialog
                    openPopup={openPopup}
                    title="Add New Page"
                    setOpenPopup={setOpenPopup}
                    addPage={addNewPage}
                ></AddNewSimulationScenarioPageDialog>
                <ToDoListDialog
                    openToDo={openToDo}
                    setOpenToDo={setOpenToDo}
                ></ToDoListDialog>
            </div>
        );
    }

    const NavBar = (
        <div>
            <CssBaseline />
            <AppBar
                position="fixed"
                className={clsx(classes.appBar, {
                    [classes.appBarShift]: open,
                })}
            >
                <Toolbar>
                    <Box display="flex" flexGrow={1}>
                        <IconButton
                            color="inherit"
                            aria-label="open drawer"
                            onClick={handleDrawerOpen}
                            edge="start"
                            className={clsx(
                                classes.menuButton,
                                open && classes.hide
                            )}
                        >
                            <MenuIcon />
                        </IconButton>

                        <Typography variant="h4" noWrap>
                            Ethisim Scenario Editor
                        </Typography>
                    </Box>

                    <Button
                        component={Link}
                        to={{
                            pathname: '/dashboard',
                        }}
                        className={classes.exitButton}
                    >
                        <WhiteTextTypography noWrap>
                            Return to Dashboard
                        </WhiteTextTypography>
                    </Button>
                </Toolbar>
            </AppBar>
        </div>
    );

    if (getValues.error) {
        return (
            <div>
                {NavBar}
                <div className={classes.issue}>
                    <div className={classes.container}>
                        <ErrorIcon className={classes.iconError} />
                        <Typography align="center" variant="h3">
                            Error in fetching Scenario Data.
                        </Typography>
                    </div>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleLogisticsGet}
                    >
                        <RefreshIcon className={classes.iconRefreshLarge} />
                    </Button>
                </div>
            </div>
        );
    }

    if (showEditor === false) {
        return <LoadingSpinner />;
    }

    return (
        <div className={classes.container}>
            {NavBar}
            <Sidebar />
            <main
                className={clsx(classes.content1, {
                    [classes.contentShift]: open,
                })}
            >
                <div className={classes.drawerHeader} />
                <div className={classes.bannerContainer}>
                    <SuccessBanner
                        successMessage={successBannerMessage}
                        fade={successBannerFade}
                    />
                    <ErrorBanner
                        errorMessage={errorBannerMessage}
                        fade={errorBannerFade}
                    />
                </div>
                {!getValues.data ||
                scenarioComponent === null ||
                getValues.loading ||
                !showComponent ? (
                    <LoadingSpinner />
                ) : (
                    <div>{scenarioComponent}</div>
                )}
            </main>
        </div>
    );
}
