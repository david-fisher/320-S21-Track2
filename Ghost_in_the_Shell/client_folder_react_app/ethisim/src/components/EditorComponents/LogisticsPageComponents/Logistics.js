import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
//import Author from './Author';
import {
    Button,
    TextField,
    Typography,
    Container,
    Divider,
    Grid,
} from '@material-ui/core';
import put from '../../../universalHTTPRequests/put';
import get from '../../../universalHTTPRequests/get';
import LoadingSpinner from '../../LoadingSpinner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import SuccessBanner from '../../Banners/SuccessBanner';
import ErrorBanner from '../../Banners/ErrorBanner';
import Tags from './DropDown';
import Checkbox from '@material-ui/core/Checkbox';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import PropTypes from 'prop-types';
import HelpIcon from '@material-ui/icons/Help';
import GenericInfoButton from '../../InfoButtons/GenericInfoButton';

const useStyles = makeStyles((theme) => ({
    textfields: {
        '& > *': {
            margin: theme.spacing(1),
            width: '100%',
        },
    },
    buttons: {
        '& > *': {
            margin: theme.spacing(1),
            marginBottom: theme.spacing(1),
            width: '100%',
            //textTransform: 'unset',
        },
    },
    authorButtons: {
        width: '100%',
        display: 'flex',
        flexDirection: 'column',
        textTransform: 'unset',
    },
    subdiv: {
        marginTop: theme.spacing(1),
        width: '750px',
        '@media (max-width: 1100px)': {
            width: '100%',
        },
    },
    bannerContainer: {
        marginTop: theme.spacing(2),
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
    container: {
        padding: theme.spacing(1),
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
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

Logistics.propTypes = {
    scenario_ID: PropTypes.any,
};

export default function Logistics({ scenario_ID }) {
    //Need scenario id
    const endpointGetLogistics = '/logistics?scenario=';
    const endpointGetCourses = '/api/courses/';
    const endPointPut = '/logistics';
    console.log('Logistics');
    console.log(scenario_ID);
    const classes = useStyles();
    //temporary until backend implements id's
    const [fetchCourseResponse, setFetchCourseResponse] = useState({
        data: null,
        loading: false,
        error: null,
    });

    //TODO temporary ID
    // eslint-disable-next-line
    const [id, setId] = useState(scenario_ID);

    //Authors mock implementation
    const [authors, setAuthors] = useState([]);

    //Set fake ID for list item
    let initialAuthorsWithID = authors.map(function (author) {
        return {
            author: author,
            id: Math.floor(Math.random() * 10000),
        };
    });

    const [authorsWithID, setAuthorsWithID] = useState(initialAuthorsWithID);

    let resetAuthorsWithID = (authorsWithID) => {
        let initialAuthorsWithID = authors.map(function (author) {
            return {
                author: author,
                id: Math.floor(Math.random() * 10000),
            };
        });
        setAuthorsWithID(initialAuthorsWithID);
    };

    useEffect(resetAuthorsWithID, [authors]);

    // eslint-disable-next-line
    const removeAuthor = (authorID) => {
        const leftAuthors = authorsWithID.filter(
            (author) => author.id !== authorID
        );
        setAuthorsWithID(leftAuthors);
    };

    // eslint-disable-next-line
    const addAuthor = (e) => {
        let newAuthors = authorsWithID.map((data) => data.author);
        newAuthors = [...newAuthors, ''];
        setAuthors(newAuthors);
        const newAuthorsWithID = [
            ...authorsWithID,
            {
                id: Math.floor(Math.random() * 10000),
                author: '',
            },
        ];
        setAuthorsWithID(newAuthorsWithID);
    };

    // eslint-disable-next-line
    const [shouldFetch, setShouldFetch] = useState(0);
    const [shouldRender, setShouldRender] = useState(false);
    const [fetchLogisticsResponse, setFetchLogisticsResponse] = useState({
        data: null,
        loading: true,
        error: null,
    });
    const [menuCourseItems, setMenuCourseItems] = useState(null);
    // eslint-disable-next-line
    const [responseSave, setResponseSave] = useState({
        data: null,
        loading: false,
        error: null,
    });
    const [successBannerMessage, setSuccessBannerMessage] = useState('');
    const [successBannerFade, setSuccessBannerFade] = useState(false);
    const [errorBannerMessage, setErrorBannerMessage] = useState('');
    const [errorBannerFade, setErrorBannerFade] = useState(false);
    const [errorName, setErrorName] = useState(false);
    const [errorNameText, setErrorNameText] = useState('');
    const [errorNumConvos, setErrorNumConvos] = useState(false);
    const [errorNumConvosText, setErrorNumConvosText] = useState('');
    const [errorCourses, setErrorCourses] = useState(false);
    const [currentCourses, setCurrentCourses] = useState([]);
    const [scenarioName, setScenarioName] = useState('');
    const [numConvos, setNumConvos] = useState(0);
    const [isPublic, setIsPublic] = useState(false);
    const [isFinished, setIsFinished] = useState(false);

    //for info button
    const [open, setOpen] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };

    //For Banners
    useEffect(() => {
        const timeout = setTimeout(() => {
            setSuccessBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [successBannerFade]);

    useEffect(() => {
        const timeout = setTimeout(() => {
            setErrorBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [errorBannerFade]);

    const handleOnChangePublic = (event) => {
        setIsPublic(event.target.checked);
        setEdit({ ...NewScenario, public: event.target.checked });
    };

    const handleOnChangeFinish = (event) => {
        setIsFinished(event.target.checked);
        setEdit({ ...NewScenario, is_finished: event.target.checked });
    };

    const handleOnChangeNumConvo = (event) => {
        NewScenario.num_conversation = event.target.value;
        setNumConvos(event.target.value);
        setEdit(NewScenario);
    };

    const makeNewCourses = (response) => {
        let sel = [];

        for (let i = 0; i < response.length; i++) {
            for (let j = 0; j < NewScenario.courses.length; j++) {
                if (response[i].name === NewScenario.courses[j].name) {
                    sel.push(response[i]);
                }
            }
        }

        NewScenario.courses = sel;
        setCurrentCourses(sel);
        setEdit(NewScenario);
    };

    const [NewScenario, setEdit] = useState({
        scenario: 0,
        version: 0,
        name: '',
        public: false,
        num_conversation: 0,
        is_finished: false,
        date_created: ' ',
        scenario_id: 0,
        courses: [],
    });

    let getData = () => {
        function onSuccess(response) {
            NewScenario.scenario = response.data.scenario;
            NewScenario.version = response.data.version;
            NewScenario.name = response.data.name;
            NewScenario.public = response.data.public;
            NewScenario.num_conversation = response.data.num_conversation;
            NewScenario.is_finished = response.data.is_finished;
            NewScenario.date_created = response.data.data_created;
            NewScenario.courses = response.data.courses;
            NewScenario.scenario_id = response.data.scenario_id;

            setScenarioName(response.data.name);
            setIsFinished(response.data.is_finished);
            setIsPublic(response.data.public);
            setNumConvos(response.data.num_conversation);
            setEdit(NewScenario);
            getCourses();
        }

        //code for implementing authors
        /*
     Authors
                </form>

                {authorsWithID.map((data) => (
                    <Author
                        key={data.id}
                        id={data.id}
                        removeAuthor={removeAuthor}
                        author={data.author}
                        listOfAuthors={authorsWithID}
                        setListOfAuthors={setAuthorsWithID}
                    />
                ))}
                <Button variant="contained" color="primary" onClick={addAuthor}>
                    Add Author
                </Button>
                
        */

        function onFailure() {
            //GET request failed, loading animation should end
            setFetchCourseResponse({
                data: null,
                loading: false,
                error: null,
            });
        }

        //Smooth loading animation, loading animation will not reset during both GET requests (GET logistics and GET courses)
        setFetchCourseResponse({
            data: null,
            loading: true,
            error: null,
        });
        get(
            setFetchLogisticsResponse,
            endpointGetLogistics + id,
            onFailure,
            onSuccess
        );
    };

    let getCourses = () => {
        function onSuccessCourse(response) {
            setMenuCourseItems(response.data);
            makeNewCourses(response.data);
            setShouldRender(true);
        }

        function onFailureCourse() {
            setErrorBannerMessage('Failed to save! Please try again.');
            setErrorBannerFade(true);
        }
        get(
            setFetchCourseResponse,
            endpointGetCourses,
            onFailureCourse,
            onSuccessCourse
        );
    };

    useEffect(getData, [shouldFetch]);

    const handleSave = () => {
        function onSuccessLogistic(response) {
            setSuccessBannerMessage('Successfully Saved!');
            setSuccessBannerFade(true);
        }

        function onFailureLogistic() {
            setErrorBannerMessage('Failed to save! Please try again.');
            setErrorBannerFade(true);
        }

        let validInput = true;

        if (!NewScenario.name || !NewScenario.name.trim()) {
            setErrorName(true);
            setErrorNameText('Scenario name cannot be empty');
            validInput = false;
        } else if (NewScenario.name.length >= 1000) {
            setErrorName(true);
            setErrorNameText(
                'Scenario name must have less than 1000 characters'
            );
            validInput = false;
        } else {
            setErrorName(false);
        }

        if (
            isNaN(NewScenario.num_conversation) ||
            NewScenario.num_conversation === ''
        ) {
            setErrorNumConvos(true);
            setErrorNumConvosText(
                'Max Number of Conversations Must Be A Number'
            );
            validInput = false;
        } else {
            setErrorNumConvos(false);
        }

        if (NewScenario.courses.length === 0) {
            setErrorCourses(true);
            validInput = false;
        } else {
            setErrorCourses(false);
        }

        if (validInput) {
            put(
                setResponseSave,
                endPointPut + '?scenario=' + id,
                onFailureLogistic,
                onSuccessLogistic,
                NewScenario
            );
        } else {
            setErrorBannerFade(true);
            setErrorBannerMessage(
                'There are currently errors within your page. Please fix all errors in order to save.'
            );
        }
    };

    const handleOnChange = (event) => {
        NewScenario.name = event.target.value;
        setScenarioName(event.target.value);
        setEdit(NewScenario);
    };

    const updateSelectedClasses = (selectedClasses) => {
        //set new scenario courses to selected classes
        let sel = [];
        selectedClasses.map((element) =>
            sel.push({ course: element.course, name: element.name })
        );
        NewScenario.courses = sel;
        setCurrentCourses(sel);
        setEdit(NewScenario);
    };

    if (fetchLogisticsResponse.error) {
        return (
            <div className={classes.errorContainer}>
                <ErrorBanner
                    fade={errorBannerFade}
                    errorMessage={errorBannerMessage}
                />
                <div className={classes.container}>
                    <ErrorIcon className={classes.iconError} />
                    <Typography align="center" variant="h3">
                        Error in fetching scenario logistics.
                    </Typography>
                </div>
                <div className={classes.container}>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={getData}
                    >
                        <RefreshIcon className={classes.iconRefreshLarge} />
                    </Button>
                </div>
            </div>
        );
    }

    if (fetchCourseResponse.error) {
        return (
            <div className={classes.errorContainer}>
                <ErrorBanner
                    fade={errorBannerFade}
                    errorMessage={errorBannerMessage}
                />
                <div className={classes.container}>
                    <ErrorIcon className={classes.iconError} />
                    <Typography align="center" variant="h3">
                        Error in fetching scenario courses.
                    </Typography>
                </div>
                <div className={classes.container}>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={getData}
                    >
                        <RefreshIcon className={classes.iconRefreshLarge} />
                    </Button>
                </div>
            </div>
        );
    }

    //Loading for both GET requests
    if (fetchLogisticsResponse.loading || fetchCourseResponse.loading) {
        return <LoadingSpinner />;
    }

    return (
        <div>
            <div className={classes.bannerContainer}>
                <SuccessBanner
                    fade={successBannerFade}
                    successMessage={successBannerMessage}
                />
                <ErrorBanner
                    fade={errorBannerFade}
                    errorMessage={errorBannerMessage}
                />
            </div>
            <Container component="main">
                <Typography align="center" variant="h2">
                    Logistics
                </Typography>
                <Grid container justify="flex-end">
                    <Button color="primary" onClick={handleClickOpen}>
                        <HelpIcon />
                    </Button>
                    <GenericInfoButton
                        description={`If it's your first time using Ethism, you'll see in the top left of the screen an icon of three horizontal lines. 
                        This is the menu and is accessible from all pages.
                        The page you're on is the Logistics page and handles some organizational pieces of your ethical scenario.
                         Here, you can edit the name of your scenario, the courses associated with this scenario, and max number of selected conversations. 
                         By default the max number of selected conversations is zero. However, you may enter the maximum number of stakeholders you would like to permit students to speak with. This will be explained more in depth on the Conversation Editor page.
                          Clicking the “Public” box allows your scenario to be viewed publicly by others. Clicking the “Is Finished” box puts your scenario in the Finished section of the Dashboard, 
                        ready for student distribution. Don’t forget to click “Save” before leaving the page.`}
                        open={open}
                        setOpen={setOpen}
                    />
                </Grid>
                <form
                    className={classes.textfields}
                    noValidate
                    autoComplete="off"
                >
                    Scenario Title
                    {errorName ? (
                        <TextField
                            error
                            helperText={errorNameText}
                            value={scenarioName}
                            rows={1}
                            onChange={handleOnChange}
                        />
                    ) : (
                        <TextField
                            value={scenarioName}
                            rows={1}
                            onChange={handleOnChange}
                        />
                    )}
                    Courses
                    {shouldRender ? (
                        <Tags
                            courses={menuCourseItems}
                            current={currentCourses}
                            update={updateSelectedClasses}
                        />
                    ) : null}
                    {errorCourses ? (
                        <Typography
                            style={{ marginLeft: 15 }}
                            variant="caption"
                            display="block"
                            color="error"
                        >
                            At least one course must be selected
                        </Typography>
                    ) : null}
                    Maximum Number of Conversations Allowed
                    {errorNumConvos ? (
                        <TextField
                            error
                            helperText={errorNumConvosText}
                            value={numConvos}
                            rows={1}
                            onChange={handleOnChangeNumConvo}
                        />
                    ) : (
                        <TextField
                            value={numConvos}
                            rows={1}
                            onChange={handleOnChangeNumConvo}
                        />
                    )}
                    <Divider style={{ margin: '20px 0' }} />
                </form>

                <form style={{ marginLeft: -15, marginTop: 10 }}>
                    <FormControlLabel
                        control={
                            <Checkbox
                                checked={isPublic}
                                onChange={handleOnChangePublic}
                                color="primary"
                            />
                        }
                        label="Make Public"
                        labelPlacement="start"
                    />

                    <FormControlLabel
                        control={
                            <Checkbox
                                checked={isFinished}
                                onChange={handleOnChangeFinish}
                                color="primary"
                            />
                        }
                        label="Publish"
                        labelPlacement="start"
                    />
                </form>

                <div className={classes.subdiv}>
                    <form
                        className={classes.buttons}
                        noValidate
                        autoComplete="off"
                    >
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleSave}
                        >
                            Save Scenario Info
                        </Button>
                    </form>
                </div>
            </Container>
        </div>
    );
}
