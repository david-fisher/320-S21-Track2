import React, { useState, useEffect, useRef } from 'react';
import {
    Typography,
    Button,
    Grid,
    TextField,
    MenuItem,
    Dialog,
    DialogTitle,
    DialogContent,
    DialogContentText,
    DialogActions,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import EntryFields from './IssueEntryFieldList';
import get from '../../../universalHTTPRequests/get';
import LoadingSpinner from '../../LoadingSpinner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import PropTypes from 'prop-types';
import IssueMatrix from './IssueCoverageMatrix';
import { baseURL } from '../../../Constants/Config';

import MaterialTable from 'material-table';
import addStakeHolder from '../ConversationEditorComponents/StakeHoldersComponent/stakeHolders';
import HelpIcon from '@material-ui/icons/Help';
import GenericInfoButton from '../../InfoButtons/GenericInfoButton';

//Need scenarioID
const endpointGET = '/api/issues/?SCENARIO=';

const useStyles = makeStyles((theme) => ({
    issue: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    spacing: {
        padding: theme.spacing(1),
    },
    saveButton: {
        margin: theme.spacing(2),
        float: 'right',
        textTransform: 'unset',
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

ICMatrix.propTypes = {
    scenario_ID: PropTypes.number,
};

let values = {};

export default function ICMatrix({ scenario_ID }) {
    //for info button
    const [openHelp, setOpenHelp] = React.useState(false);
    const handleClickOpenHelp = () => {
        setOpenHelp(true);
    };

    const stakeHolders = useRef(null);
    const [isLoading, setLoading] = useState(false); //stores status of whether something is loading

    var axios = require('axios'); //backend
    const [successBannerMessage, setSuccessBannerMessage] = useState(''); //success banner
    const [successBannerFade, setSuccessBannerFade] = useState(false);
    const [errorBannerMessage, setErrorBannerMessage] = useState(''); //error banner
    const [errorBannerFade, setErrorBannerFade] = useState(false);

    /*const addStakeHolders = (data) => {
        // if (!checkTime(setCurrentTime, currentTime)) {
        //     return;
        // }
        // setLoading(true);

        var data = JSON.stringify({
            stakeholder: null,
            version: null,
            name: '',
            description: '',
            job: '',
            introduction: '',
            enable_multi_convo: false,
            scenario: null,
        });

        var config = {
            method: 'post',
            url: baseURL + '/stakeholder',
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };
        axios(config)
            .then(function (response) {
                //console.log(values)
                response.data['name'] = values['name'];
                response.data['description'] = values['description'];
                response.data['introduction'] = values['introduction'];
                response.data['job'] = values['job'];
                saveStakeHolders(response.data);
                // setStakeHolders([...stakeHolders, response.data]);
                // setSuccessBannerMessage(
                //     'Successfully created a new stakeholder!'
                // );
                //setSuccessBannerFade(true);
            })
            .catch(function (error) {
                // setErrorBannerMessage(
                //     'Failed to create a stakeholder! Please try again.'
                // );
                // setErrorBannerFade(true);
            });
    };*/
    const saveStakeHolders = (data) => {
        //var data = [...values]

        var config = {
            method: 'put',
            //url: baseURL + '/multi_stake?scenario=' + scenario_ID,
            //url: baseURL + '/multi_stake?scenario=' + scenario_ID,
            url: baseURL + '/stakeholder',
            headers: {
                'Content-Type': 'application/json',
            },
            data: [data],
        };

        axios(config)
            .then(function (response) {
                getExistingStakeHolders();
                // setSuccessBannerMessage('Successfully add and saved the stakeholders!');
                // setSuccessBannerFade(true);
            })
            .catch(function (error) {
                // setErrorBannerMessage(
                //     'Failed to save the stakeholders! Please try again.'
                // );
                // setErrorBannerFade(true);
            });
    };

    const [open, setOpen] = React.useState(false);
    const [open2, setOpen2] = React.useState(false);

    const handleClickOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        saveStakeHolders(values);
        setOpen(false);
    };
    const handleClickOpen2 = () => {
        setOpen2(true);
    };
    const handleClose2 = () => {
        console.log(issueValues);
        // issueEntryFieldList =[issueValues]
        // setIssueEntryFieldList={setIssueEntryFieldList}
        //scenarioID={scenario_ID}
        getData();
        setOpen2(false);
    };
    const classes = useStyles();
    const [issueEntryFieldList, setIssueEntryFieldList] = useState({
        data: null,
        loading: true,
        error: null,
    });
    const [issueCoverageMatrix, setIssueCoverageMatrix] = useState({
        data: null,
        loading: true,
        error: null,
    });

    useEffect(() => {
        getData();
    }, [stakeHolders]);

    let getData = () => {
        //getExistingStakeHolders()
        get(setIssueEntryFieldList, endpointGET + scenario_ID);
        get(setIssueCoverageMatrix, endpointGET + scenario_ID);
    };

    useEffect(() => {
        stakeHolders.current = [];
        getExistingStakeHolders();
        getData();
    }, []);

    if (issueCoverageMatrix.loading || issueEntryFieldList.loading) {
        return <LoadingSpinner />;
    }

    if (issueEntryFieldList.error) {
        return (
            <div className={classes.issue}>
                <div className={classes.container}>
                    <ErrorIcon className={classes.iconError} />
                    <Typography align="center" variant="h3">
                        Error in fetching issues.
                    </Typography>
                </div>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshLarge} />
                </Button>
            </div>
        );
    }

    const onStakeHolderChange = () => {
        getExistingStakeHolders();
    };

    /*<IssueMatrix onChange = {this.onStakeHolderChange}/>*/

    function getExistingStakeHolders() {
        setLoading(true); //starts loading icon

        var data = { scenario: { scenario_ID } };
        var config = {
            method: 'get',
            url: baseURL + '/stakeholder?scenario_id=' + scenario_ID,
            //url: baseURL + '/stakeholder?scenario_id=' + s,

            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };

        axios(config) //backend call to get data in response
            .then(function (response) {
                stakeHolders.current = response.data;
                setLoading(false);
            })
            .catch(function (error) {
                setErrorBannerMessage(
                    'Failed to get Stakeholders! Please try again.'
                );
                setErrorBannerFade(true);
            });
    }

    //for info button

    if (isLoading) {
        return <LoadingSpinner />;
    }

    let issueValues = {};
    let values = {
        stakeholder: 1,
        version: 1,
        name: '',
        description: '',
        job: '',
        introduction: '',
        enable_multi_convo: false,
        scenario: scenario_ID,
    };
    const getName = (e) => {
        values['name'] = e.target.value;
    };
    const getDes = (e) => {
        values['description'] = e.target.value;
    };
    const getIntro = (e) => {
        values['introduction'] = e.target.value;
    };
    const getJob = (e) => {
        values['job'] = e.target.value;
    };
    const getIssueName = (e) => {
        issueValues['name'] = e.target.value;
    };
    const getImportance = (e) => {
        issueValues['importance_score'] = e.target.value;
    };

    return (
        <div className={classes.issue}>
            <Typography align="center" variant="h2">
                Configure Coverage Scores
            </Typography>
            <Grid container justify="flex-end">
                <Button color="primary" onClick={handleClickOpenHelp}>
                    <HelpIcon />
                </Button>
                <GenericInfoButton
                    description={`On this page, you will notice an issue coverage matrix. This table displays all your stakeholders and the issues associated with them. 
                    There is a search function for ease of access. A running sum is calculated as a column sum for each issue. This table can be exported as a PDF or CSV file. 
                    You can add stakeholders to the Issue Coverage Matrix without leaving the page using the “Add Stakeholder” button. 
                    Clicking this button will show you a popup window with fields like Name, Job, etc. which you can fill in to create a new stakeholder. 
                    You can also create new issues and rate their importance on this page by clicking on the “Add Issue” button.`}
                    open={openHelp}
                    setOpen={setOpenHelp}
                />
            </Grid>
            <div className={classes.spacing}>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshSmall} />
                </Button>
            </div>

            {/* <EntryFields
                issueEntryFieldList={
                    issueEntryFieldList !== null ? issueEntryFieldList : []
                }
                setIssueEntryFieldList={setIssueEntryFieldList}
                scenario_stakeHolders={stakeHolders}
                scenarioID={scenario_ID}
            /> */}

            <Button
                className={classes.button}
                id="button"
                onClick={handleClickOpen2}
                variant="contained"
                color="primary"
            >
                {' '}
                Add Issues
            </Button>

            <Dialog
                open={open2}
                onClose={handleClose2}
                aria-labelledby=""
                aria-describedby=""
            >
                <DialogTitle id="Add Issues">{'Add Issue'}</DialogTitle>
                <Grid container direction="row" justify="centre">
                    <Grid item xs={8}>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Issue Name"
                            label="Issue Name"
                            id="scenariopageAdder"
                            onChange={(e) => getIssueName(e)}
                        ></TextField>

                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Importance Factor"
                            label="Importance Factor"
                            id="scenariopageAdder"
                            onChange={(e) => getImportance(e)}
                        ></TextField>
                    </Grid>
                </Grid>
                <DialogActions>
                    <Button onClick={handleClose2} color="primary">
                        Add
                    </Button>
                </DialogActions>
            </Dialog>

            <Button
                className={classes.button}
                id="button"
                onClick={handleClickOpen}
                variant="contained"
                color="primary"
            >
                {' '}
                Add Stakeholders
            </Button>

            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby=""
                aria-describedby=""
            >
                <DialogTitle id="Add stakeholder">
                    {'Add Stakeholder'}
                </DialogTitle>
                <Grid container direction="row" justify="centre">
                    <Grid item xs={8}>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="StakeHolder name"
                            label="Stakeholder name"
                            id="scenariopageAdder"
                            onChange={(e) => getName(e)}
                        ></TextField>

                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Job"
                            label="Job"
                            id="scenariopageAdder"
                            onChange={(e) => getJob(e)}
                        ></TextField>

                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Description"
                            label="Description"
                            id="scenariopageAdder"
                            onChange={(e) => getDes(e)}
                        ></TextField>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Bio"
                            label="Bio"
                            id="scenariopageAdder"
                            onChange={(e) => getIntro(e)}
                        ></TextField>
                    </Grid>
                </Grid>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Add
                    </Button>
                </DialogActions>
            </Dialog>

            <IssueMatrix /*this might need to be edited, sends scenario id to IssueCoverageMatrix*/
                scenario_stakeHolders={stakeHolders.current}
                scenario={scenario_ID}
                // onChangeStakeHolders={onStakeHolderChange}
            />
        </div>
    );
}
